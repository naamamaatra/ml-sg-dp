# =============================================================================
# model_baseline.py — Baseline (Non-Private) Neural Network
# =============================================================================
# This module contains:
#   - SimpleNN   : a lightweight two-hidden-layer neural network
#   - train_baseline_model() : trains the model without any privacy mechanism
#
# The baseline provides the "upper bound" of utility against which
# differentially-private models are benchmarked.
# =============================================================================

import time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import streamlit as st
from sklearn.metrics import accuracy_score, f1_score

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ---------------------------------------------------------------------------
# Model hyper-parameters (constants so they are easy to change)
# ---------------------------------------------------------------------------
INPUT_DIM      = 14    # default for Adult Income; overridden dynamically per dataset
HIDDEN_DIM_1   = 64    # neurons in the first hidden layer
HIDDEN_DIM_2   = 32    # neurons in the second hidden layer
OUTPUT_DIM     = 1     # binary classification → single sigmoid neuron

LEARNING_RATE  = 1e-3  # Adam learning rate
DEFAULT_EPOCHS = 10    # default number of training epochs
DEFAULT_BATCH  = 64    # default mini-batch size


# ===========================================================================
# SimpleNN — shared architecture used by both baseline and DP models
# ===========================================================================
class SimpleNN(nn.Module):
    """
    A lightweight feed-forward network for binary classification.

    Architecture
    ------------
    Input (14)  →  Linear(64) → ReLU  →  Linear(32) → ReLU  →  Linear(1) → Sigmoid
    """

    def __init__(
        self,
        input_dim: int  = INPUT_DIM,
        hidden1:   int  = HIDDEN_DIM_1,
        hidden2:   int  = HIDDEN_DIM_2,
        output_dim: int = OUTPUT_DIM,
    ):
        super(SimpleNN, self).__init__()

        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden1),
            nn.ReLU(),
            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Linear(hidden2, output_dim),
            nn.Sigmoid(),   # output ∈ (0, 1) — interpreted as P(income > 50K)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


# ===========================================================================
# Baseline training function
# ===========================================================================
def train_baseline_model(
    X_train:     np.ndarray,
    y_train:     np.ndarray,
    X_test:      np.ndarray,
    y_test:      np.ndarray,
    epochs:      int   = DEFAULT_EPOCHS,
    batch_size:  int   = DEFAULT_BATCH,
    lr:          float = LEARNING_RATE,
    input_dim:   int   = INPUT_DIM,   # ← dynamic: set from X_train.shape[1]
    progress_bar=None,   # optional Streamlit progress bar widget
    status_text =None,   # optional Streamlit text widget for status updates
) -> dict:
    """
    Train the baseline model with standard Adam optimiser (no privacy).

    Parameters
    ----------
    X_train, y_train : training features and labels (numpy)
    X_test,  y_test  : test features and labels (numpy)
    epochs           : number of full passes over the training data
    batch_size       : mini-batch size
    lr               : Adam learning rate
    progress_bar     : st.progress() widget (optional)
    status_text      : st.empty()  widget (optional)

    Returns
    -------
    dict with keys: model, accuracy, f1, train_history, test_history, training_time
    """

    # Set seeds again for function-level reproducibility
    torch.manual_seed(RANDOM_SEED)

    # ------------------------------------------------------------------
    # 1. Build PyTorch DataLoader
    # ------------------------------------------------------------------
    X_tr_t = torch.tensor(X_train, dtype=torch.float32)
    y_tr_t = torch.tensor(y_train, dtype=torch.float32)
    X_te_t = torch.tensor(X_test,  dtype=torch.float32)
    y_te_t = torch.tensor(y_test,  dtype=torch.float32)

    train_dataset = TensorDataset(X_tr_t, y_tr_t)
    train_loader  = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True, drop_last=False
    )

    # ------------------------------------------------------------------
    # 2. Initialise model, loss and optimiser
    #    input_dim is passed dynamically so the model adapts to any dataset
    # ------------------------------------------------------------------
    model     = SimpleNN(input_dim=input_dim)
    criterion = nn.BCELoss()   # Binary Cross-Entropy
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # ------------------------------------------------------------------
    # 3. Training loop
    # ------------------------------------------------------------------
    train_acc_history = []
    test_acc_history  = []
    start_time        = time.time()

    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0

        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch).squeeze(1)   # shape (batch,)
            loss    = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        # ------------------------------------------------------------------
        # Evaluate on training and test sets at end of each epoch
        # ------------------------------------------------------------------
        model.eval()
        with torch.no_grad():
            # Training metrics
            train_preds = (model(X_tr_t).squeeze(1) >= 0.5).numpy().astype(int)
            train_acc   = accuracy_score(y_train, train_preds)

            # Test metrics
            test_preds  = (model(X_te_t).squeeze(1) >= 0.5).numpy().astype(int)
            test_acc    = accuracy_score(y_test, test_preds)

        train_acc_history.append(train_acc)
        test_acc_history.append(test_acc)

        # ------------------------------------------------------------------
        # Update Streamlit widgets (if provided)
        # ------------------------------------------------------------------
        if progress_bar is not None:
            progress_bar.progress(epoch / epochs)
        if status_text is not None:
            status_text.text(
                f"Baseline | Epoch {epoch}/{epochs} — "
                f"Train Acc: {train_acc:.4f} | Test Acc: {test_acc:.4f}"
            )

    training_time = time.time() - start_time

    # ------------------------------------------------------------------
    # 4. Final evaluation on the test set
    # ------------------------------------------------------------------
    model.eval()
    with torch.no_grad():
        test_probs = model(X_te_t).squeeze(1).numpy()
        test_preds = (test_probs >= 0.5).astype(int)

    final_accuracy = accuracy_score(y_test, test_preds)
    final_f1       = f1_score(y_test, test_preds, average="binary")

    return {
        "model"         : model,
        "accuracy"      : final_accuracy,
        "f1"            : final_f1,
        "train_history" : train_acc_history,
        "test_history"  : test_acc_history,
        "training_time" : training_time,
        "epsilon"       : None,   # no privacy guarantee
        "attack_adv"    : None,   # computed separately in model_dp_sgd.py
    }
