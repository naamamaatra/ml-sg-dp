# =============================================================================
# data_loader.py — Multi-Dataset Loader (Built-in + CSV Upload)
# =============================================================================
# Supports:
#   Built-in datasets  : Adult Income, Heart Disease, Diabetes (Pima)
#   User uploads       : Any binary-classification CSV file
#
# All paths return the same signature:
#   X_train, X_test, y_train, y_test, feature_names, stats
# =============================================================================

import io
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# ---------------------------------------------------------------------------
# Random seed & split ratio
# ---------------------------------------------------------------------------
RANDOM_SEED = 42
TEST_SIZE    = 0.20

# ---------------------------------------------------------------------------
# Built-in Dataset Catalogue
# ---------------------------------------------------------------------------
BUILTIN_DATASETS = {

    "🏦 Adult Income": {
        "url": (
            "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
        ),
        "columns": [
            "age", "workclass", "fnlwgt", "education", "education_num",
            "marital_status", "occupation", "relationship", "race", "sex",
            "capital_gain", "capital_loss", "hours_per_week", "native_country", "income",
        ],
        "target"      : "income",
        "categorical" : [
            "workclass", "education", "marital_status",
            "occupation", "relationship", "race", "sex", "native_country",
        ],
        "na_values"   : "?",
        "sep"         : ",",
        "header"      : None,           # no header row in file
        "binarize"    : None,           # target already binary-ish after encode
        "description" : (
            "Predict whether a person earns **>$50K/year** based on census features. "
            "48,842 records · 14 features."
        ),
        "task"        : "Income > $50K?",
    },

    "❤️ Heart Disease": {
        "url": (
            "https://archive.ics.uci.edu/ml/machine-learning-databases/"
            "heart-disease/processed.cleveland.data"
        ),
        "columns": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope",
            "ca", "thal", "target",
        ],
        "target"      : "target",
        "categorical" : [],             # all values are numeric codes
        "na_values"   : "?",
        "sep"         : ",",
        "header"      : None,
        "binarize"    : True,           # values 1-4 → 1 (has disease), 0 → 0
        "description" : (
            "Predict presence of **heart disease** from clinical measurements. "
            "303 records · 13 features. Great example of sensitive medical data."
        ),
        "task"        : "Heart disease present?",
    },

    "💉 Diabetes (Pima)": {
        "url": (
            "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
        ),
        "columns"     : None,           # file has its own header row
        "target"      : "Outcome",
        "categorical" : [],             # all numerical
        "na_values"   : None,
        "sep"         : ",",
        "header"      : 0,              # first row is the header
        "binarize"    : None,
        "description" : (
            "Predict **diabetes diagnosis** for Pima Indian women based on "
            "medical measurements. 768 records · 8 features."
        ),
        "task"        : "Diabetic?",
    },
}


# ===========================================================================
# Built-in dataset loader
# ===========================================================================
@st.cache_data(show_spinner=False)
def load_builtin_data(dataset_name: str):
    """
    Download and preprocess one of the built-in datasets.

    Parameters
    ----------
    dataset_name : key in BUILTIN_DATASETS (e.g. "❤️ Heart Disease")

    Returns
    -------
    X_train, X_test, y_train, y_test  — numpy float32 arrays
    feature_names                     — list[str]
    stats                             — dict for UI display
    """
    cfg = BUILTIN_DATASETS[dataset_name]

    # ------------------------------------------------------------------
    # 1. Download
    # ------------------------------------------------------------------
    try:
        df = pd.read_csv(
            cfg["url"],
            names     = cfg["columns"],
            sep       = cfg["sep"],
            header    = cfg["header"],
            na_values = cfg["na_values"],
            skipinitialspace=True,
        )
    except Exception as e:
        st.error(f"Failed to download **{dataset_name}**: {e}")
        raise

    # ------------------------------------------------------------------
    # 2. Drop missing rows
    # ------------------------------------------------------------------
    original_len = len(df)
    df.dropna(inplace=True)
    dropped = original_len - len(df)

    # ------------------------------------------------------------------
    # 3. Binarise target if needed (Heart Disease: 0 vs 1-4)
    # ------------------------------------------------------------------
    target_col = cfg["target"]
    if cfg.get("binarize"):
        df[target_col] = (df[target_col].astype(float) > 0).astype(int)
    elif df[target_col].dtype == object:
        # Adult Income style — strip whitespace and encode ">50K" → 1
        df[target_col] = df[target_col].str.strip()
        df[target_col] = df[target_col].str.contains(">50K", na=False).astype(int)
    else:
        df[target_col] = df[target_col].astype(int)

    # ------------------------------------------------------------------
    # 4. Encode categorical features
    # ------------------------------------------------------------------
    for col in cfg["categorical"]:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))

    # ------------------------------------------------------------------
    # 5. Split features / target → train/test
    # ------------------------------------------------------------------
    feature_names = [c for c in df.columns if c != target_col]
    X = df[feature_names].values.astype(np.float32)
    y = df[target_col].values.astype(np.float32)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED, stratify=y
    )

    # ------------------------------------------------------------------
    # 6. Normalise (fit on train only)
    # ------------------------------------------------------------------
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train).astype(np.float32)
    X_test  = scaler.transform(X_test).astype(np.float32)

    # ------------------------------------------------------------------
    # 7. Stats for UI
    # ------------------------------------------------------------------
    n_pos = int(y.sum())
    n_neg = len(y) - n_pos
    stats = {
        "dataset_name"  : dataset_name,
        "description"   : cfg["description"],
        "task"          : cfg["task"],
        "total_samples" : len(df),
        "train_samples" : len(X_train),
        "test_samples"  : len(X_test),
        "n_features"    : X_train.shape[1],
        "n_positive"    : n_pos,
        "n_negative"    : n_neg,
        "positive_pct"  : round(100 * n_pos / len(y), 1),
        "negative_pct"  : round(100 * n_neg / len(y), 1),
        "dropped_rows"  : dropped,
        "source"        : "builtin",
    }

    return X_train, X_test, y_train, y_test, feature_names, stats


# ===========================================================================
# Uploaded CSV loader
# ===========================================================================
def load_uploaded_data(uploaded_file, target_col: str):
    """
    Preprocess a user-uploaded CSV file for binary classification.

    Auto-detects:
      - Numerical columns    → StandardScaler
      - Categorical columns  → LabelEncoder
      - Missing values       → drop rows with any NaN

    Parameters
    ----------
    uploaded_file : Streamlit UploadedFile object
    target_col    : name of the target/label column chosen by the user

    Returns
    -------
    Same signature as load_builtin_data()
    """
    # ------------------------------------------------------------------
    # 1. Read CSV
    # ------------------------------------------------------------------
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Could not read the uploaded file: {e}")
        raise

    if target_col not in df.columns:
        st.error(f"Target column **{target_col}** not found in the file.")
        raise ValueError(f"Column '{target_col}' not found.")

    # ------------------------------------------------------------------
    # 2. Drop rows with missing values
    # ------------------------------------------------------------------
    original_len = len(df)
    df.dropna(inplace=True)
    dropped = original_len - len(df)

    if len(df) < 50:
        st.error(
            f"After dropping missing rows, only {len(df)} rows remain. "
            "Need at least 50 rows to train."
        )
        raise ValueError("Too few rows after NaN removal.")

    # ------------------------------------------------------------------
    # 3. Encode target — must be binary (0 / 1)
    # ------------------------------------------------------------------
    y_raw    = df[target_col]
    n_classes = y_raw.nunique()

    if n_classes < 2:
        st.error("Target column has only one unique value — cannot train a classifier.")
        raise ValueError("Target is constant.")

    if n_classes > 2:
        st.warning(
            f"⚠️ Target column has **{n_classes} unique values**. "
            "Automatically binarising: the **most frequent class → 0**, all others → 1."
        )
        majority = y_raw.value_counts().index[0]
        df[target_col] = (df[target_col] != majority).astype(int)
    else:
        # Binary — encode as 0/1
        le_target = LabelEncoder()
        df[target_col] = le_target.fit_transform(df[target_col].astype(str))

    # ------------------------------------------------------------------
    # 4. Auto-detect and encode categorical feature columns
    # ------------------------------------------------------------------
    feature_cols = [c for c in df.columns if c != target_col]

    for col in feature_cols:
        if df[col].dtype == object or str(df[col].dtype) == "category":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))

    # ------------------------------------------------------------------
    # 5. Features + target split
    # ------------------------------------------------------------------
    X = df[feature_cols].values.astype(np.float32)
    y = df[target_col].values.astype(np.float32)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED, stratify=y
    )

    # ------------------------------------------------------------------
    # 6. Normalise
    # ------------------------------------------------------------------
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train).astype(np.float32)
    X_test  = scaler.transform(X_test).astype(np.float32)

    # ------------------------------------------------------------------
    # 7. Stats
    # ------------------------------------------------------------------
    n_pos = int(y.sum())
    n_neg = len(y) - n_pos
    stats = {
        "dataset_name"  : uploaded_file.name,
        "description"   : f"User-uploaded file: **{uploaded_file.name}**",
        "task"          : f"Predict `{target_col}`",
        "total_samples" : len(df),
        "train_samples" : len(X_train),
        "test_samples"  : len(X_test),
        "n_features"    : X_train.shape[1],
        "n_positive"    : n_pos,
        "n_negative"    : n_neg,
        "positive_pct"  : round(100 * n_pos / len(y), 1),
        "negative_pct"  : round(100 * n_neg / len(y), 1),
        "dropped_rows"  : dropped,
        "source"        : "upload",
    }

    return X_train, X_test, y_train, y_test, feature_cols, stats


# ---------------------------------------------------------------------------
# Legacy shim — keeps backward compatibility with any cached calls to load_data()
# ---------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data():
    """Backward-compatible wrapper — loads Adult Income by default."""
    return load_builtin_data("🏦 Adult Income")
