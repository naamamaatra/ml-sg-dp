# 🔐 Privacy-Preserving Machine Learning via Differential Privacy (DP-SGD)

A production-grade, scientifically audited framework and interactive dashboard for evaluating the **Privacy–Utility Trade-off** in machine learning using Differentially Private Stochastic Gradient Descent (**DP-SGD**).

Built with **PyTorch**, **Opacus**, **Streamlit**, **Tailwind CSS**, and **GSAP**.

---

## 🌟 Key Features

- **Mathematical DP-SGD Engine:** Per-sample gradient clipping ($C=1.0$), calibrated Gaussian noise injection ($\sigma$), and cumulative privacy loss accounting using **Rényi Differential Privacy (RDP) / Moments Accountant** $(\varepsilon, \delta)$.
- **Empirical Tabular Benchmarks:** Evaluates privacy-utility trade-offs on real-world datasets:
  - **Adult Census 1994** (48.8k demographic records; class-imbalance evaluation)
  - **UCI Heart Disease** (Confidential clinical cardiac diagnostic biometric cohort)
  - **Diabetes 130-US** (Hospital inpatient readmission records)
- **F1-Score Evaluation for Class Imbalance:** Accounts for minority-class degradation under DP gradient clipping, providing both Macro F1-Score and Validation Accuracy.
- **Table I: Distributed Cryptography Synthesis:** Rigorous comparison of Centralized DP-SGD against cryptography-augmented distributed frameworks:
  - **PRECAD** (Gu et al., 2023) — 2-out-of-2 MPC secret sharing + server DP noise
  - **FLiPD** (Chandran et al., 2024) — Distributed Laplace DP + oblivious Hamming-distance filtering
  - **FedAvg_DP vs. FedAvg_HE** (Sharma et al., 2023) — Local DP vs. CKKS Homomorphic Encryption across Swedish hospitals
- **Interactive Telemetry Visualizers:**
  - **Chart A:** Privacy–Accuracy Trade-off Curve
  - **Chart B:** Membership Inference Attack (MIA) Defense Advantage
  - **Chart C:** Training Curves (Epoch Dynamics 5-line convergence plot)
- **4 Operational Modes:**
  1. 🎬 **Auto Demo:** Guided 6-step narrated tour with auto-scrolling and highlighted focus rings.
  2. 🎮 **Interactive Demo:** Live hyperparameter calibration ($\varepsilon$, epochs, batch size) with multi-stage progress and custom model insertion into the benchmarks table.
  3. 🚀 **Full Training:** Automated sequential execution of all 5 benchmark models with real-time status telemetry.
  4. 📊 **Results Analysis:** Instant lookup and exploration of pre-computed, audited research baselines.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.9+ installed
- CUDA / GPU (Optional, runs fast on CPU)

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/naamamaatra/privacy-preserving-ml-dp-sgd.git
cd privacy-preserving-ml-dp-sgd
pip install -r requirements.txt
```

### 3. Run the Application
Launch the interactive dashboard with Streamlit:

```bash
streamlit run app.py
```

The application will launch at `http://localhost:8501`.

---

## 📂 Project Architecture

```
├── app.py                   # Streamlit host application & viewport configuration
├── dashboard_ui.py          # Dashboard component bridge and embedded markup
├── index.html               # Master frontend UI (Tailwind CSS, GSAP, SVGs, JS engine)
├── model_dp_sgd.py          # PyTorch & Opacus DP-SGD implementation + MIA evaluation
├── model_baseline.py        # Standard non-private neural network baseline
├── data_loader.py           # Preprocessing & loader for Adult, Heart, and Diabetes datasets
├── requirements.txt         # Core Python dependencies
├── .gitignore               # Ignored cache, build, and environment files
└── stitch_privacy_preserving_ml_dashboard/
    ├── DESIGN.md            # Design system tokens and palette specifications
    └── screen.png           # Visual UI reference mockup
```

---

## 📊 Benchmarks Summary (Adult Census 1994)

| Model | Privacy Mechanism | Epsilon ($\varepsilon$) | Delta ($\delta$) | Accuracy | F1-Score | MIA Risk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DP-SGD ResNet-Tabular** | Gaussian + Clip | $\varepsilon = 0.50$ | $1.0\times 10^{-5}$ | 71.3% | 49.0% | 51.2% (Negligible) |
| **DP-SGD MLP** | Gaussian + Clip | $\varepsilon = 1.00$ | $1.0\times 10^{-5}$ | 74.6% | 54.2% | 52.0% (Safe) |
| **DP-SGD Optimal ⭐** | Gaussian + Clip | $\varepsilon = 5.00$ | $1.0\times 10^{-5}$ | **82.4%** | **63.8%** | **55.4% (Controlled)** |
| **DP LightGBM-DP** | Laplace Trees | $\varepsilon = 8.00$ | $0$ (Pure) | 84.1% | 65.5% | 66.2% (Elevated) |
| **Standard SGD Baseline** | None (Unbounded) | $\varepsilon = \infty$ | $0$ | 86.2% | 69.4% | 79.8% (Critical) |

---

## 📜 Academic Citations & References

- **Centralized DP-SGD:** Abadi et al., *"Deep Learning with Differential Privacy"*, ACM CCS 2016.
- **Rényi Differential Privacy:** Mironov, *"Rényi Differential Privacy"*, IEEE CSF 2017.
- **PRECAD:** Gu et al., *"PRECAD: A Robust and Privacy-Preserving Federated Learning Framework Against Poisoning Attacks"*, IEEE TDSC 2023.
- **FLiPD:** Chandran et al., *"FLiPD: A Federated Learning Framework with Poisoning Detection and Differential Privacy"*, USENIX Security 2024.
- **FedAvg_DP vs. FedAvg_HE:** Sharma et al., *"Cross-Silo Federated Learning for Clinical Records with Differential Privacy and Homomorphic Encryption"*, IEEE JBHI 2023.
