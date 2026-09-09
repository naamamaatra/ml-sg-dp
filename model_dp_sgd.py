# =============================================================================
# model_dp_sgd.py — Differentially-Private SGD Model (Opacus)
# =============================================================================
# This module contains:
#   - train_dp_model()            : trains a SimpleNN with DP-SGD via Opacus
#   - membership_inference_attack(): evaluates membership inference risk
#
# Key DP concepts implemented here:
#   * Per-sample gradient clipping  (max_grad_norm = 1.0)
#   * Gaussian noise addition       (calibrated to (ε, δ)-DP)
#   * Privacy accounting            (Rényi / moments accountant via Opacus)
#
# Reference: Abadi et al. (2016) "Deep Learning with Differential Privacy"
# =============================================================================

import time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import accuracy_score, f1_score

# Opacus: DP-SGD library from Meta Research
try:
    from opacus import PrivacyEngine
    from opacus.validators import ModuleValidator
    OPACUS_AVAILABLE = True
except ImportError:
    OPACUS_AVAILABLE = False

# Re-use the same network architecture as the baseline
from model_baseline import SimpleNN

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ---------------------------------------------------------------------------
# DP hyper-parameters (constants)
# ---------------------------------------------------------------------------
DELTA          = 1e-5    # DP delta — small failure probability
MAX_GRAD_NORM  = 1.0     # L2 clipping threshold for per-sample gradients
LEARNING_RATE  = 0.05    # SGD learning rate (DP-SGD typically uses SGD, not Adam)


# ===========================================================================
# DP-SGD Training
# ===========================================================================
def train_dp_model(
    X_train:      np.ndarray,
    y_train:      np.ndarray,
    X_test:       np.ndarray,
    y_test:       np.ndarray,
    target_epsilon: float = 1.0,
    delta:          float = DELTA,
    epochs:         int   = 10,
    batch_size:     int   = 64,
    max_grad_norm:  float = MAX_GRAD_NORM,
    input_dim:      int   = 14,        # ← dynamic: set from X_train.shape[1]
    progress_bar          = None,   # Streamlit st.progress() widget
    status_text           = None,   # Streamlit st.empty() widget
) -> dict:
    """
    Train a SimpleNN using Differentially-Private SGD (DP-SGD) via Opacus.

    How DP-SGD works
    ----------------
    1. Compute per-sample gradients (not averaged) for a mini-batch.
    2. Clip each per-sample gradient to max_grad_norm (limits sensitivity).
    3. Add calibrated Gaussian noise to the clipped sum.
    4. Divide by batch size → noisy average gradient.
    5. Update weights as in standard SGD.

    The noise scale (σ) is chosen automatically by Opacus such that
    the cumulative privacy cost after all epochs is ≤ target_epsilon.

    Parameters
    ----------
    target_epsilon  : desired final privacy budget ε (e.g. 0.5, 1, 5, 10)
    delta           : DP delta (probability of accidental disclosure)
    epochs          : number of training epochs
    batch_size      : mini-batch size (larger → less privacy cost per epoch)
    max_grad_norm   : clipping bound for per-sample gradients

    Returns
    -------
    dict with model, accuracy, f1, epsilon_spent, attack_advantage, histories
    """

    if not OPACUS_AVAILABLE:
        raise ImportError(
            "Opacus is not installed. Run:  pip install opacus==1.4.1"
        )

    torch.manual_seed(RANDOM_SEED)

    # ------------------------------------------------------------------
    # 1. Build DataLoaders
    #    NOTE: Opacus requires drop_last=True so every batch is the same size
    # ------------------------------------------------------------------
    X_tr_t = torch.tensor(X_train, dtype=torch.float32)
    y_tr_t = torch.tensor(y_train, dtype=torch.float32)
    X_te_t = torch.tensor(X_test,  dtype=torch.float32)
    y_te_t = torch.tensor(y_test,  dtype=torch.float32)

    train_dataset = TensorDataset(X_tr_t, y_tr_t)
    train_loader  = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=True,      # required by Opacus for uniform batch sizes
    )

    # ------------------------------------------------------------------
    # 2. Initialise model
    #    input_dim is passed dynamically so the model adapts to any dataset.
    #    Opacus may need BatchNorm → GroupNorm replacement; SimpleNN
    #    uses no BN so no replacement is needed, but we validate anyway.
    # ------------------------------------------------------------------
    model = SimpleNN(input_dim=input_dim)

    # Validate and fix any incompatible modules (e.g. replace BatchNorm)
    errors = ModuleValidator.validate(model, strict=False)
    if errors:
        model = ModuleValidator.fix(model)

    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=LEARNING_RATE, momentum=0.9)

    # ------------------------------------------------------------------
    # 3. Attach Opacus PrivacyEngine
    #    This wraps the model and optimizer transparently so the rest of
    #    the training loop looks almost identical to standard training.
    # ------------------------------------------------------------------
    privacy_engine = PrivacyEngine()

    model, optimizer, train_loader = privacy_engine.make_private_with_epsilon(
        module        = model,
        optimizer     = optimizer,
        data_loader   = train_loader,
        epochs        = epochs,
        target_epsilon= target_epsilon,
        target_delta  = delta,
        max_grad_norm = max_grad_norm,
    )

    # ------------------------------------------------------------------
    # 4. Training loop (same as baseline — Opacus handles DP internally)
    # ------------------------------------------------------------------
    train_acc_history = []
    test_acc_history  = []
    epsilon_history   = []
    start_time        = time.time()

    for epoch in range(1, epochs + 1):
        model.train()

        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch).squeeze(1)
            loss    = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()   # ← Opacus clips gradients + adds noise here

        # ------------------------------------------------------------------
        # Evaluate on full train/test (no grad needed)
        # ------------------------------------------------------------------
        model.eval()
        with torch.no_grad():
            train_preds = (model(X_tr_t).squeeze(1) >= 0.5).numpy().astype(int)
            train_acc   = accuracy_score(y_train, train_preds)

            test_preds  = (model(X_te_t).squeeze(1) >= 0.5).numpy().astype(int)
            test_acc    = accuracy_score(y_test, test_preds)

        # Query how much privacy budget has been consumed so far
        epsilon_spent = privacy_engine.get_epsilon(delta=delta)

        train_acc_history.append(train_acc)
        test_acc_history.append(test_acc)
        epsilon_history.append(epsilon_spent)

        # ------------------------------------------------------------------
        # Update Streamlit widgets (if provided)
        # ------------------------------------------------------------------
        if progress_bar is not None:
            progress_bar.progress(epoch / epochs)
        if status_text is not None:
            status_text.text(
                f"DP-SGD (ε={target_epsilon}) | Epoch {epoch}/{epochs} — "
                f"Test Acc: {test_acc:.4f} | ε spent: {epsilon_spent:.4f}"
            )

    training_time = time.time() - start_time
    final_epsilon = privacy_engine.get_epsilon(delta=delta)

    # ------------------------------------------------------------------
    # 5. Final evaluation
    # ------------------------------------------------------------------
    model.eval()
    with torch.no_grad():
        test_probs = model(X_te_t).squeeze(1).numpy()
        test_preds = (test_probs >= 0.5).astype(int)

    final_accuracy = accuracy_score(y_test,  test_preds)
    final_f1       = f1_score(y_test, test_preds, average="binary")

    # ------------------------------------------------------------------
    # 6. Membership Inference Attack
    # ------------------------------------------------------------------
    attack_adv = membership_inference_attack(
        model=model,
        X_train=X_train,
        X_test=X_test,
    )

    return {
        "model"          : model,
        "accuracy"       : final_accuracy,
        "f1"             : final_f1,
        "epsilon_target" : target_epsilon,
        "epsilon_spent"  : final_epsilon,
        "delta"          : delta,
        "attack_adv"     : attack_adv,
        "train_history"  : train_acc_history,
        "test_history"   : test_acc_history,
        "epsilon_history": epsilon_history,
        "training_time"  : training_time,
    }


# ===========================================================================
# Membership Inference Attack (simple confidence-based attack)
# ===========================================================================
def membership_inference_attack(
    model,
    X_train: np.ndarray,
    X_test:  np.ndarray,
    sample_size: int = 1000,
) -> float:
    """
    Estimate membership inference vulnerability using a confidence-gap attack.

    Intuition
    ---------
    If a model memorises its training data, it will assign higher confidence
    (closer to 0 or 1) to training samples than to unseen test samples.
    An adversary can exploit this signal to guess whether a record was in
    the training set.

    Attack advantage = mean(|conf_train|) − mean(|conf_test|)
    where conf = model output (probability).

    A perfectly private model → advantage ≈ 0.
    A heavily over-fitted model → advantage can be > 0.1.

    Parameters
    ----------
    model       : trained PyTorch model
    X_train     : training features (numpy)
    X_test      : test features (numpy)
    sample_size : number of samples to draw from each split (for speed)

    Returns
    -------
    float : attack advantage ∈ [0, 1]
    """
    model.eval()
    rng = np.random.default_rng(RANDOM_SEED)

    # Subsample for speed
    train_idx = rng.choice(len(X_train), min(sample_size, len(X_train)), replace=False)
    test_idx  = rng.choice(len(X_test),  min(sample_size, len(X_test)),  replace=False)

    X_tr_sample = torch.tensor(X_train[train_idx], dtype=torch.float32)
    X_te_sample = torch.tensor(X_test[test_idx],   dtype=torch.float32)

    with torch.no_grad():
        # Model outputs are in (0,1); distance from 0.5 = "confidence"
        train_conf = model(X_tr_sample).squeeze(1).numpy()
        test_conf  = model(X_te_sample).squeeze(1).numpy()

    # Convert to confidence (distance from the decision boundary 0.5)
    train_conf_score = np.abs(train_conf - 0.5) * 2   # → [0, 1]
    test_conf_score  = np.abs(test_conf  - 0.5) * 2

    attack_advantage = float(np.mean(train_conf_score) - np.mean(test_conf_score))
    # Clip to [0, 1] in case of numerical weirdness
    return max(0.0, min(1.0, attack_advantage))


# ===========================================================================
# Privacy level helper — maps epsilon to a human-readable label
# ===========================================================================
def get_privacy_level(epsilon: float) -> tuple[str, str]:
    """
    Map an epsilon value to a descriptive privacy label and colour.

    Returns
    -------
    (label, colour) where colour is a CSS/hex colour string
    """
    if epsilon is None:
        return "No Privacy", "#e74c3c"
    elif epsilon <= 1.0:
        return "🔒 Strong Privacy", "#27ae60"
    elif epsilon <= 5.0:
        return "🔐 Moderate Privacy", "#f39c12"
    elif epsilon <= 10.0:
        return "🔓 Weak Privacy", "#e67e22"
    else:
        return "⚠️ Minimal Privacy", "#e74c3c"
