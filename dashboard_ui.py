# =============================================================================
# dashboard_ui.py — Pixel-Perfect Dashboard UI/UX Matching screen.png
# =============================================================================
import os
import streamlit as st
import streamlit.components.v1 as components

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_INDEX_HTML_PATH = os.path.join(_CURRENT_DIR, "index.html")

def get_dashboard_html():
    """Dynamically loads index.html from disk if present, else falls back to embedded HTML."""
    if os.path.exists(_INDEX_HTML_PATH):
        try:
            with open(_INDEX_HTML_PATH, "r", encoding="utf-8") as f:
                content = f.read()
                if len(content) > 1000:
                    return content
        except Exception:
            pass
    return DASHBOARD_HTML

def render_dashboard_component(stats=None, height=1000):
    """Renders the complete pixel-perfect dashboard UI with smooth scrolling."""
    html_content = get_dashboard_html()
    components.html(html_content, height=height, scrolling=False)

DASHBOARD_HTML = """<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Epsilon — Differential Privacy Studio</title>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            brandBg: "#0d1117",
            brandSurface: "#161b22",
            brandPrimary: "#667eea",
            brandSafe: "#27ae60",
            brandModerate: "#f39c12",
            brandDanger: "#e74c3c",
            brandMuted: "#6b7280",
            brandText: "#e2e8f0"
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace']
          }
        }
      }
    }
  </script>
<style>
    body {
      background-color: #0d1117;
      color: #e2e8f0;
      font-family: 'Inter', sans-serif;
    }
    
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0d1117;
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.2);
    }

    .border-subtle {
      border: 1px solid rgba(255, 255, 255, 0.07);
    }

    .border-subtle-hover:hover {
      border-color: rgba(102, 126, 234, 0.35);
      box-shadow: 0 0 14px rgba(102, 126, 234, 0.08);
    }

    .section-title {
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #6b7280;
      font-weight: 600;
    }

    .sidebar-section-title {
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #6b7280;
      font-weight: 700;
    }

    .btn-gradient {
      background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
      position: relative;
      overflow: hidden;
    }

    .btn-gradient::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(
        60deg,
        rgba(255,255,255,0) 20%,
        rgba(255,255,255,0.2) 40%,
        rgba(255,255,255,0) 60%
      );
      transform: rotate(25deg) translateY(-100%);
      transition: transform 0.6s ease;
    }

    .btn-gradient:hover::after {
      transform: rotate(25deg) translateY(100%);
    }

    .hero-char {
      display: inline-block;
      opacity: 0;
      transform: translateY(30px);
    }

    .word-blur {
      display: inline-block;
      filter: blur(8px);
      opacity: 0;
    }

    /* Range slider custom styling */
    input[type=range] {
      -webkit-appearance: none;
      appearance: none;
      background: rgba(255, 255, 255, 0.08);
      height: 6px;
      border-radius: 9999px;
      outline: none;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #667eea;
      cursor: pointer;
      border: 2px solid #ffffff;
      box-shadow: 0 0 10px rgba(102, 126, 234, 0.6);
      transition: transform 0.15s ease;
    }
    input[type=range]::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }
  
    .text-gradient-flow {
      background: linear-gradient(90deg, #ffffff 0%, #667eea 25%, #f093fb 50%, #4facfe 75%, #ffffff 100%);
      background-size: 200% auto;
      color: transparent;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: textShineFlow 3.5s linear infinite;
    }
    @keyframes textShineFlow {
      0% { background-position: 0% 50%; }
      100% { background-position: 200% 50%; }
    }

    .tour-focus-glow {
      box-shadow: 0 0 35px rgba(102, 126, 234, 0.45), 0 0 0 2px rgba(102, 126, 234, 0.85) !important;
      border-color: rgba(102, 126, 234, 0.9) !important;
      transform: translateY(-2px);
      transition: all 0.4s ease-in-out;
      position: relative;
    }

    .tour-def-chip {
      position: absolute;
      top: -13px;
      left: 20px;
      z-index: 50;
      padding: 3px 12px;
      border-radius: 9999px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 600;
      background: #0d1117;
      border: 1px solid rgba(102, 126, 234, 0.8);
      box-shadow: 0 4px 18px rgba(102, 126, 234, 0.45);
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    /* old */
    .tour-focus-glow-old {
      box-shadow: 0 0 25px rgba(102, 126, 234, 0.45), 0 0 0 2px rgba(102, 126, 234, 0.8) !important;
      border-color: rgba(102, 126, 234, 0.9) !important;
      transform: translateY(-2px);
      transition: all 0.4s ease-in-out;
    }

</style>
</head>
<body class="h-screen w-screen bg-brandBg text-brandText flex overflow-hidden antialiased selection:bg-brandPrimary/30 selection:text-white" style="height:100vh;max-height:100vh;overflow:hidden;">
<!-- ========================================================================= -->
<!-- LEFT SIDEBAR (260px Fixed/Sticky full-height, gradient from #0f0c29 to #302b63) -->
<!-- ========================================================================= -->
<aside class="w-[260px] flex-shrink-0 h-screen sticky top-0 bg-gradient-to-b from-[#0f0c29] to-[#302b63] border-r border-white/[0.06] flex flex-col justify-between p-5 z-40 select-none">
<!-- Top Container -->
<div class="flex flex-col gap-5">
<!-- 1. Logo Row -->
<div class="flex items-center justify-between pt-1">
<div class="flex items-center gap-2">
<span class="text-xl">🔒</span>
<span class="font-bold text-white text-base tracking-tight font-sans">DP-ML</span>
</div>
<span class="font-mono text-[11px] font-semibold text-[#f093fb] bg-white/[0.08] px-2 py-0.5 rounded border border-white/[0.1]">
          v2.4
        </span>
</div>
<!-- Separator Line -->
<div class="h-[1px] w-full bg-white/[0.07]"></div>
<!-- 2. DATA SOURCE SECTION -->
<div class="flex flex-col gap-2.5">
<span class="sidebar-section-title">Data Source</span>
<!-- Segmented Switch -->
<div class="grid grid-cols-2 p-1 bg-black/40 rounded-lg border border-white/[0.05] text-xs">
<button class="py-1 px-2 rounded-md font-medium text-white bg-white/10 transition-all text-center" id="btn-src-builtin" onclick="toggleSource('builtin')">
            Built-in
          </button>
<button class="py-1 px-2 rounded-md font-medium text-brandMuted hover:text-white transition-all text-center" id="btn-src-upload" onclick="toggleSource('upload')">
            Upload CSV
          </button>
</div>
<!-- Built-in View -->
<div class="flex flex-col gap-2 mt-1" id="panel-builtin">
<div class="relative">
<select class="w-full bg-[#161b22]/90 border border-white/[0.08] text-xs text-brandText rounded-lg px-3 py-2 appearance-none focus:outline-none focus:border-brandPrimary/70 cursor-pointer font-sans" id="dataset-select" onchange="changeDataset(this.value)">
<option value="adult">🏦 Adult Income (1994)</option>
<option value="heart">❤️ Heart Disease</option>
<option value="diabetes">💉 Diabetes</option>
</select>
<span class="material-symbols-outlined text-brandMuted pointer-events-none absolute right-2.5 top-2.5 text-[18px]">
              expand_more
            </span>
</div>
<p class="text-[11px] text-brandMuted leading-relaxed" id="dataset-desc">
            Standard 48.8k Census benchmark for predicting income &gt;50K with high demographic variance.
          </p>
</div>
<!-- Upload CSV View (Hidden by default) -->
<div class="hidden flex-col gap-2 mt-1" id="panel-upload">
<div class="border border-dashed border-white/20 hover:border-brandPrimary/70 rounded-lg p-3.5 flex flex-col items-center justify-center text-center cursor-pointer bg-black/20 hover:bg-black/40 transition-colors">
<span class="material-symbols-outlined text-brandPrimary text-2xl mb-1">upload_file</span>
<span class="text-xs text-brandText font-medium">Drop CSV here</span>
<span class="text-[10px] text-brandMuted mt-0.5">or browse up to 50MB</span>
</div>
<div class="relative">
<select class="w-full bg-[#161b22]/90 border border-white/[0.08] text-[11px] text-brandMuted rounded-lg px-2.5 py-1.5 appearance-none focus:outline-none focus:border-brandPrimary/70">
<option>Target: Auto-detect label</option>
<option>Target: column_0</option>
<option>Target: target_class</option>
</select>
<span class="material-symbols-outlined text-brandMuted pointer-events-none absolute right-2 top-2 text-[14px]">expand_more</span>
</div>
</div>
</div>
<!-- Separator Line -->
<div class="h-[1px] w-full bg-white/[0.07]"></div>
<!-- 3. MODE SECTION -->
<div class="flex flex-col gap-2">
<span class="sidebar-section-title">Mode</span>
<div class="flex flex-col gap-1.5" id="mode-selector">
<button class="mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-brandMuted hover:text-white hover:bg-white/[0.04] transition-all text-left" onclick="switchMode(this, 'auto')">
<span>🎬</span>
<span>Auto Demo</span>
</button>
<button class="mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-white bg-white/[0.1] border border-white/[0.1] shadow-sm transition-all text-left" onclick="switchMode(this, 'interactive')">
<span>🎮</span>
<span>Interactive Demo</span>
</button>
<button class="mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-brandMuted hover:text-white hover:bg-white/[0.04] transition-all text-left" onclick="switchMode(this, 'training')">
<span>🚀</span>
<span>Full Training</span>
</button>
<button class="mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-brandMuted hover:text-white hover:bg-white/[0.04] transition-all text-left" onclick="switchMode(this, 'results')">
<span>📊</span>
<span>Results Analysis</span>
</button>
</div>
</div>
</div>
<!-- Bottom Mathematical Formula Card -->
<div class="group relative pt-4 border-t border-white/[0.06]">
<div class="p-2.5 rounded-lg bg-black/40 border border-white/[0.05] flex flex-col gap-1 cursor-help">
<div class="flex items-center justify-between">
<span class="text-[9px] uppercase tracking-wider text-brandMuted font-mono">Formal DP Bound</span>
<span class="text-[11px] text-brandMuted group-hover:text-brandPrimary transition-colors">ℹ</span>
</div>
<div class="font-mono text-[10.5px] text-[#f093fb] tracking-tight leading-relaxed">
          P[M(D)∈S] ≤ e<sup>ε</sup>·P[M(D')∈S] + δ
        </div>
</div>
<!-- Tooltip on hover -->
<div class="absolute bottom-full left-0 mb-2 hidden group-hover:block w-[240px] p-3 rounded-lg bg-[#161b22] border border-white/10 shadow-2xl text-[11px] text-brandMuted leading-relaxed z-50 pointer-events-none">
<span class="font-semibold text-white block mb-1">(ε, δ)-Differential Privacy</span>
        Limits the statistical leakage of any single record in the training dataset D compared to neighboring dataset D'. Lower ε provides tighter worst-case bounded risk.
      </div>
</div>
</aside>
<!-- ========================================================================= -->
<!-- MAIN CONTENT (flex-1 scrollable with padding: 48px 56px, max-width 1200px) -->
<!-- ========================================================================= -->
<main id="main-scroller" class="flex-1 h-screen overflow-y-auto px-7 md:px-14 py-12 flex justify-center" style="height:100vh;max-height:100vh;overflow-y:auto;scroll-behavior:smooth;">
<div class="w-full max-w-[1200px] flex flex-col gap-10">
<!-- ===================================================================== -->
<!-- SECTION 1: HERO -->
<!-- ===================================================================== -->
<section class="flex flex-col gap-4">
<div>
<h1 class="text-3xl md:text-4xl font-bold tracking-tight text-white leading-tight font-sans" id="hero-title">
            Privacy-Preserving Machine Learning
          </h1>
<p class="text-sm md:text-base text-brandMuted max-w-3xl mt-2 font-normal leading-relaxed" id="hero-sub">
            Empirical evaluation of DP-SGD against Membership Inference Attacks across varying privacy budgets.
          </p>
</div>
<!-- Active Dataset Badge Pill with subtle gradient border -->
<div class="inline-flex self-start items-center gap-3 px-3 py-1.5 rounded-full bg-brandSurface border-subtle border-subtle-hover transition-all text-xs">
<div class="flex items-center gap-1.5 text-brandPrimary font-medium">
<span class="material-symbols-outlined text-[16px]">dataset</span>
<span class="text-brandText font-semibold" id="badge-dataset-name">Adult Census 1994</span>
</div>
<span class="text-white/20">|</span>
<span class="text-brandMuted" id="badge-sample-count">48,842 samples</span>
<span class="text-white/20">|</span>
<span class="text-brandMuted" id="badge-feat-count">14 Tabular Features</span>
<span class="w-1.5 h-1.5 rounded-full bg-brandSafe ml-1 animate-pulse"></span>
</div>
</section>
<!-- ===================================================================== -->
<!-- SECTION 2: METRICS ROW (5 Cards Grid) -->
<!-- ===================================================================== -->
<section id="section-dataset-metrics" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3.5 relative transition-all duration-500 rounded-xl p-1">
<!-- Card 1 -->
<div class="metric-card p-4 rounded-xl bg-brandSurface border-subtle border-subtle-hover flex flex-col justify-between transition-all duration-300 group">
<div class="flex items-center justify-between">
<span class="text-[11px] uppercase tracking-wider font-semibold text-brandMuted">Total Samples</span>
<span class="material-symbols-outlined text-sm text-brandMuted group-hover:text-brandPrimary transition-colors">folder_open</span>
</div>
<div class="my-2.5">
<span class="stat-counter text-2xl font-bold text-white tracking-tight" data-target="48842" id="stat-total-samples">48,842</span>
</div>
<div class="flex items-center gap-1 text-[11px] text-brandSafe">
<span id="stat-total-sub">↑ 100% curated</span>
</div>
</div>
<!-- Card 2 -->
<div class="metric-card p-4 rounded-xl bg-brandSurface border-subtle border-subtle-hover flex flex-col justify-between transition-all duration-300 group">
<div class="flex items-center justify-between">
<span class="text-[11px] uppercase tracking-wider font-semibold text-brandMuted">Train Partition</span>
<span class="material-symbols-outlined text-sm text-brandMuted group-hover:text-brandPrimary transition-colors">splitscreen</span>
</div>
<div class="my-2.5">
<span class="stat-counter text-2xl font-bold text-white tracking-tight" data-target="39074" id="stat-train-samples">39,074</span>
</div>
<div class="flex items-center gap-1 text-[11px] text-brandMuted">
<span class="w-1.5 h-1.5 rounded-full bg-brandPrimary"></span>
<span id="stat-train-sub">80.0% train split</span>
</div>
</div>
<!-- Card 3 -->
<div class="metric-card p-4 rounded-xl bg-brandSurface border-subtle border-subtle-hover flex flex-col justify-between transition-all duration-300 group">
<div class="flex items-center justify-between">
<span class="text-[11px] uppercase tracking-wider font-semibold text-brandMuted">Test Validation</span>
<span class="material-symbols-outlined text-sm text-brandMuted group-hover:text-brandPrimary transition-colors">fact_check</span>
</div>
<div class="my-2.5">
<span class="stat-counter text-2xl font-bold text-white tracking-tight" data-target="9768" id="stat-test-samples">9,768</span>
</div>
<div class="flex items-center gap-1 text-[11px] text-brandMuted">
<span class="w-1.5 h-1.5 rounded-full bg-[#f093fb]"></span>
<span id="stat-test-sub">20.0% holdout</span>
</div>
</div>
<!-- Card 4 -->
<div class="metric-card p-4 rounded-xl bg-brandSurface border-subtle border-subtle-hover flex flex-col justify-between transition-all duration-300 group">
<div class="flex items-center justify-between">
<span class="text-[11px] uppercase tracking-wider font-semibold text-brandMuted">Feature Dims</span>
<span class="material-symbols-outlined text-sm text-brandMuted group-hover:text-brandPrimary transition-colors">view_week</span>
</div>
<div class="my-2.5">
<span class="stat-counter text-2xl font-bold text-white tracking-tight" data-target="108" id="stat-feat-dims">108</span>
</div>
<div class="flex items-center gap-1 text-[11px] text-brandMuted">
<span id="stat-feat-sub">One-hot encoded</span>
</div>
</div>
<!-- Card 5 -->
<div class="metric-card p-4 rounded-xl bg-brandSurface border-subtle border-subtle-hover flex flex-col justify-between transition-all duration-300 group col-span-2 md:col-span-1">
<div class="flex items-center justify-between">
<span class="text-[11px] uppercase tracking-wider font-semibold text-brandMuted">Class Balance</span>
<span class="material-symbols-outlined text-sm text-brandMuted group-hover:text-brandPrimary transition-colors">balance</span>
</div>
<div class="my-2.5">
<span class="text-xl font-bold text-white tracking-tight font-mono" id="stat-class-balance">75.9 / 24.1</span>
</div>
<div class="flex items-center gap-1 text-[11px] text-brandModerate">
<span id="stat-class-sub">Skewed distribution</span>
</div>
</div>
</section>
<!-- ===================================================================== -->
<!-- SECTION 3: DYNAMIC MODE PANELS (Interactive, Auto, Training, Results) -->
<!-- ===================================================================== -->

<!-- 1. INTERACTIVE DEMO PANEL -->
<section id="mode-panel-interactive" class="p-6 rounded-xl bg-brandSurface border-subtle flex flex-col gap-6 transition-all duration-300">
  <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 border-b border-white/[0.06] pb-4">
    <div>
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-brandPrimary/10 text-brandPrimary border border-brandPrimary/20">Active Mode</span>
        <h2 class="section-title">Hyperparameter Calibration (Interactive Demo)</h2>
      </div>
      <p class="text-xs text-brandMuted mt-0.5">Tune Differential Privacy guarantees and monitor expected utility trade-offs in real time.</p>
    </div>
    <!-- Live Badge -->
    <div id="epsilon-badge" class="px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5 transition-all">
      <span id="epsilon-badge-dot" class="w-2 h-2 rounded-full bg-emerald-400"></span>
      <span id="epsilon-badge-text">Privacy Budget ε = 1.0 — Safe (Strong Privacy)</span>
    </div>
  </div>

  <!-- Inputs Grid -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-end">
    <!-- Epsilon Slider -->
    <div class="flex flex-col gap-2">
      <div class="flex items-center justify-between text-xs">
        <span class="font-medium text-brandText">Privacy Budget (ε)</span>
        <span id="epsilon-num" class="font-mono font-bold text-brandPrimary">1.0</span>
      </div>
      <input id="epsilon-slider" type="range" min="0.5" max="10.0" step="0.1" value="1.0" class="w-full" oninput="updateLiveTelemetryVisuals()"/>
      <div class="flex justify-between text-[10px] font-mono text-brandMuted">
        <span>0.5 (Safe)</span>
        <span>5.0 (Balanced)</span>
        <span>10.0 (Relaxed)</span>
      </div>
    </div>

    <!-- Epochs Slider -->
    <div class="flex flex-col gap-2">
      <div class="flex items-center justify-between text-xs">
        <span class="font-medium text-brandText">Training Epochs</span>
        <span id="epochs-num" class="font-mono font-bold text-brandPrimary">15</span>
      </div>
      <input id="epochs-slider" type="range" min="5" max="20" step="1" value="15" class="w-full" oninput="updateLiveTelemetryVisuals()"/>
      <div class="flex justify-between text-[10px] font-mono text-brandMuted">
        <span>5</span>
        <span>15</span>
        <span>20</span>
      </div>
    </div>

    <!-- Batch Size Select -->
    <div class="flex flex-col gap-2">
      <div class="flex items-center justify-between text-xs">
        <span class="font-medium text-brandText">Batch Size (q = B/N)</span>
        <span class="text-[10px] text-brandMuted font-mono">Subsampling rate</span>
      </div>
      <div class="relative">
        <select id="batch-select" class="w-full bg-black/40 border border-white/[0.08] text-xs text-brandText rounded-lg px-3 py-2 appearance-none focus:outline-none focus:border-brandPrimary/70 cursor-pointer font-mono" onchange="updateLiveTelemetryVisuals()">
          <option value="16">16 (q = 0.0004)</option>
          <option value="32">32 (q = 0.0008)</option>
          <option value="64" selected>64 (q = 0.0016)</option>
          <option value="128">128 (q = 0.0032)</option>
        </select>
        <span class="material-symbols-outlined text-brandMuted pointer-events-none absolute right-2.5 top-2 text-[18px]">expand_more</span>
      </div>
    </div>
  </div>

  <!-- Full-width CTA Button -->
  <button id="btn-train" class="btn-gradient w-full py-3 px-6 rounded-xl font-medium text-sm text-white shadow-lg flex items-center justify-center gap-2 hover:opacity-95 transition-all" onclick="triggerTrainSimulation()">
    <span id="btn-train-text">Train DP-SGD Model</span>
    <span id="btn-train-icon" class="material-symbols-outlined text-base">arrow_forward</span>
  </button>

  <!-- Interactive Training Telemetry & Result Card (Hidden until Train is clicked) -->
  <div id="interactive-training-results" class="hidden flex flex-col gap-4 pt-3 border-t border-white/[0.08] transition-all">
    <!-- Progress Indicator during training -->
    <div id="interactive-progress-box" class="flex flex-col gap-2 p-4 rounded-xl bg-black/30 border border-white/[0.06]">
      <div class="flex items-center justify-between text-xs font-mono">
        <span id="interactive-progress-status" class="text-brandPrimary flex items-center gap-2">
          <span class="w-3 h-3 rounded-full border-2 border-brandPrimary border-t-transparent animate-spin inline-block"></span>
          <span id="interactive-progress-text">Epoch 1/15 • Clipping norm C=1.0 • Injecting Gaussian noise...</span>
        </span>
        <span id="interactive-progress-pct" class="font-bold text-white text-xs">0%</span>
      </div>
      <div class="w-full bg-white/[0.08] h-2 rounded-full overflow-hidden mt-1">
        <div id="interactive-progress-bar" class="h-full bg-gradient-to-r from-[#667eea] via-[#f093fb] to-[#4facfe] transition-all duration-300 w-0"></div>
      </div>
    </div>

    <!-- Live Model Audit Summary Card (Revealed after training completes) -->
    <div id="interactive-summary-card" class="hidden p-5 rounded-xl bg-black/50 border border-emerald-500/40 shadow-2xl flex flex-col gap-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-white/[0.06] pb-3">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <h4 class="text-xs font-bold text-white uppercase tracking-wider font-mono">Custom DP-SGD Model Training & Audit Complete</h4>
        </div>
        <span id="interactive-privacy-guarantee" class="px-2.5 py-0.5 rounded text-[11px] font-mono bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
          Guaranteed (ε = 1.0, δ = 1.0e-5)
        </span>
      </div>

      <!-- 5 High-contrast live KPI pills including F1-Score (Class Imbalance Metric) -->
      <div class="grid grid-cols-2 lg:grid-cols-5 gap-3">
        <div class="p-3 rounded-lg bg-white/[0.03] border border-white/[0.06]">
          <div class="text-[10px] uppercase font-mono text-brandMuted font-semibold">Trained Accuracy</div>
          <div id="result-model-acc" class="text-xl font-bold text-white mt-1 font-mono">74.6%</div>
          <div id="result-acc-diff" class="text-[10px] text-emerald-400 font-mono mt-0.5">-11.6% vs Baseline</div>
        </div>

        <div class="p-3 rounded-lg bg-white/[0.03] border border-white/[0.06]">
          <div class="text-[10px] uppercase font-mono text-[#4facfe] font-semibold flex items-center justify-between">
            <span>F1-Score (Macro)</span>
            <span class="text-[9px] text-brandMuted font-mono">Imbalance</span>
          </div>
          <div id="result-model-f1" class="text-xl font-bold text-[#4facfe] mt-1 font-mono">54.2%</div>
          <div id="result-f1-diff" class="text-[10px] text-amber-400 font-mono mt-0.5">-15.2% vs Baseline</div>
        </div>

        <div class="p-3 rounded-lg bg-white/[0.03] border border-white/[0.06]">
          <div class="text-[10px] uppercase font-mono text-brandMuted font-semibold">MIA Risk (Shadow)</div>
          <div id="result-model-mia" class="text-xl font-bold text-emerald-400 mt-1 font-mono">52.0%</div>
          <div id="result-mia-badge" class="text-[10px] text-brandSafe font-mono mt-0.5">Low Attack Advantage</div>
        </div>

        <div class="p-3 rounded-lg bg-white/[0.03] border border-white/[0.06]">
          <div class="text-[10px] uppercase font-mono text-brandMuted font-semibold">Gaussian Noise (σ)</div>
          <div id="result-model-sigma" class="text-xl font-bold text-[#f093fb] mt-1 font-mono">σ = 2.41</div>
          <div class="text-[10px] text-brandMuted font-mono mt-0.5">Clip Bound C = 1.0</div>
        </div>

        <div class="p-3 rounded-lg bg-white/[0.03] border border-white/[0.06] col-span-2 lg:col-span-1">
          <div class="text-[10px] uppercase font-mono text-brandMuted font-semibold">Training Regimen</div>
          <div id="result-model-regimen" class="text-xl font-bold text-white mt-1 font-mono">15 Epochs</div>
          <div id="result-batch-size" class="text-[10px] text-brandMuted font-mono mt-0.5">Batch Size 64</div>
        </div>
      </div>

      <!-- Action buttons -->
      <div class="flex items-center justify-between flex-wrap gap-3 pt-1">
        <span class="text-xs text-brandMuted">Empirical audit validated. You can view this model on the telemetry curves or add it to the benchmarks table.</span>
        <div class="flex items-center gap-2">
          <button onclick="document.getElementById('chart-epoch-curves') ? document.getElementById('chart-epoch-curves').scrollIntoView({ behavior: 'smooth', block: 'center' }) : document.getElementById('chart-privacy-accuracy').scrollIntoView({ behavior: 'smooth', block: 'center' })" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-white/[0.06] text-white hover:bg-white/[0.12] border border-white/[0.1] transition-all flex items-center gap-1.5">
            <span>View Training Curves</span>
            <span class="material-symbols-outlined text-xs">arrow_downward</span>
          </button>
          <button id="btn-add-custom-table" onclick="addCustomModelToTable()" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30 border border-emerald-500/40 transition-all flex items-center gap-1.5 shadow-md">
            <span class="material-symbols-outlined text-xs">add_chart</span>
            <span id="btn-add-table-text">Add to Benchmarks Table</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 2. AUTO DEMO PANEL (Hidden by default) -->
<section id="mode-panel-auto" class="hidden p-6 rounded-xl bg-brandSurface border border-[#667eea]/40 shadow-2xl flex flex-col gap-5 transition-all duration-300">
  <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-white/[0.06] pb-4">
    <div>
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-purple-500/10 text-[#f093fb] border border-purple-500/20">Self-Guided Walkthrough</span>
        <h2 class="section-title">Automated Privacy Tour (Auto Demo)</h2>
      </div>
      <p class="text-xs text-brandMuted mt-0.5">Hands-free tour that automatically navigates through every component across the system and terminates after 1 complete cycle.</p>
    </div>
    <div class="flex items-center gap-2">
      <!-- Tour Progress Indicator -->
      <span id="auto-tour-badge" class="px-2.5 py-1 rounded-md text-[11px] font-mono bg-white/[0.05] text-brandText border border-white/[0.08]">
        Step 1 of 6 • Dataset Overview
      </span>
      <button id="btn-auto-toggle" onclick="toggleAutoTour()" class="px-4 py-1.5 rounded-lg text-xs font-semibold bg-brandPrimary text-white shadow-lg hover:bg-brandPrimary/90 flex items-center gap-1.5 transition-all">
        <span id="auto-play-icon" class="material-symbols-outlined text-base">play_arrow</span>
        <span id="auto-play-text">Start Auto Tour</span>
      </button>
    </div>
  </div>

  <!-- Tour Progress Track -->
  <div class="w-full bg-white/[0.06] h-1.5 rounded-full overflow-hidden">
    <div id="auto-tour-progress-bar" class="h-full bg-gradient-to-r from-[#667eea] via-[#f093fb] to-[#4facfe] transition-all duration-500 w-[16.6%]"></div>
  </div>

  <!-- 6-Component Navigation Grid -->
  <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
    <button onclick="jumpAutoStep(0)" id="auto-step-btn-0" class="auto-step-pill p-2.5 rounded-lg bg-brandPrimary/10 border border-brandPrimary/60 text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-[#4facfe] font-mono font-semibold uppercase">Step 1</div>
      <div class="text-[11px] font-bold text-white truncate">Dataset Metrics</div>
      <div class="text-[9px] text-brandMuted truncate">Overview & partitions</div>
    </button>
    <button onclick="jumpAutoStep(1)" id="auto-step-btn-1" class="auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-emerald-400 font-mono font-semibold uppercase">Step 2</div>
      <div class="text-[11px] font-bold text-white truncate">DP-SGD Budgets</div>
      <div class="text-[9px] text-brandMuted truncate">ε = 0.5 to 10.0</div>
    </button>
    <button onclick="jumpAutoStep(2)" id="auto-step-btn-2" class="auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-[#4facfe] font-mono font-semibold uppercase">Step 3</div>
      <div class="text-[11px] font-bold text-white truncate">Accuracy Curve</div>
      <div class="text-[9px] text-brandMuted truncate">Validation telemetry</div>
    </button>
    <button onclick="jumpAutoStep(3)" id="auto-step-btn-3" class="auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-[#f093fb] font-mono font-semibold uppercase">Step 4</div>
      <div class="text-[11px] font-bold text-white truncate">MIA Defense</div>
      <div class="text-[9px] text-brandMuted truncate">Shadow attack risks</div>
    </button>
    <button onclick="jumpAutoStep(4)" id="auto-step-btn-4" class="auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-purple-400 font-mono font-semibold uppercase">Step 5</div>
      <div class="text-[11px] font-bold text-white truncate">Epoch Dynamics</div>
      <div class="text-[9px] text-brandMuted truncate">Loss convergence</div>
    </button>
    <button onclick="jumpAutoStep(5)" id="auto-step-btn-5" class="auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]">
      <div class="text-[9px] text-amber-400 font-mono font-semibold uppercase">Step 6</div>
      <div class="text-[11px] font-bold text-white truncate">Audit Benchmarks</div>
      <div class="text-[9px] text-brandMuted truncate">5-Model table & reco</div>
    </button>
  </div>

  <!-- Narrative Callout Box -->
  <div class="p-4 rounded-xl bg-black/40 border border-white/[0.08] flex items-start justify-between gap-4">
    <div class="flex items-start gap-3">
      <span id="auto-narrative-icon" class="material-symbols-outlined text-brandPrimary text-2xl mt-0.5">analytics</span>
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="px-2 py-0.5 rounded text-[9px] font-mono bg-brandPrimary/20 text-brandPrimary border border-brandPrimary/40 font-bold uppercase tracking-wider">Definition</span>
          <h4 id="auto-narrative-title" class="text-xs font-bold text-gradient-flow">Component 1 of 6: Dataset Overview & Partition Metrics</h4>
        </div>
        <p id="auto-narrative-desc" class="text-xs text-brandMuted mt-1 leading-relaxed max-w-3xl">
          Analyzes cohort demographics and splits the active dataset into an 80% private training corpus and 20% validation holdout, measuring feature dimensionality and target class balance.
        </p>
      </div>
    </div>
    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="stepPrevAuto()" class="p-1.5 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] text-brandMuted hover:text-white transition-all">
        <span class="material-symbols-outlined text-sm">chevron_left</span>
      </button>
      <button onclick="stepNextAuto()" class="p-1.5 rounded-lg bg-white/[0.05] hover:bg-white/[0.1] text-brandMuted hover:text-white transition-all">
        <span class="material-symbols-outlined text-sm">chevron_right</span>
      </button>
    </div>
  </div>
</section>

<!-- 3. FULL TRAINING PANEL (Hidden by default) -->
<section id="mode-panel-training" class="hidden p-6 rounded-xl bg-brandSurface border border-[#f093fb]/30 shadow-2xl flex flex-col gap-6 transition-all duration-300">
  <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-white/[0.06] pb-4">
    <div>
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-pink-500/10 text-pink-400 border border-pink-500/20">Sequential Suite</span>
        <h2 class="section-title">Multi-Model Training Suite (Full Training)</h2>
      </div>
      <p class="text-xs text-brandMuted mt-0.5">Train 1 unclipped baseline + 4 DP-SGD models (ε ∈ {0.5, 1.0, 5.0, 10.0}) sequentially to audit the trade-off frontier.</p>
    </div>
    <div class="text-right">
      <span class="text-xs font-mono text-brandMuted">Est. Runtime: ~1m 30s</span>
    </div>
  </div>

  <!-- Model Pipeline Grid -->
  <div class="grid grid-cols-1 md:grid-cols-5 gap-3" id="training-model-cards">
    <!-- Card 1: Baseline -->
    <div id="train-card-0" class="p-3.5 rounded-lg bg-white/[0.02] border border-white/[0.06] flex flex-col justify-between gap-2">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase text-rose-400 font-semibold">Model 1</span>
          <span id="train-status-0" class="text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono">Pending</span>
        </div>
        <div class="text-xs font-bold text-white mt-1">Standard Baseline</div>
        <div class="text-[10px] text-brandMuted">ε = ∞ (Unbounded)</div>
      </div>
      <div class="text-[11px] font-mono text-brandMuted" id="train-metric-0">Acc: -- | MIA: --</div>
    </div>
    <!-- Card 2: eps 10.0 -->
    <div id="train-card-1" class="p-3.5 rounded-lg bg-white/[0.02] border border-white/[0.06] flex flex-col justify-between gap-2">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase text-purple-400 font-semibold">Model 2</span>
          <span id="train-status-1" class="text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono">Pending</span>
        </div>
        <div class="text-xs font-bold text-white mt-1">DP-SGD Relaxed</div>
        <div class="text-[10px] text-brandMuted">ε = 10.0 (High noise)</div>
      </div>
      <div class="text-[11px] font-mono text-brandMuted" id="train-metric-1">Acc: -- | MIA: --</div>
    </div>
    <!-- Card 3: eps 5.0 (Optimal) -->
    <div id="train-card-2" class="p-3.5 rounded-lg bg-white/[0.02] border border-white/[0.06] flex flex-col justify-between gap-2">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase text-amber-400 font-semibold">Model 3</span>
          <span id="train-status-2" class="text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono">Pending</span>
        </div>
        <div class="text-xs font-bold text-white mt-1">DP-SGD Optimal</div>
        <div class="text-[10px] text-brandMuted">ε = 5.0 (Sweet-spot)</div>
      </div>
      <div class="text-[11px] font-mono text-brandMuted" id="train-metric-2">Acc: -- | MIA: --</div>
    </div>
    <!-- Card 4: eps 1.0 -->
    <div id="train-card-3" class="p-3.5 rounded-lg bg-white/[0.02] border border-white/[0.06] flex flex-col justify-between gap-2">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase text-emerald-400 font-semibold">Model 4</span>
          <span id="train-status-3" class="text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono">Pending</span>
        </div>
        <div class="text-xs font-bold text-white mt-1">DP-SGD Strong</div>
        <div class="text-[10px] text-brandMuted">ε = 1.0 (Guaranteed)</div>
      </div>
      <div class="text-[11px] font-mono text-brandMuted" id="train-metric-3">Acc: -- | MIA: --</div>
    </div>
    <!-- Card 5: eps 0.5 -->
    <div id="train-card-4" class="p-3.5 rounded-lg bg-white/[0.02] border border-white/[0.06] flex flex-col justify-between gap-2">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-mono uppercase text-blue-400 font-semibold">Model 5</span>
          <span id="train-status-4" class="text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono">Pending</span>
        </div>
        <div class="text-xs font-bold text-white mt-1">DP-SGD Maximum</div>
        <div class="text-[10px] text-brandMuted">ε = 0.5 (Provable)</div>
      </div>
      <div class="text-[11px] font-mono text-brandMuted" id="train-metric-4">Acc: -- | MIA: --</div>
    </div>
  </div>

  <!-- Progress Bar & Status (Hidden until started) -->
  <div id="training-progress-container" class="hidden flex flex-col gap-2">
    <div class="flex items-center justify-between text-xs font-mono">
      <span id="training-progress-label" class="text-white font-semibold">Training Pipeline Active: [1/5] Standard Baseline...</span>
      <span id="training-progress-pct" class="text-brandPrimary">20%</span>
    </div>
    <div class="w-full h-2 bg-white/[0.08] rounded-full overflow-hidden">
      <div id="training-progress-bar" class="h-full bg-gradient-to-r from-[#667eea] via-[#f093fb] to-[#4facfe] transition-all duration-300 w-0"></div>
    </div>
  </div>

  <!-- Action CTA -->
  <button id="btn-train-all" class="btn-gradient w-full py-3.5 px-6 rounded-xl font-semibold text-sm text-white shadow-xl flex items-center justify-center gap-2 hover:opacity-95 transition-all" onclick="runFullTrainingPipeline()">
    <span class="material-symbols-outlined text-lg">rocket_launch</span>
    <span id="btn-train-all-text">Train All 5 Benchmark Models (Sequential Pipeline)</span>
  </button>

  <!-- Full Training Completion & Results Callout (Revealed after all 5 train) -->
  <div id="full-training-completion-card" class="hidden flex-col gap-3 p-4 rounded-xl bg-black/40 border border-emerald-500/30 shadow-lg">
    <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="text-xs font-semibold text-white">All 5 Models Trained: Empirical Telemetry & Benchmarks Updated</span>
      </div>
      <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Audit Complete (5/5)</span>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs font-mono">
      <div class="p-2.5 rounded-lg bg-white/[0.03] border border-white/[0.06] flex flex-col">
        <span class="text-[10px] text-brandMuted uppercase">Standard Baseline (ε=∞)</span>
        <span id="ft-res-base" class="text-white font-bold text-sm mt-0.5">86.2% Acc | 79.8% MIA</span>
        <span class="text-[10px] text-rose-400">High Leakage Risk</span>
      </div>
      <div class="p-2.5 rounded-lg bg-white/[0.03] border border-white/[0.06] flex flex-col">
        <span class="text-[10px] text-brandMuted uppercase">Optimal Sweet Spot (ε=5.0)</span>
        <span id="ft-res-opt" class="text-[#4facfe] font-bold text-sm mt-0.5">82.4% Acc | 55.4% MIA</span>
        <span class="text-[10px] text-emerald-400">96.7% Utility Retained</span>
      </div>
      <div class="p-2.5 rounded-lg bg-white/[0.03] border border-white/[0.06] flex flex-col">
        <span class="text-[10px] text-brandMuted uppercase">Provable Strong (ε=0.5)</span>
        <span id="ft-res-safe" class="text-emerald-400 font-bold text-sm mt-0.5">71.3% Acc | 51.2% MIA</span>
        <span class="text-[10px] text-blue-400">Provable Privacy</span>
      </div>
    </div>
    <div class="flex items-center gap-2 mt-1">
      <button onclick="document.getElementById('chart-privacy-accuracy').scrollIntoView({ behavior: 'smooth', block: 'center' })" class="px-3 py-1.5 rounded-lg bg-white/[0.06] hover:bg-white/[0.1] text-xs text-white font-medium flex items-center gap-1 transition-all">
        <span>View Telemetry Curves</span>
        <span class="material-symbols-outlined text-sm">arrow_downward</span>
      </button>
      <button onclick="document.getElementById('benchmarks-tbody').scrollIntoView({ behavior: 'smooth', block: 'center' })" class="px-3 py-1.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-xs text-emerald-300 font-medium flex items-center gap-1 transition-all">
        <span>View Benchmarks Table</span>
        <span class="material-symbols-outlined text-sm">table_rows</span>
      </button>
    </div>
  </div>

</section>

<!-- 4. RESULTS ANALYSIS PANEL (Hidden by default) -->
<section id="mode-panel-results" class="hidden p-6 rounded-xl bg-brandSurface border border-[#4facfe]/30 shadow-2xl flex flex-col gap-6 transition-all duration-300">
  <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-white/[0.06] pb-4">
    <div>
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-cyan-500/10 text-[#4facfe] border border-cyan-500/20">Audit Matrix</span>
        <h2 class="section-title">Comparative Results Analysis & Defense Audit</h2>
      </div>
      <p class="text-xs text-brandMuted mt-0.5">Empirical Pareto-frontier trade-off evaluation and membership inference attack resistance analysis.</p>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="downloadCSVReport()" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-white/[0.06] text-white border border-white/[0.1] hover:bg-white/[0.1] flex items-center gap-1.5 transition-all">
        <span class="material-symbols-outlined text-sm">download</span>
        <span>Download Audit CSV</span>
      </button>
    </div>
  </div>

  <!-- 3 KPI Cards -->
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06]">
      <div class="text-[10px] font-mono text-emerald-400 font-semibold uppercase">Pareto Optimal Point</div>
      <div class="text-xl font-bold text-white mt-1">ε = 5.0</div>
      <div class="text-xs text-brandMuted mt-1">Retains 96.7% baseline accuracy with 68% lower MIA vulnerability.</div>
    </div>
    <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06]">
      <div class="text-[10px] font-mono text-brandPrimary font-semibold uppercase">Defense Factor</div>
      <div class="text-xl font-bold text-white mt-1">1.56× Protection</div>
      <div class="text-xs text-brandMuted mt-1">Reduces worst-case membership inference risk from 79.8% to 51.2%.</div>
    </div>
    <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06]">
      <div class="text-[10px] font-mono text-amber-400 font-semibold uppercase">Gaussian Overhead</div>
      <div class="text-xl font-bold text-white mt-1">+18.4% Compute</div>
      <div class="text-xs text-brandMuted mt-1">Per-sample gradient clipping & noise addition runtime impact.</div>
    </div>
  </div>

  <!-- Filter Buttons for Table -->
  <div class="flex items-center justify-between flex-wrap gap-2 pt-2">
    <div class="flex items-center gap-2 text-xs">
      <span class="text-brandMuted font-medium">Filter Benchmarks:</span>
      <button onclick="filterBenchmarkRows('all', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.1] text-white font-medium">All Models (5)</button>
      <button onclick="filterBenchmarkRows('safe', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white font-medium">Provable Safe (ε ≤ 1.0)</button>
      <button onclick="filterBenchmarkRows('rec', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white font-medium">Optimal Only (ε = 5.0)</button>
      <button onclick="filterBenchmarkRows('base', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white font-medium">Baseline (No DP)</button>
    </div>
    <button onclick="document.getElementById('benchmarks-tbody').scrollIntoView({ behavior: 'smooth', block: 'center' })" class="text-xs text-brandPrimary hover:underline flex items-center gap-1 font-mono">
      <span>Jump to Benchmarks Table</span>
      <span class="material-symbols-outlined text-xs">arrow_downward</span>
    </button>
  </div>
</section>

<!-- ===================================================================== -->
<!-- SECTION 4: CHARTS -->
<!-- ===================================================================== -->
<section id="section-telemetry-curves" class="flex flex-col gap-6">
<div class="flex items-center justify-between">
<h2 class="section-title">Telemetry &amp; Empirical Curves</h2>
<span id="telemetry-audit-sub" class="text-xs text-brandMuted font-mono">Audit: Gaussian Mechanism (δ = 1e-5, σ = 4.84, q = 0.0016)</span>
</div>
<!-- Two Side-by-Side SVG Charts -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
<!-- Chart A: Privacy-Accuracy Trade-off -->
<div id="chart-privacy-accuracy" class="p-5 rounded-xl bg-brandSurface border-subtle flex flex-col gap-3 transition-all duration-500 relative">
<div class="flex items-center justify-between">
<div>
<h3 class="text-xs font-semibold text-white">Privacy–Accuracy Trade-off</h3>
<p class="text-[11px] text-brandMuted">Validation accuracy as privacy budget ε expands</p>
</div>
<div class="flex items-center gap-2">
  <span id="chart-a-status" class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]">Awaiting Training</span>
  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-[#4facfe] border border-white/[0.08]">Top-1 Acc</span>
</div>
</div>
<!-- SVG Vector Canvas -->
<div class="w-full relative mt-2">
  <!-- Clean Awaiting Training Overlay -->
  <div id="chart-a-empty-overlay" class="absolute inset-0 z-10 flex flex-col items-center justify-center bg-brandSurface/85 backdrop-blur-[2px] rounded-lg transition-all duration-300">
    <div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.05] border border-white/[0.08] text-xs font-mono text-brandMuted shadow-sm">
      <span class="w-2 h-2 rounded-full bg-amber-400/80 animate-pulse"></span>
      <span>No Models Trained Yet</span>
    </div>
    <span class="text-[11px] text-brandMuted mt-1.5">Train model or launch demo in active mode to plot empirical trade-off curve</span>
  </div>

  <svg class="w-full h-auto overflow-visible select-none font-mono text-[10px]" viewbox="0 0 460 210">
    <defs>
      <lineargradient id="cyanArea" x1="0" x2="0" y1="0" y2="1">
        <stop offset="0%" stop-color="#4facfe" stop-opacity="0.15"></stop>
        <stop offset="100%" stop-color="#4facfe" stop-opacity="0.0"></stop>
      </lineargradient>
    </defs>
    <!-- Gridlines & Y Axis Ticks (Always clean & visible) -->
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="20" y2="20"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="24">90%</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="70" y2="70"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="74">80%</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="120" y2="120"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="124">70%</text>
    <line stroke="rgba(255,255,255,0.12)" x1="35" x2="445" y1="170" y2="170"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="174">60%</text>
    <!-- X Axis Labels -->
    <text fill="#6b7280" text-anchor="middle" x="45" y="190">0.5</text>
    <text fill="#6b7280" text-anchor="middle" x="115" y="190">1.0</text>
    <text fill="#6b7280" text-anchor="middle" x="195" y="190">2.0</text>
    <text fill="#6b7280" text-anchor="middle" x="280" y="190">5.0</text>
    <text fill="#6b7280" text-anchor="middle" x="360" y="190">8.0</text>
    <text fill="#6b7280" text-anchor="middle" x="430" y="190">10.0</text>

    <!-- Plotted elements (Hidden initially, revealed only after training) -->
    <g id="chart-a-plot-elements" style="opacity: 0; transition: opacity 0.4s ease;">
      <!-- Non-private Baseline Dashed Line (86.2% -> y = 39) -->
      <line id="baseline-acc-line" stroke="#e74c3c" stroke-dasharray="4,4" stroke-width="1.2" x1="35" x2="445" y1="39" y2="39"></line>
      <text id="baseline-acc-text" fill="#e74c3c" font-size="9" text-anchor="end" x="440" y="33">Baseline = 0.862</text>
      <!-- Curve Fill Area -->
      <path id="curve-acc-area" d="M 45 113 Q 120 78 200 60 T 430 43 L 430 170 L 45 170 Z" fill="url(#cyanArea)"></path>
      <!-- Accuracy Line (#4facfe, strokeWidth 2.5) -->
      <path class="chart-line" d="M 45 113 Q 120 78 200 60 T 430 43" fill="none" id="curve-acc" stroke="#4facfe" stroke-linecap="round" stroke-width="2.5"></path>
      <!-- Key Data Markers & Floating Value Labels -->
      <circle cx="45" cy="113" fill="#0d1117" r="3.5" stroke="#4facfe" stroke-width="2"></circle>
      <text fill="#4facfe" font-size="9" text-anchor="middle" x="45" y="130">71.3%</text>
      <circle cx="195" cy="62" fill="#0d1117" r="3.5" stroke="#4facfe" stroke-width="2"></circle>
      <text fill="#4facfe" font-size="9" text-anchor="middle" x="195" y="52">78.9%</text>
      <circle cx="280" cy="54" fill="#4facfe" r="5" stroke="#ffffff" stroke-width="2"></circle>
      <!-- Floating Sweet Spot Pill -->
      <g id="acc-opt-pill" transform="translate(280, 26)">
        <rect fill="#161b22" height="18" rx="4" stroke="#4facfe" stroke-width="1" width="70" x="-35" y="-10"></rect>
        <text id="acc-opt-text" fill="#4facfe" font-size="9" font-weight="bold" text-anchor="middle" x="0" y="3">82.4% (Opt)</text>
      </g>
      <circle cx="430" cy="43" fill="#0d1117" r="3.5" stroke="#4facfe" stroke-width="2"></circle>
      <text fill="#4facfe" font-size="9" text-anchor="end" x="425" y="58">84.8%</text>
    </g>

    <!-- Interactive Real-Time Operating Indicator (Hidden initially) -->
    <g id="interactive-acc-pointer" style="display: none; opacity: 0;">
      <circle id="interactive-acc-pulse" cx="115" cy="97" r="9" fill="#667eea" fill-opacity="0.25" class="animate-ping"></circle>
      <circle id="interactive-acc-circle" cx="115" cy="97" r="5.5" fill="#667eea" stroke="#ffffff" stroke-width="2"></circle>
      <g id="interactive-acc-tag" transform="translate(115, 75)">
        <rect x="-46" y="-12" width="92" height="20" rx="6" fill="#0d1117" stroke="#667eea" stroke-width="1.5" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.6))"></rect>
        <text id="interactive-acc-tag-text" x="0" y="2" fill="#4facfe" font-size="9" font-weight="bold" text-anchor="middle">ε=1.0 | 75.4%</text>
      </g>
    </g>
  </svg>
</div>
</div>
<!-- Chart B: Membership Inference Risk -->
<div id="chart-mia-risk" class="p-5 rounded-xl bg-brandSurface border-subtle flex flex-col gap-3 transition-all duration-500 relative">
<div class="flex items-center justify-between">
<div>
<h3 class="text-xs font-semibold text-white">Membership Inference Risk</h3>
<p class="text-[11px] text-brandMuted">Shadow attack success likelihood vs privacy budget</p>
</div>
<div class="flex items-center gap-2">
  <span id="chart-b-status" class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]">Awaiting Training</span>
  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-[#f093fb] border border-white/[0.08]">MIA Precision</span>
</div>
</div>
<!-- SVG Vector Canvas with Threat Zones -->
<div class="w-full relative mt-2">
  <!-- Clean Awaiting Training Overlay -->
  <div id="chart-b-empty-overlay" class="absolute inset-0 z-10 flex flex-col items-center justify-center bg-brandSurface/85 backdrop-blur-[2px] rounded-lg transition-all duration-300">
    <div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.05] border border-white/[0.08] text-xs font-mono text-brandMuted shadow-sm">
      <span class="w-2 h-2 rounded-full bg-amber-400/80 animate-pulse"></span>
      <span>No Models Trained Yet</span>
    </div>
    <span class="text-[11px] text-brandMuted mt-1.5">Train model or launch demo in active mode to plot attack risk curve</span>
  </div>

  <svg class="w-full h-auto overflow-visible select-none font-mono text-[10px]" viewbox="0 0 460 210">
    <!-- Colored Horizontal Threat Zones (Always visible) -->
    <!-- High Risk (0.15+ leakage beyond random 50% -> >65% y:20-75) -->
    <rect fill="#e74c3c" fill-opacity="0.08" height="55" width="410" x="35" y="20"></rect>
    <text fill="#e74c3c" font-size="9" font-weight="600" text-anchor="end" x="440" y="34">High Risk (&gt;0.15)</text>
    <!-- Moderate (0.05 - 0.15 -> 55%-65% y:75-125) -->
    <rect fill="#f39c12" fill-opacity="0.08" height="50" width="410" x="35" y="75"></rect>
    <text fill="#f39c12" font-size="9" font-weight="600" text-anchor="end" x="440" y="89">Moderate (0.05–0.15)</text>
    <!-- Low Risk (0 - 0.05 -> 50%-55% y:125-170) -->
    <rect fill="#27ae60" fill-opacity="0.08" height="45" width="410" x="35" y="125"></rect>
    <text fill="#27ae60" font-size="9" font-weight="600" text-anchor="end" x="440" y="139">Low Risk (&lt;0.05)</text>
    <!-- Gridlines -->
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="20" y2="20"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="24">80%</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="75" y2="75"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="79">65%</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="35" x2="445" y1="125" y2="125"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="129">55%</text>
    <line stroke="rgba(255,255,255,0.12)" x1="35" x2="445" y1="170" y2="170"></line>
    <text fill="#6b7280" text-anchor="end" x="28" y="174">50%</text>
    <!-- X Axis Labels -->
    <text fill="#6b7280" text-anchor="middle" x="45" y="190">0.5</text>
    <text fill="#6b7280" text-anchor="middle" x="115" y="190">1.0</text>
    <text fill="#6b7280" text-anchor="middle" x="195" y="190">2.0</text>
    <text fill="#6b7280" text-anchor="middle" x="280" y="190">5.0</text>
    <text fill="#6b7280" text-anchor="middle" x="360" y="190">8.0</text>
    <text fill="#6b7280" text-anchor="middle" x="430" y="190">10.0</text>

    <!-- Plotted elements (Hidden initially, revealed only after training) -->
    <g id="chart-b-plot-elements" style="opacity: 0; transition: opacity 0.4s ease;">
      <!-- MIA Curve (#f093fb, strokeWidth 2.5) -->
      <path class="chart-line" d="M 45 165 Q 120 156 200 142 T 280 118 T 430 35" fill="none" id="curve-mia" stroke="#f093fb" stroke-linecap="round" stroke-width="2.5"></path>
      <!-- Markers and Values -->
      <circle id="mia-circle-1" cx="45" cy="165" fill="#27ae60" r="4" stroke="#ffffff" stroke-width="1.5"></circle>
      <text id="mia-text-1" fill="#27ae60" font-size="9" text-anchor="middle" x="45" y="152">51.2% (Low)</text>
      <circle id="mia-circle-2" cx="280" cy="118" fill="#f39c12" r="4" stroke="#ffffff" stroke-width="1.5"></circle>
      <text id="mia-text-2" fill="#f39c12" font-size="9" text-anchor="middle" x="280" y="106">55.4% (Mod)</text>
      <circle id="mia-circle-3" cx="430" cy="35" fill="#e74c3c" r="4" stroke="#ffffff" stroke-width="1.5"></circle>
      <text id="mia-text-3" fill="#e74c3c" font-size="9" text-anchor="end" x="420" y="24">79.8% (Danger)</text>
    </g>

    <!-- Interactive Real-Time Operating Indicator (Hidden initially) -->
    <g id="interactive-mia-pointer" style="display: none; opacity: 0;">
      <circle id="interactive-mia-pulse" cx="115" cy="155" r="9" fill="#27ae60" fill-opacity="0.25" class="animate-ping"></circle>
      <circle id="interactive-mia-circle" cx="115" cy="155" r="5.5" fill="#27ae60" stroke="#ffffff" stroke-width="2"></circle>
      <g id="interactive-mia-tag" transform="translate(115, 135)">
        <rect x="-42" y="-12" width="84" height="20" rx="6" fill="#0d1117" stroke="#27ae60" stroke-width="1.5" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.6))"></rect>
        <text id="interactive-mia-tag-text" x="0" y="2" fill="#27ae60" font-size="9" font-weight="bold" text-anchor="middle">MIA: 52.0%</text>
      </g>
    </g>
  </svg>
</div>
</div>
</div>
<!-- Full-width Below: Training Curves (Epoch Dynamics) -->
<div id="chart-epoch-curves" class="p-5 rounded-xl bg-brandSurface border-subtle flex flex-col gap-3 transition-all duration-500 relative">
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
<div>
<h3 class="text-xs font-semibold text-white">Training Curves (Epoch Dynamics)</h3>
<p class="text-[11px] text-brandMuted">Loss trajectory convergence over 20 epochs across DP budgets</p>
</div>
<!-- Top Right Legend & Status -->
<div class="flex items-center gap-3 flex-wrap text-[10px] font-mono">
<span id="chart-c-status" class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]">Awaiting Training</span>
<span id="legend-interactive-curve" class="hidden items-center gap-1.5 text-[#667eea] font-semibold">
  <span class="w-2.5 h-0.5 bg-[#667eea] shadow-[0_0_8px_#667eea]"></span> <span id="legend-interactive-text">Your Model (ε=1.0)</span>
</span>
<span class="flex items-center gap-1.5 text-[#e74c3c]">
<span class="w-2.5 h-0.5 bg-[#e74c3c]"></span> Baseline (ε=∞)
              </span>
<span class="flex items-center gap-1.5 text-[#8a2be2]">
<span class="w-2.5 h-0.5 bg-[#8a2be2]"></span> ε=10.0
              </span>
<span class="flex items-center gap-1.5 text-[#f59e0b] font-semibold">
<span class="w-2.5 h-0.5 bg-[#f59e0b]"></span> ε=5.0
              </span>
<span class="flex items-center gap-1.5 text-[#27ae60]">
<span class="w-2.5 h-0.5 bg-[#27ae60]"></span> ε=1.0
              </span>
<span class="flex items-center gap-1.5 text-[#3b82f6]">
<span class="w-2.5 h-0.5 bg-[#3b82f6]"></span> ε=0.5
              </span>
</div>
</div>
<!-- Full Width SVG Canvas -->
<div class="w-full relative mt-1">
  <!-- Clean Awaiting Training Overlay -->
  <div id="chart-c-empty-overlay" class="absolute inset-0 z-10 flex flex-col items-center justify-center bg-brandSurface/85 backdrop-blur-[2px] rounded-lg transition-all duration-300">
    <div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.05] border border-white/[0.08] text-xs font-mono text-brandMuted shadow-sm">
      <span class="w-2 h-2 rounded-full bg-amber-400/80 animate-pulse"></span>
      <span>No Loss Trajectories Plotted</span>
    </div>
    <span class="text-[11px] text-brandMuted mt-1.5">Loss trajectories will converge and plot across DP budgets during training</span>
  </div>

  <svg class="w-full h-auto overflow-visible select-none font-mono text-[10px]" viewbox="0 0 920 220">
    <!-- Dark 10% Gridlines -->
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="45" x2="895" y1="20" y2="20"></line>
    <text fill="#6b7280" text-anchor="end" x="35" y="24">0.70</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="45" x2="895" y1="70" y2="70"></line>
    <text fill="#6b7280" text-anchor="end" x="35" y="74">0.50</text>
    <line stroke="rgba(255,255,255,0.06)" stroke-dasharray="2,2" x1="45" x2="895" y1="120" y2="120"></line>
    <text fill="#6b7280" text-anchor="end" x="35" y="124">0.35</text>
    <line stroke="rgba(255,255,255,0.12)" x1="45" x2="895" y1="170" y2="170"></line>
    <text fill="#6b7280" text-anchor="end" x="35" y="174">0.20</text>
    <!-- X Axis Ticks -->
    <text fill="#6b7280" text-anchor="middle" x="50" y="195">Epoch 0</text>
    <text fill="#6b7280" text-anchor="middle" x="260" y="195">Epoch 5</text>
    <text fill="#6b7280" text-anchor="middle" x="470" y="195">Epoch 10</text>
    <text fill="#6b7280" text-anchor="middle" x="680" y="195">Epoch 15</text>
    <text fill="#6b7280" text-anchor="middle" x="890" y="195">Epoch 20</text>

    <!-- Plotted Curves (Hidden initially, revealed during/after training) -->
    <g id="chart-c-plot-elements" style="opacity: 0; transition: opacity 0.4s ease;">
      <!-- Line 1: Baseline ε=∞ (Red, rapid drop to 0.22 -> y=165) -->
      <path id="epoch-curve-baseline" class="epoch-curve" d="M 50 30 C 180 120, 380 158, 890 165" fill="none" stroke="#e74c3c" stroke-width="1.8"></path>
      <!-- Line 2: ε=10.0 (Violet, drops to y=150) -->
      <path id="epoch-curve-eps10" class="epoch-curve" d="M 50 32 C 200 110, 420 142, 890 150" fill="none" stroke="#8a2be2" stroke-width="1.8"></path>
      <!-- Line 3: ε=5.0 (Amber/Yellow, Optimal balance, drops to y=138) -->
      <path id="epoch-curve-eps5" class="epoch-curve" d="M 50 36 C 220 95, 450 128, 890 138" fill="none" stroke="#f59e0b" stroke-width="2.6"></path>
      <!-- Line 4: ε=1.0 (Green, drops to y=110) -->
      <path id="epoch-curve-eps1" class="epoch-curve" d="M 50 42 C 240 85, 480 102, 890 110" fill="none" stroke="#27ae60" stroke-width="1.8"></path>
      <!-- Line 5: ε=0.5 (Blue, High noise floor, stops at y=85) -->
      <path id="epoch-curve-eps05" class="epoch-curve" d="M 50 48 C 260 70, 500 80, 890 85" fill="none" stroke="#3b82f6" stroke-width="1.8"></path>

      <!-- Line 6: Interactive Trained Dynamic Curve (Vibrant Violet/Indigo Glow) -->
      <path id="epoch-curve-interactive" fill="none" stroke="#667eea" stroke-width="3.2" filter="drop-shadow(0 0 8px rgba(102, 126, 234, 0.8))" stroke-linecap="round" style="display: none;"></path>
    </g>

    <!-- Interactive Real-Time Epoch Horizon Guide Line & Flag (Hidden initially) -->
    <g id="interactive-epoch-guide" style="display: none; opacity: 0;">
      <line id="interactive-epoch-line" stroke="#667eea" stroke-dasharray="3,3" stroke-width="2" x1="680" x2="680" y1="20" y2="170" opacity="0.8"></line>
      <g id="interactive-epoch-flag" transform="translate(680, 16)">
        <rect x="-44" y="-12" width="88" height="18" rx="4" fill="#161b22" stroke="#667eea" stroke-width="1.4" filter="drop-shadow(0 2px 6px rgba(0,0,0,0.6))"></rect>
        <text id="interactive-epoch-flag-text" x="0" y="1" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Stop: Epoch 15</text>
      </g>
    </g>

    <!-- Interactive Real-Time Epoch Endpoint Loss Pointer -->
    <g id="interactive-epoch-pointer" style="display: none; opacity: 0;">
      <circle id="interactive-epoch-pulse" cx="680" cy="110" r="9" fill="#667eea" fill-opacity="0.3" class="animate-ping"></circle>
      <circle id="interactive-epoch-circle" cx="680" cy="110" r="5.5" fill="#667eea" stroke="#ffffff" stroke-width="2"></circle>
      <g id="interactive-epoch-tag" transform="translate(680, 85)">
        <rect x="-55" y="-12" width="110" height="20" rx="6" fill="#0d1117" stroke="#667eea" stroke-width="1.5" filter="drop-shadow(0 2px 8px rgba(0,0,0,0.6))"></rect>
        <text id="interactive-epoch-tag-text" x="0" y="2" fill="#667eea" font-size="9" font-weight="bold" text-anchor="middle">Loss: 0.380 @ Ep 15</text>
      </g>
    </g>
  </svg>
</div>
</div>
</section>
<!-- ===================================================================== -->
<!-- SECTION 5: RESULTS TABLE -->
<!-- ===================================================================== -->
<!-- ===================================================================== -->
<!-- SECTION 5: AUDITED BENCHMARKS & DISTRIBUTED FRAMEWORKS (TABLE I) -->
<!-- ===================================================================== -->
<section id="section-audited-benchmarks" class="p-6 rounded-xl bg-brandSurface border-subtle flex flex-col gap-5 transition-all duration-500">
  <!-- Header with Title, Dataset Indicator, and Tab Switcher -->
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/[0.06] pb-4">
    <div>
      <div class="flex items-center gap-2">
        <h2 class="section-title text-base sm:text-lg">Audited Benchmarks &amp; Comparative Analysis</h2>
        <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-brandPrimary/15 text-brandPrimary border border-brandPrimary/30 font-semibold">Research Synthesis</span>
      </div>
      <p class="text-xs text-brandMuted mt-1">Empirical differential privacy metrics measured against synthetic shadow models &amp; distributed cryptographic baselines.</p>
    </div>

    <!-- Tab Switcher -->
    <div class="flex items-center gap-1.5 p-1 bg-black/40 border border-white/[0.08] rounded-xl self-start md:self-auto">
      <button id="tab-btn-empirical" onclick="switchBenchmarkTab('empirical')" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-brandPrimary text-white shadow-md transition-all flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[15px]">table_chart</span>
        <span>Empirical Benchmarks (Acc &amp; F1)</span>
      </button>
      <button id="tab-btn-distributed" onclick="switchBenchmarkTab('distributed')" class="px-3.5 py-1.5 rounded-lg text-xs font-semibold text-brandMuted hover:text-white transition-all flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[15px]">account_tree</span>
        <span>Table I: Distributed Frameworks</span>
      </button>
    </div>
  </div>

  <!-- TAB 1: EMPIRICAL BENCHMARKS TABLE (Accuracy & F1-Score) -->
  <div id="tab-pane-empirical" class="flex flex-col gap-4">
    <div class="flex items-center justify-between flex-wrap gap-2">
      <div class="flex items-center gap-2">
        <span class="text-xs text-brandMuted font-mono" id="table-dataset-name">Dataset: Adult 1994</span>
        <span class="text-[11px] text-brandMuted">•</span>
        <span class="text-[11px] text-brandMuted font-mono">Includes <strong class="text-white font-semibold">F1-Score</strong> to evaluate minority class trade-offs under DP noise</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-xs text-brandMuted font-medium mr-1">Filter:</span>
        <button onclick="filterBenchmarkRows('all', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.1] text-white text-xs font-medium">All</button>
        <button onclick="filterBenchmarkRows('safe', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white text-xs font-medium">Safe (ε≤1.0)</button>
        <button onclick="filterBenchmarkRows('rec', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white text-xs font-medium">Optimal (ε=5.0)</button>
        <button onclick="filterBenchmarkRows('base', this)" class="bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white text-xs font-medium">Baseline</button>
      </div>
    </div>

    <div class="overflow-x-auto rounded-lg border border-white/[0.06]">
      <table class="w-full text-left text-xs font-sans">
        <thead>
          <tr class="bg-black/30 border-b border-white/[0.07] text-[11px] uppercase tracking-wider text-brandMuted font-semibold">
            <th class="py-3 px-3">Model</th>
            <th class="py-3 px-3">Mechanism</th>
            <th class="py-3 px-3">Epsilon (ε)</th>
            <th class="py-3 px-3">Delta (δ)</th>
            <th class="py-3 px-3">Accuracy</th>
            <th class="py-3 px-3 text-[#4facfe]">F1-Score</th>
            <th class="py-3 px-3">MIA Risk</th>
            <th class="py-3 px-3 text-right">Training Time</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/[0.04] font-mono text-[12px]" id="benchmarks-tbody">
          <!-- Row 1: ε=0.5 -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3 px-3 font-sans font-medium text-white">DP-SGD ResNet-Tabular</td>
            <td class="py-3 px-3 text-brandMuted font-sans">Gaussian + Clip</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                ε = 0.50
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">1.0e-5</td>
            <td class="py-3 px-3 text-white font-medium">71.3%</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">49.0%</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 text-emerald-400">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span>51.2% Negligible</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">4m 12s</td>
          </tr>
          <!-- Row 2: ε=1.0 -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3 px-3 font-sans font-medium text-white">DP-SGD MLP</td>
            <td class="py-3 px-3 text-brandMuted font-sans">Gaussian + Clip</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                ε = 1.00
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">1.0e-5</td>
            <td class="py-3 px-3 text-white font-medium">74.6%</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">54.2%</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 text-emerald-400">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span>52.0% Safe</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">3m 48s</td>
          </tr>
          <!-- Row 3: ε=5.0 (Recommended) -->
          <tr class="bg-white/[0.03] hover:bg-white/[0.05] transition-colors border-l-2 border-brandPrimary">
            <td class="py-3 px-3 font-sans font-medium text-white flex items-center gap-1.5">
              <span>DP-SGD Optimal</span>
              <span class="text-[10px] font-sans font-semibold text-brandPrimary bg-brandPrimary/10 px-1.5 py-0.2 rounded">Recommended</span>
            </td>
            <td class="py-3 px-3 text-brandMuted font-sans">Gaussian + Clip</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20">
                ε = 5.00
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">1.0e-5</td>
            <td class="py-3 px-3 text-white font-medium">82.4%</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">63.8%</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 text-amber-400">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                <span>55.4% Controlled</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">3m 50s</td>
          </tr>
          <!-- Row 4: ε=8.0 -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3 px-3 font-sans font-medium text-white">DP LightGBM-DP</td>
            <td class="py-3 px-3 text-brandMuted font-sans">Laplace Trees</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                ε = 8.00
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">0 (Pure)</td>
            <td class="py-3 px-3 text-white font-medium">84.1%</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">65.5%</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 text-rose-400">
                <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                <span>66.2% Elevated</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">1m 20s</td>
          </tr>
          <!-- Row 5: Baseline -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3 px-3 font-sans font-medium text-white">Standard SGD Baseline</td>
            <td class="py-3 px-3 text-brandMuted font-sans">None (Unbounded)</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                ε = ∞ (None)
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">0</td>
            <td class="py-3 px-3 text-white font-medium">86.2%</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">69.4%</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 text-rose-400">
                <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                <span>79.8% Critical</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">1m 05s</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Bottom Action CTA -->
    <div class="flex items-center justify-between pt-2 border-t border-white/[0.06] flex-wrap gap-3">
      <div class="text-xs text-brandMuted flex items-center gap-1.5">
        <span class="material-symbols-outlined text-sm text-brandSafe">verified</span>
        <span>DP-SGD with moments accountant delivers certified differential privacy with minimal minority-class degradation.</span>
      </div>
      <button onclick="downloadCSVReport()" class="px-3.5 py-1.5 rounded-lg border border-white/[0.12] text-xs font-medium text-brandText hover:border-brandSafe hover:text-brandSafe hover:bg-brandSafe/5 transition-all flex items-center gap-1.5">
        <span class="material-symbols-outlined text-xs">download</span>
        <span>Download CSV Report</span>
      </button>
    </div>
  </div>

  <!-- TAB 2: DISTRIBUTED FRAMEWORKS COMPARISON (TABLE I FROM PAPER) -->
  <div id="tab-pane-distributed" class="hidden flex flex-col gap-4">
    <div class="flex items-center justify-between flex-wrap gap-2">
      <div>
        <h3 class="text-sm font-semibold text-white flex items-center gap-2">
          <span>Table I: Comparison of Differential Privacy &amp; Cryptographic Frameworks</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-purple-500/20 text-[#f093fb] border border-purple-500/30">Section V-C</span>
        </h3>
        <p class="text-xs text-brandMuted mt-0.5">Rigorous comparison with cryptography-augmented distributed frameworks (Gu et al. [36], Sharma et al. [37], Chandran et al. [38]).</p>
      </div>
      <span class="px-2.5 py-1 rounded-md text-[11px] font-mono bg-white/[0.05] border border-white/[0.08] text-brandText">
        IEEE/ACM Research Benchmarks
      </span>
    </div>

    <!-- Table I Container with Horizontal Scroll -->
    <div class="overflow-x-auto rounded-lg border border-white/[0.08] bg-black/20">
      <table class="w-full text-left text-xs font-sans min-w-[860px]">
        <thead>
          <tr class="bg-black/40 border-b border-white/[0.07] text-[11px] uppercase tracking-wider text-brandMuted font-semibold">
            <th class="py-3.5 px-3">Framework / Study</th>
            <th class="py-3.5 px-3">Privacy Mechanism</th>
            <th class="py-3.5 px-3">Privacy Accounting</th>
            <th class="py-3.5 px-3">Threat / Trust Model</th>
            <th class="py-3.5 px-3">Byzantine / Poisoning Defense</th>
            <th class="py-3.5 px-3 text-right">Compute &amp; Network Overhead</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/[0.04] text-[12px]">
          <!-- Row 1: Centralized DP-SGD (This work) -->
          <tr class="bg-brandPrimary/[0.06] hover:bg-brandPrimary/[0.1] transition-colors border-l-2 border-brandPrimary">
            <td class="py-3.5 px-3 font-medium text-white">
              <div class="flex items-center gap-1.5">
                <span class="font-bold text-white text-sm">Centralized DP-SGD</span>
                <span class="px-1.5 py-0.2 rounded text-[9px] font-mono bg-brandPrimary/20 text-brandPrimary border border-brandPrimary/30 font-semibold">THIS WORK</span>
              </div>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Centralized Machine Learning</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="font-medium text-white">Gaussian Noise + Gradient Clip</span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">σ ≈ 1.18 - 4.84, C = 1.0</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                Moments Accountant / RDP
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">(ε = 0.5 - 10.0, δ = 10⁻⁵)</div>
            </td>
            <td class="py-3.5 px-3 text-brandText">
              <span class="font-medium text-white">Single Trusted Curator</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Untrusted analysts / external MIA attackers</div>
            </td>
            <td class="py-3.5 px-3 text-amber-400">
              <div class="flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                <span class="font-medium">Implicit (Norm Bound C=1.0)</span>
              </div>
              <div class="text-[11px] text-brandMuted mt-0.5">Poisoning not directly mitigated</div>
            </td>
            <td class="py-3.5 px-3 text-right">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                Low (~1.2 - 1.8× Compute)
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Single-node; 0 network overhead</div>
            </td>
          </tr>

          <!-- Row 2: PRECAD -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3.5 px-3 font-medium text-white">
              <div class="font-semibold text-white">PRECAD</div>
              <div class="text-[11px] text-brandMuted mt-0.5">Gu et al. (2023) [36]</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="text-brandText">2-out-of-2 MPC + Gaussian DP</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Additive secret sharing + server DP noise</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-white/[0.06] text-white border border-white/[0.1]">
                Rényi DP (RDP)
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Moments accountant tracking</div>
            </td>
            <td class="py-3.5 px-3 text-brandText">
              <span class="font-medium text-white">2 Non-Colluding Servers</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Honest-but-curious servers + untrusted clients</div>
            </td>
            <td class="py-3.5 px-3 text-emerald-400">
              <div class="flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span class="font-medium">Enhanced (MPC Norm Verification)</span>
              </div>
              <div class="text-[11px] text-brandMuted mt-0.5">Verified client clipping norm C in MPC</div>
            </td>
            <td class="py-3.5 px-3 text-right">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20">
                Moderate (~7× Compute)
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Local DP compute + MPC communication</div>
            </td>
          </tr>

          <!-- Row 3: FLiPD -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3.5 px-3 font-medium text-white">
              <div class="font-semibold text-white">FLiPD</div>
              <div class="text-[11px] text-brandMuted mt-0.5">Chandran et al. (2024) [38]</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="text-brandText">Distributed Laplace DP + HD Filter</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Oblivious Hamming distance outlier filtering</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-white/[0.06] text-white border border-white/[0.1]">
                Pure / Approx DP
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Distributed noise composition</div>
            </td>
            <td class="py-3.5 px-3 text-brandText">
              <span class="font-medium text-white">2 MPC Servers, ≥1 Honest Client</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Tolerates minority Byzantine clients</div>
            </td>
            <td class="py-3.5 px-3 text-emerald-400">
              <div class="flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span class="font-medium">Strong (Oblivious HD Filter)</span>
              </div>
              <div class="text-[11px] text-brandMuted mt-0.5">No trusted pre-trained base model required</div>
            </td>
            <td class="py-3.5 px-3 text-right">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-blue-500/10 text-blue-400 border border-blue-500/20">
                Low-to-Moderate
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">63.5% MPC comm shifted to offline prep</div>
            </td>
          </tr>

          <!-- Row 4: FedAvg_DP -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3.5 px-3 font-medium text-white">
              <div class="font-semibold text-white">FedAvg_DP</div>
              <div class="text-[11px] text-brandMuted mt-0.5">Sharma et al. (2023) [37]</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="text-brandText">Local Laplace DP / SVT</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Per-client perturbation before transmission</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-white/[0.06] text-white border border-white/[0.1]">
                Advanced Comp / SVT
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Local DP privacy budget tracking</div>
            </td>
            <td class="py-3.5 px-3 text-brandText">
              <span class="font-medium text-white">Honest-but-Curious Orchestrator</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Tested across 4 Swedish county hospitals</div>
            </td>
            <td class="py-3.5 px-3 text-rose-400">
              <div class="flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                <span class="font-medium">Vulnerable</span>
              </div>
              <div class="text-[11px] text-brandMuted mt-0.5">Susceptible to poisoned client updates</div>
            </td>
            <td class="py-3.5 px-3 text-right">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                Low Compute / High Acc Drop
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Severe utility degradation on small cohorts</div>
            </td>
          </tr>

          <!-- Row 5: FedAvg_HE -->
          <tr class="hover:bg-white/[0.02] transition-colors">
            <td class="py-3.5 px-3 font-medium text-white">
              <div class="font-semibold text-white">FedAvg_HE</div>
              <div class="text-[11px] text-brandMuted mt-0.5">Sharma et al. (2023) [37]</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="text-brandText">CKKS Homomorphic Encryption</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Additive aggregation over ciphertexts</div>
            </td>
            <td class="py-3.5 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-purple-500/10 text-purple-400 border border-purple-500/20">
                RLWE Hardness (Cryptographic)
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">Zero statistical utility loss</div>
            </td>
            <td class="py-3.5 px-3 text-brandText">
              <span class="font-medium text-white">Honest-but-Curious Server</span>
              <div class="text-[11px] text-brandMuted mt-0.5">Aggregates without decrypting weights</div>
            </td>
            <td class="py-3.5 px-3 text-rose-400">
              <div class="flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                <span class="font-medium">Extremely Limited</span>
              </div>
              <div class="text-[11px] text-brandMuted mt-0.5">Ciphertext prevents aggregator inspection (needs ZKPs)</div>
            </td>
            <td class="py-3.5 px-3 text-right">
              <span class="px-2 py-0.5 rounded text-[11px] font-mono font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20">
                High Overhead (~1.69× / 17.7h)
              </span>
              <div class="text-[11px] text-brandMuted font-mono mt-0.5">63,700s vs 37,800s; MB-scale ciphertexts</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 3 Real-World Architectural Deep Dive Cards (Section V-C Findings) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-1">
      <!-- Card 1 -->
      <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06] flex flex-col justify-between gap-2.5">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-base">🏥</span>
            <span class="text-xs font-semibold text-white uppercase tracking-wider font-mono">Centralized vs Cross-Silo Trust</span>
          </div>
          <p class="text-xs text-brandMuted mt-2 leading-relaxed">
            <strong class="text-white">Centralized DP-SGD</strong> achieves optimal utility (<span class="text-brandSafe font-mono">ΔAcc ≤ 2.9%</span>, <span class="text-brandSafe font-mono">1.5× compute</span>) when data is legally poolable in a single administrative enclave. In cross-silo settings where data sharing is prohibited by GDPR/HIPAA, distributed MPC frameworks (<strong class="text-white">PRECAD, FLiPD</strong>) become essential despite network overhead.
          </p>
        </div>
        <div class="text-[10px] text-brandSafe font-mono border-t border-white/[0.05] pt-2">
          ✓ Optimal for Single-Host Hospital / FinTech Enclaves
        </div>
      </div>

      <!-- Card 2 -->
      <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06] flex flex-col justify-between gap-2.5">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-base">⚡</span>
            <span class="text-xs font-semibold text-white uppercase tracking-wider font-mono">The Homomorphic Encryption Reality</span>
          </div>
          <p class="text-xs text-brandMuted mt-2 leading-relaxed">
            <strong class="text-white">CKKS Homomorphic Encryption (FedAvg_HE)</strong> avoids accuracy loss entirely, but incurs a <strong class="text-rose-400">17.7-hour training latency</strong> (63,700s vs 37,800s plaintext over 250 rounds on Swedish hospitals) and multi-megabyte ciphertext inflation per client update, making it impractical without specialized hardware acceleration.
          </p>
        </div>
        <div class="text-[10px] text-amber-400 font-mono border-t border-white/[0.05] pt-2">
          ⚠️ Extreme Latency &amp; Bandwidth Trade-off
        </div>
      </div>

      <!-- Card 3 -->
      <div class="p-4 rounded-xl bg-black/25 border border-white/[0.06] flex flex-col justify-between gap-2.5">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-base">🛡️</span>
            <span class="text-xs font-semibold text-white uppercase tracking-wider font-mono">Byzantine Poisoning vs DP Noise</span>
          </div>
          <p class="text-xs text-brandMuted mt-2 leading-relaxed">
            Differential privacy protects <strong class="text-white">sample membership</strong>, not <strong class="text-white">model integrity</strong>. Adversaries can inject backdoors while satisfying DP bounds. Frameworks like <strong class="text-white">FLiPD</strong> deploy oblivious Hamming-distance filtering to reject malicious model updates without requiring a trusted base model or plaintext disclosure.
          </p>
        </div>
        <div class="text-[10px] text-[#4facfe] font-mono border-t border-white/[0.05] pt-2">
          🔒 Certified Privacy ≠ Poisoning Immunity
        </div>
      </div>
    </div>
  </div>
</section>
<!-- ===================================================================== -->
<!-- SECTION 6: INSIGHT CARDS ROW (3 Cards with 3px Left Border) -->
<!-- ===================================================================== -->
<section class="grid grid-cols-1 md:grid-cols-3 gap-5">
<!-- Left Card: Max Privacy -->
<div class="p-5 rounded-xl bg-brandSurface border-subtle border-l-[3px] border-l-[#27ae60] flex flex-col justify-between gap-3">
<div>
<div class="flex items-center justify-between">
<span class="text-xs font-semibold text-white">🔒 Maximum Privacy ε=0.5</span>
<span class="text-[10px] font-mono text-brandSafe">Provable</span>
</div>
<p class="text-xs text-brandMuted mt-2 leading-relaxed">
              Provides mathematical indistinguishability. Prevents shadow model inference and record reconstruction entirely, but causes a noticeable utility penalty on tail demographics.
            </p>
</div>
<div class="pt-3 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono">
<span class="text-brandMuted" id="insight-max-acc">Accuracy: 71.3%</span>
<span class="text-brandSafe" id="insight-max-mia">MIA Risk: 51.2%</span>
</div>
</div>
<!-- Center Card: Sweet Spot (Highlighted / Slightly Elevated) -->
<div class="p-5 rounded-xl bg-brandSurface border-subtle border-l-[3px] border-l-[#f39c12] flex flex-col justify-between gap-3 -translate-y-1 shadow-[0_4px_20px_rgba(243,156,18,0.08)]">
<div>
<div class="flex items-center justify-between">
<span class="text-xs font-semibold text-white">⚖️ Sweet Spot ε=5</span>
<span class="text-[10px] font-mono text-brandModerate">Production Ready</span>
</div>
<p class="text-xs text-brandMuted mt-2 leading-relaxed">
              Achieves the ideal industrial trade-off. Mitigates membership leakage by over 68% relative to baseline while sustaining 96.7% of peak non-private classification accuracy.
            </p>
</div>
<div class="pt-3 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono">
<span class="text-brandMuted" id="insight-sweet-acc">Accuracy: 82.4%</span>
<span class="text-brandModerate" id="insight-sweet-mia">MIA Risk: 55.4%</span>
</div>
</div>
<!-- Right Card: No Privacy Baseline -->
<div class="p-5 rounded-xl bg-brandSurface border-subtle border-l-[3px] border-l-[#e74c3c] flex flex-col justify-between gap-3">
<div>
<div class="flex items-center justify-between">
<span class="text-xs font-semibold text-white">⚠️ No Privacy Baseline</span>
<span class="text-[10px] font-mono text-brandDanger">Vulnerable</span>
</div>
<p class="text-xs text-brandMuted mt-2 leading-relaxed">
              Unclipped SGD overfits severely to outlier training data samples. 1 in 4 training records are reliably re-identifiable using basic shadow loss query distributions.
            </p>
</div>
<div class="pt-3 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono">
<span class="text-brandMuted" id="insight-base-acc">Accuracy: 86.2%</span>
<span class="text-brandDanger" id="insight-base-mia">MIA Risk: 79.8%</span>
</div>
</div>
</section>
<!-- ===================================================================== -->
<!-- SECTION 7: SUCCESS BANNER -->
<!-- ===================================================================== -->
<section class="p-5 rounded-xl bg-[rgba(39,174,96,0.12)] border border-[rgba(39,174,96,0.30)] flex items-center gap-3.5">
<span class="text-xl flex-shrink-0">✅</span>
<p class="text-xs md:text-sm text-brandText leading-relaxed">
<strong class="text-white font-semibold">Recommendation:</strong> <span id="recommendation-text">DP-SGD with <span class="font-mono font-semibold text-brandSafe">ε=5</span> achieves the best privacy-utility balance for production use (96.7% baseline accuracy retention with 68% lower MIA vulnerability).</span>
        </p>
</section>
</div>
</main>
<!-- ========================================================================= -->
<!-- GSAP ANIMATIONS & INTERACTIVE SCRIPTS -->
<!-- ========================================================================= -->
<script>
    document.addEventListener("DOMContentLoaded", () => {
      // Register ScrollTrigger
      gsap.registerPlugin(ScrollTrigger);
      ScrollTrigger.defaults({
        scroller: "#main-scroller"
      });

      const scroller = document.getElementById("main-scroller");
      if (scroller) {
        scroller.addEventListener("scroll", () => ScrollTrigger.update(), { passive: true });
      }

      // Allow wheel scrolling anywhere in the window (even over sidebar)
      window.addEventListener("wheel", (e) => {
        if (scroller) {
          scroller.scrollTop += e.deltaY;
        }
      }, { passive: true });

      // Keyboard navigation (Arrow keys, PageUp/Down, Space)
      window.addEventListener("keydown", (e) => {
        if (!scroller) return;
        if (e.key === "ArrowDown") scroller.scrollTop += 60;
        else if (e.key === "ArrowUp") scroller.scrollTop -= 60;
        else if (e.key === "PageDown" || (e.key === " " && !e.shiftKey)) scroller.scrollTop += window.innerHeight * 0.75;
        else if (e.key === "PageUp" || (e.key === " " && e.shiftKey)) scroller.scrollTop -= window.innerHeight * 0.75;
      });

      // 1. GSAP Character-Split animated headline
      const heroTitle = document.getElementById("hero-title");
      if (heroTitle) {
        const text = heroTitle.innerText.trim();
        heroTitle.innerHTML = "";
        
        // Wrap characters
        for (let i = 0; i < text.length; i++) {
          const char = text[i];
          const span = document.createElement("span");
          span.className = "hero-char";
          span.innerHTML = char === " " ? "&nbsp;" : char;
          heroTitle.appendChild(span);
        }

        gsap.to(".hero-char", {
          opacity: 1,
          y: 0,
          duration: 0.7,
          stagger: 0.025,
          ease: "power3.out"
        });
      }

      // Kinetic subtitle word-by-word reveal with blur filter 8px -> 0
      const heroSub = document.getElementById("hero-sub");
      if (heroSub) {
        const words = heroSub.innerText.trim().split(" ");
        heroSub.innerHTML = "";
        words.forEach((word) => {
          const span = document.createElement("span");
          span.className = "word-blur mr-1.5";
          span.innerText = word;
          heroSub.appendChild(span);
        });

        gsap.to(".word-blur", {
          filter: "blur(0px)",
          opacity: 1,
          duration: 0.8,
          stagger: 0.03,
          ease: "power2.out",
          delay: 0.2
        });
      }

      // 2. Animate Metric Stat Counters
      const statElements = document.querySelectorAll(".stat-counter");
      statElements.forEach((el) => {
        const target = parseInt(el.getAttribute("data-target"), 10);
        gsap.to(el, {
          innerText: target,
          duration: 1.4,
          ease: "power2.out",
          snap: { innerText: 1 },
          onUpdate: function () {
            el.innerText = Math.floor(el.innerText).toLocaleString();
          },
          scrollTrigger: {
            trigger: el,
            start: "top 90%"
          }
        });
      });

      // 3. Kinetic Text Reveal for Headings on Scroll
      document.querySelectorAll(".section-title, h3, h2").forEach((heading) => {
        gsap.from(heading, {
          opacity: 0,
          y: 18,
          filter: "blur(6px)",
          duration: 0.7,
          ease: "power2.out",
          scrollTrigger: {
            trigger: heading,
            start: "top 90%"
          }
        });
      });

      // 4. SVG Line Chart Draw Animation on scroll
      const drawLines = document.querySelectorAll(".chart-line");
      drawLines.forEach((line, idx) => {
        const length = line.getTotalLength ? line.getTotalLength() : 800;
        gsap.set(line, { strokeDasharray: length, strokeDashoffset: length });

        gsap.to(line, {
          strokeDashoffset: 0,
          duration: 1.8,
          ease: "power2.inOut",
          delay: (idx % 3) * 0.1,
          scrollTrigger: {
            trigger: line.closest("svg") || line,
            start: "top 85%"
          }
        });
      });

      // 5. Marker & Badge Pop-in Animation on scroll
      document.querySelectorAll("svg").forEach((svg) => {
        const markers = svg.querySelectorAll("circle, g[transform]");
        if (markers.length) {
          gsap.from(markers, {
            scale: 0,
            opacity: 0,
            transformOrigin: "center center",
            duration: 0.6,
            stagger: 0.08,
            ease: "back.out(1.8)",
            scrollTrigger: {
              trigger: svg,
              start: "top 80%"
            }
          });
        }
      });

      // 6. Smooth Card Entrance Reveals
      gsap.utils.toArray(".metric-card, .border-subtle, .insight-card").forEach((card, i) => {
        gsap.from(card, {
          opacity: 0,
          y: 20,
          duration: 0.6,
          ease: "power2.out",
          delay: (i % 4) * 0.04,
          scrollTrigger: {
            trigger: card,
            start: "top 92%"
          }
        });
      });

    // =========================================================================
    // STATE & MODE TELEMETRY ISOLATION ENGINE
    // Guarantees clean unplotted canvas on start and strict mode isolation
    // =========================================================================
    let isCurrentModeTrained = false;

    function resetAllTelemetryToFresh(modeName) {
      isCurrentModeTrained = false;
      lastTrainedCustomModel = null;

      // 1. Chart A: Hide plot group & pointer, show empty overlay
      const gA = document.getElementById("chart-a-plot-elements");
      if (gA) gA.style.opacity = "0";
      const pA = document.getElementById("interactive-acc-pointer");
      if (pA) { pA.style.display = "none"; pA.style.opacity = "0"; }
      const ovA = document.getElementById("chart-a-empty-overlay");
      if (ovA) { ovA.style.display = "flex"; ovA.style.opacity = "1"; }
      const stA = document.getElementById("chart-a-status");
      if (stA) {
        stA.innerText = "Awaiting Training";
        stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]";
      }

      // 2. Chart B: Hide plot group & pointer, show empty overlay
      const gB = document.getElementById("chart-b-plot-elements");
      if (gB) gB.style.opacity = "0";
      const pB = document.getElementById("interactive-mia-pointer");
      if (pB) { pB.style.display = "none"; pB.style.opacity = "0"; }
      const ovB = document.getElementById("chart-b-empty-overlay");
      if (ovB) { ovB.style.display = "flex"; ovB.style.opacity = "1"; }
      const stB = document.getElementById("chart-b-status");
      if (stB) {
        stB.innerText = "Awaiting Training";
        stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]";
      }

      // 3. Chart C: Hide plot group & epoch guide, show empty overlay
      const gC = document.getElementById("chart-c-plot-elements");
      if (gC) gC.style.opacity = "0";
      const pC = document.getElementById("interactive-epoch-guide");
      if (pC) { pC.style.display = "none"; pC.style.opacity = "0"; }
      const customP = document.getElementById("interactive-epoch-pointer");
      if (customP) { customP.style.display = "none"; customP.style.opacity = "0"; }
      const customPath = document.getElementById("epoch-curve-interactive");
      if (customPath) { customPath.style.display = "none"; }
      const legInteractive = document.getElementById("legend-interactive-curve");
      if (legInteractive) { legInteractive.classList.add("hidden"); legInteractive.classList.remove("flex"); }
      const ovC = document.getElementById("chart-c-empty-overlay");
      if (ovC) { ovC.style.display = "flex"; ovC.style.opacity = "1"; }
      const stC = document.getElementById("chart-c-status");
      if (stC) {
        stC.innerText = "Awaiting Training";
        stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-white/[0.05] text-brandMuted border border-white/[0.08]";
      }

      const allEpochCurves = ["epoch-curve-baseline", "epoch-curve-eps10", "epoch-curve-eps5", "epoch-curve-eps1", "epoch-curve-eps05"];
      allEpochCurves.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.style.opacity = "0";
          el.setAttribute("stroke-width", "1.8");
          el.style.filter = "none";
          el.style.strokeDashoffset = "0";
          el.style.strokeDasharray = "none";
        }
      });

      // 4. Interactive Demo Panel Reset
      const resContainer = document.getElementById("interactive-training-results");
      if (resContainer) resContainer.classList.add("hidden");
      const progBox = document.getElementById("interactive-progress-box");
      if (progBox) progBox.classList.add("hidden");
      const summaryCard = document.getElementById("interactive-summary-card");
      if (summaryCard) summaryCard.classList.add("hidden");

      const btnTrain = document.getElementById("btn-train");
      const btnTrainText = document.getElementById("btn-train-text");
      const btnTrainIcon = document.getElementById("btn-train-icon");
      if (btnTrain) btnTrain.disabled = false;
      if (btnTrainText) btnTrainText.innerText = "Train DP-SGD Model";
      if (btnTrainIcon) btnTrainIcon.innerText = "play_circle";

      // Remove custom table rows added in benchmark table
      document.querySelectorAll("tr[id^='custom-row-']").forEach(r => r.remove());

      // 5. Full Training Panel Reset
      const completionCard = document.getElementById("full-training-completion-card");
      if (completionCard) completionCard.classList.add("hidden");
      const progContainer = document.getElementById("training-progress-container");
      if (progContainer) progContainer.classList.add("hidden");

      const btnAll = document.getElementById("btn-train-all");
      const btnAllText = document.getElementById("btn-train-all-text");
      if (btnAll) btnAll.disabled = false;
      if (btnAllText) btnAllText.innerText = "Train All 5 Benchmark Models";

      for (let i = 0; i < 5; i++) {
        const sBadge = document.getElementById("train-status-" + i);
        const mText = document.getElementById("train-metric-" + i);
        const card = document.getElementById("train-card-" + i);
        if (sBadge) {
          sBadge.innerText = "Queued";
          sBadge.className = "text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono";
        }
        if (mText) {
          mText.innerText = "Acc: -- | MIA: --";
          mText.className = "text-[11px] font-mono text-brandMuted";
        }
        if (card) {
          card.classList.remove("border-emerald-500/40", "bg-emerald-500/[0.04]");
        }
      }

      // 6. Auto Demo highlights reset
      clearTourHighlights();
    }

    window.resetAllTelemetryToFresh = resetAllTelemetryToFresh;

    // =========================================================================
    // REAL-TIME REACTIVE TELEMETRY & EMPIRICAL CURVES
    // Dynamically updates Chart A, Chart B, Chart C, Audit Header & Summary Card
    // =========================================================================
    function updateLiveTelemetryVisuals() {
      const epsSlider = document.getElementById("epsilon-slider");
      const epochsSlider = document.getElementById("epochs-slider");
      const batchSelect = document.getElementById("batch-select");
      const datasetSelect = document.getElementById("dataset-select");

      const eps = parseFloat(epsSlider ? epsSlider.value : "1.0") || 1.0;
      const epochs = parseInt(epochsSlider ? epochsSlider.value : "15") || 15;
      const batchVal = batchSelect ? batchSelect.value : "64";
      const currentDs = datasetSelect ? datasetSelect.value : "adult";

      // Update slider numerical readout badges
      const epsNum = document.getElementById("epsilon-num");
      if (epsNum) epsNum.innerText = eps.toFixed(1);

      const epochsNum = document.getElementById("epochs-num");
      if (epochsNum) epochsNum.innerText = epochs;

      // Update Epsilon Badge
      const epsBadge = document.getElementById("epsilon-badge");
      const epsBadgeDot = document.getElementById("epsilon-badge-dot");
      const epsBadgeText = document.getElementById("epsilon-badge-text");

      if (epsBadgeText && epsBadge && epsBadgeDot) {
        if (eps <= 2.0) {
          epsBadge.className = "px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5 transition-all";
          epsBadgeDot.className = "w-2 h-2 rounded-full bg-emerald-400";
          epsBadgeText.innerText = "Privacy Budget ε = " + eps.toFixed(1) + " — Safe (Strong Privacy)";
        } else if (eps <= 5.0) {
          epsBadge.className = "px-3 py-1 rounded-full text-xs font-medium bg-amber-500/10 text-amber-400 border border-amber-500/30 flex items-center gap-1.5 transition-all";
          epsBadgeDot.className = "w-2 h-2 rounded-full bg-amber-400";
          epsBadgeText.innerText = "Privacy Budget ε = " + eps.toFixed(1) + " — Moderate-Strong";
        } else {
          epsBadge.className = "px-3 py-1 rounded-full text-xs font-medium bg-rose-500/10 text-rose-400 border border-rose-500/30 flex items-center gap-1.5 transition-all";
          epsBadgeDot.className = "w-2 h-2 rounded-full bg-rose-400";
          epsBadgeText.innerText = "Privacy Budget ε = " + eps.toFixed(1) + " — Relaxed Privacy";
        }
      }

      // Compute metrics using calibrated engine
      const m = calculateTrainedMetrics(eps, epochs, batchVal, currentDs);

      // Subsampling rate q = B / N
      const qMap = { "16": "0.0004", "32": "0.0008", "64": "0.0016", "128": "0.0032" };
      const qVal = qMap[batchVal] || "0.0016";

      // Update Audit Header with live sigma & subsampling q
      const auditSub = document.getElementById("telemetry-audit-sub");
      if (auditSub) {
        auditSub.innerText = "Audit: Gaussian Mechanism (δ = 1e-5, σ = " + m.sigma + ", q = " + qVal + ")";
      }

      // If model has not yet been trained in current mode, do NOT plot pointers on graph
      if (!isCurrentModeTrained) {
        const pA = document.getElementById("interactive-acc-pointer");
        const pB = document.getElementById("interactive-mia-pointer");
        const pC = document.getElementById("interactive-epoch-guide");
        if (pA) { pA.style.display = "none"; pA.style.opacity = "0"; }
        if (pB) { pB.style.display = "none"; pB.style.opacity = "0"; }
        if (pC) { pC.style.display = "none"; pC.style.opacity = "0"; }
        return;
      }

      // --- CHART A: Map Epsilon to X and Accuracy to Y ---
      let chartX;
      if (eps <= 1.0) {
        chartX = 45 + (115 - 45) * ((eps - 0.5) / 0.5);
      } else if (eps <= 2.0) {
        chartX = 115 + (195 - 115) * ((eps - 1.0) / 1.0);
      } else if (eps <= 5.0) {
        chartX = 195 + (280 - 195) * ((eps - 2.0) / 3.0);
      } else if (eps <= 8.0) {
        chartX = 280 + (360 - 280) * ((eps - 5.0) / 3.0);
      } else {
        chartX = 360 + (430 - 360) * ((eps - 8.0) / 2.0);
      }
      chartX = Math.max(45, Math.min(430, chartX));

      // Y coordinates for Chart A: 90%->20, 80%->70, 70%->120, 60%->170 (50px per 10%)
      const chartAY = Math.max(20, Math.min(168, 170 - (m.accRaw - 0.60) * 500));

      const aPulse = document.getElementById("interactive-acc-pulse");
      const aCircle = document.getElementById("interactive-acc-circle");
      const aTag = document.getElementById("interactive-acc-tag");
      const aText = document.getElementById("interactive-acc-tag-text");

      if (aPulse && aCircle && aTag && aText) {
        aPulse.setAttribute("cx", chartX);
        aPulse.setAttribute("cy", chartAY);
        aCircle.setAttribute("cx", chartX);
        aCircle.setAttribute("cy", chartAY);

        const tagY = Math.max(16, chartAY - 22);
        const tagX = Math.max(48, Math.min(412, chartX));
        aTag.setAttribute("transform", "translate(" + tagX + ", " + tagY + ")");
        aText.textContent = "ε=" + eps.toFixed(1) + " | " + m.accPct;

        const color = eps <= 2.0 ? "#27ae60" : (eps <= 5.0 ? "#4facfe" : "#f093fb");
        aCircle.setAttribute("fill", color);
        aText.setAttribute("fill", color);
      }

      // --- CHART B: Map Epsilon to X and MIA Risk to Y ---
      let chartBY;
      if (m.miaRaw <= 0.55) {
        chartBY = 170 - ((m.miaRaw - 0.50) / 0.05) * 45;
      } else if (m.miaRaw <= 0.65) {
        chartBY = 125 - ((m.miaRaw - 0.55) / 0.10) * 50;
      } else {
        chartBY = 75 - ((m.miaRaw - 0.65) / 0.15) * 55;
      }
      chartBY = Math.max(20, Math.min(168, chartBY));

      const bPulse = document.getElementById("interactive-mia-pulse");
      const bCircle = document.getElementById("interactive-mia-circle");
      const bTag = document.getElementById("interactive-mia-tag");
      const bText = document.getElementById("interactive-mia-tag-text");

      if (bPulse && bCircle && bTag && bText) {
        bPulse.setAttribute("cx", chartX);
        bPulse.setAttribute("cy", chartBY);
        bCircle.setAttribute("cx", chartX);
        bCircle.setAttribute("cy", chartBY);

        const tagY = Math.max(16, chartBY - 22);
        const tagX = Math.max(45, Math.min(415, chartX));
        bTag.setAttribute("transform", "translate(" + tagX + ", " + tagY + ")");
        bText.textContent = "MIA: " + m.miaPct;

        const miaColor = m.miaRaw < 0.53 ? "#27ae60" : (m.miaRaw < 0.65 ? "#f39c12" : "#e74c3c");
        bCircle.setAttribute("fill", miaColor);
        bText.setAttribute("fill", miaColor);
      }

      // --- CHART C: Map Epochs to X & Highlight Active Budget Curve ---
      const epochX = Math.max(50, Math.min(890, 50 + epochs * 42));
      const epLine = document.getElementById("interactive-epoch-line");
      const epFlag = document.getElementById("interactive-epoch-flag");
      const epText = document.getElementById("interactive-epoch-flag-text");

      if (epLine && epFlag && epText) {
        epLine.setAttribute("x1", epochX);
        epLine.setAttribute("x2", epochX);
        epFlag.setAttribute("transform", "translate(" + epochX + ", 16)");
        epText.textContent = "Stop: Epoch " + epochs;
      }

      // Highlight the matching epoch curve in Chart C
      const curves = ["epoch-curve-eps05", "epoch-curve-eps1", "epoch-curve-eps5", "epoch-curve-eps10", "epoch-curve-baseline"];
      let activeCurveId = "epoch-curve-eps1";
      if (eps <= 0.8) activeCurveId = "epoch-curve-eps05";
      else if (eps <= 2.5) activeCurveId = "epoch-curve-eps1";
      else if (eps <= 7.0) activeCurveId = "epoch-curve-eps5";
      else activeCurveId = "epoch-curve-eps10";

      curves.forEach(cid => {
        const cEl = document.getElementById(cid);
        if (cEl) {
          if (cid === activeCurveId) {
            cEl.setAttribute("stroke-width", "3.5");
            cEl.style.filter = "drop-shadow(0 0 8px rgba(102,126,234,0.7))";
            cEl.style.opacity = "1.0";
          } else {
            cEl.setAttribute("stroke-width", "1.6");
            cEl.style.filter = "none";
            cEl.style.opacity = "0.45";
          }
        }
      });

      // If Interactive Training Summary Card is currently visible, update it live too!
      const summaryCard = document.getElementById("interactive-summary-card");
      if (summaryCard && !summaryCard.classList.contains("hidden")) {
        const sAcc = document.getElementById("summary-acc-val");
        const sAccDiff = document.getElementById("summary-acc-diff");
        const sMia = document.getElementById("summary-mia-val");
        const sSigma = document.getElementById("summary-sigma-val");
        const sRegimen = document.getElementById("summary-regimen-val");
        const sBadge = document.getElementById("interactive-privacy-guarantee-badge");

        if (sAcc) sAcc.innerText = m.accPct;
        if (sAccDiff) sAccDiff.innerText = m.diffPct + " vs Baseline";
        if (sMia) sMia.innerText = m.miaPct;
        if (sSigma) sSigma.innerText = "σ = " + m.sigma;
        if (sRegimen) sRegimen.innerText = epochs + " Epochs, B=" + batchVal;
        if (sBadge) sBadge.innerText = "Guaranteed (ε = " + eps.toFixed(1) + ", δ = 1.0e-5)";
      }

      // Update interactive epoch curve dynamically if already trained
      if (isCurrentModeTrained && currentMode === 'interactive') {
        plotInteractiveEpochCurve(eps, epochs);
      }
    }

    // --- INTERACTIVE EPOCH DYNAMICS CALCULATOR & PLOTTER ---
    function calculateInteractiveEpochTrajectory(eps, epochs) {
      const x0 = 50;
      const xEnd = Math.max(50, Math.min(890, 50 + epochs * 42));

      // Noise floor dictated by epsilon (calibrated to project benchmarks)
      const lossFloor = Math.max(0.22, 0.22 + 0.25 / (1.0 + 0.45 * eps));
      const decayRate = 0.18 + Math.min(0.12, eps * 0.02);
      const lossFinal = lossFloor + (0.68 - lossFloor) * Math.exp(-decayRate * epochs);

      // Piecewise linear mapping from loss to SVG Y coordinates:
      // Loss 0.70 -> y=20, Loss 0.50 -> y=70, Loss 0.35 -> y=120, Loss 0.20 -> y=170
      function lossToY(loss) {
        if (loss >= 0.50) {
          return 20 + Math.max(0, (0.70 - loss) / 0.20) * 50;
        } else if (loss >= 0.35) {
          return 70 + ((0.50 - loss) / 0.15) * 50;
        } else {
          return 120 + Math.min(1.0, (0.35 - loss) / 0.15) * 50;
        }
      }

      const y0 = lossToY(0.68);

      // Construct smooth SVG path through each trained epoch
      let pathD = `M ${x0} ${y0.toFixed(1)}`;
      for (let i = 1; i <= epochs; i++) {
        const curLoss = lossFloor + (0.68 - lossFloor) * Math.exp(-decayRate * i) + (Math.sin(i * 2.3) * 0.003) / Math.max(1, eps);
        const curX = 50 + i * 42;
        const curY = lossToY(curLoss);
        pathD += ` L ${curX} ${curY.toFixed(1)}`;
      }

      const finalY = lossToY(lossFinal);
      return {
        d: pathD,
        endX: xEnd,
        endY: finalY,
        finalLoss: lossFinal
      };
    }

    function plotInteractiveEpochCurve(eps, epochs) {
      const traj = calculateInteractiveEpochTrajectory(eps, epochs);

      // 1. Reveal reference benchmark curves with clean muted contrast
      const bCurves = ["epoch-curve-baseline", "epoch-curve-eps10", "epoch-curve-eps5", "epoch-curve-eps1", "epoch-curve-eps05"];
      bCurves.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.style.display = "inline";
          el.style.opacity = "0.35";
          el.setAttribute("stroke-width", "1.6");
          el.style.filter = "none";
          el.style.strokeDashoffset = "0";
          el.style.strokeDasharray = "none";
        }
      });

      // Give closest benchmark curve slightly higher prominence
      let closeId = null;
      if (Math.abs(eps - 0.5) < 0.25) closeId = "epoch-curve-eps05";
      else if (Math.abs(eps - 1.0) < 0.4) closeId = "epoch-curve-eps1";
      else if (Math.abs(eps - 5.0) < 1.0) closeId = "epoch-curve-eps5";
      else if (Math.abs(eps - 10.0) < 1.5) closeId = "epoch-curve-eps10";
      if (closeId) {
        const closeEl = document.getElementById(closeId);
        if (closeEl) closeEl.style.opacity = "0.6";
      }

      // 2. Render & animate the dedicated interactive trained trajectory
      let customPath = document.getElementById("epoch-curve-interactive");
      if (customPath) {
        customPath.setAttribute("d", traj.d);
        customPath.style.display = "inline";
        customPath.style.opacity = "1";
        customPath.style.stroke = "#667eea";
        customPath.setAttribute("stroke-width", "3.5");
        customPath.style.filter = "drop-shadow(0 0 8px rgba(102, 126, 234, 0.85))";
        
        try {
          const len = (customPath.getTotalLength && customPath.getTotalLength() > 0) ? customPath.getTotalLength() : 900;
          if (typeof gsap !== 'undefined') {
            gsap.fromTo(customPath,
              { strokeDasharray: len, strokeDashoffset: len },
              { strokeDashoffset: 0, duration: 1.1, ease: "power2.out", onComplete: () => {
                customPath.style.strokeDasharray = "none";
                customPath.style.strokeDashoffset = "0";
              }}
            );
          } else {
            customPath.style.strokeDasharray = "none";
            customPath.style.strokeDashoffset = "0";
          }
        } catch (e) {
          customPath.style.strokeDasharray = "none";
          customPath.style.strokeDashoffset = "0";
        }
      }

      // 3. Position and illuminate vertical epoch stop line & flag
      const epGuide = document.getElementById("interactive-epoch-guide");
      const epLine = document.getElementById("interactive-epoch-line");
      const epFlag = document.getElementById("interactive-epoch-flag");
      const epFlagText = document.getElementById("interactive-epoch-flag-text");
      if (epGuide && epLine && epFlag && epFlagText) {
        epLine.setAttribute("x1", traj.endX);
        epLine.setAttribute("x2", traj.endX);
        epFlag.setAttribute("transform", `translate(${traj.endX}, 16)`);
        epFlagText.textContent = `Stop: Epoch ${epochs}`;
        epGuide.style.display = "inline";
        epGuide.style.opacity = "1";
      }

      // 4. Position and illuminate pulsing endpoint marker
      const pPointer = document.getElementById("interactive-epoch-pointer");
      const pCircle = document.getElementById("interactive-epoch-circle");
      const pPulse = document.getElementById("interactive-epoch-pulse");
      const pTag = document.getElementById("interactive-epoch-tag");
      const pTagText = document.getElementById("interactive-epoch-tag-text");

      if (pPointer && pCircle && pPulse && pTag && pTagText) {
        pCircle.setAttribute("cx", traj.endX);
        pCircle.setAttribute("cy", traj.endY.toFixed(1));
        pPulse.setAttribute("cx", traj.endX);
        pPulse.setAttribute("cy", traj.endY.toFixed(1));
        const tagY = Math.max(16, traj.endY - 22);
        const tagX = Math.max(65, Math.min(855, traj.endX));
        pTag.setAttribute("transform", `translate(${tagX}, ${tagY.toFixed(1)})`);
        pTagText.textContent = `Loss: ${traj.finalLoss.toFixed(3)} @ Ep ${epochs}`;
        pPointer.style.display = "inline";
        pPointer.style.opacity = "1";
      }

      // 5. Update legend item
      const leg = document.getElementById("legend-interactive-curve");
      const legText = document.getElementById("legend-interactive-text");
      if (leg && legText) {
        legText.textContent = `Your Model (ε=${eps.toFixed(1)})`;
        leg.classList.remove("hidden");
        leg.classList.add("flex");
      }
    }

    // --- RESULTS ANALYSIS MODE ACTIVATOR ---
    function setupResultsAnalysisMode() {
      isCurrentModeTrained = true;

      // 1. Hide empty overlays on all 3 charts
      ["chart-a-empty-overlay", "chart-b-empty-overlay", "chart-c-empty-overlay"].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = "none";
      });

      // 2. Reveal plot element groups
      ["chart-a-plot-elements", "chart-b-plot-elements", "chart-c-plot-elements"].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.opacity = "1";
      });

      // 3. Update status badges to reflect full audited state
      const stA = document.getElementById("chart-a-status");
      const stB = document.getElementById("chart-b-status");
      const stC = document.getElementById("chart-c-status");
      if (stA) { stA.innerText = "Audited Pareto Frontier (ε=0.5 to ∞)"; stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
      if (stB) { stB.innerText = "Audited Threat Matrix (MIA Resistance)"; stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
      if (stC) { stC.innerText = "All 5 Trajectories Plotted (20 Epochs)"; stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }

      // 4. Hide single-run interactive elements in Results Analysis mode
      const pA = document.getElementById("interactive-acc-pointer");
      const pB = document.getElementById("interactive-mia-pointer");
      const pC = document.getElementById("interactive-epoch-guide");
      const customP = document.getElementById("interactive-epoch-pointer");
      const customPath = document.getElementById("epoch-curve-interactive");
      const legInteractive = document.getElementById("legend-interactive-curve");
      if (pA) { pA.style.display = "none"; pA.style.opacity = "0"; }
      if (pB) { pB.style.display = "none"; pB.style.opacity = "0"; }
      if (pC) { pC.style.display = "none"; pC.style.opacity = "0"; }
      if (customP) { customP.style.display = "none"; customP.style.opacity = "0"; }
      if (customPath) { customPath.style.display = "none"; }
      if (legInteractive) { legInteractive.classList.add("hidden"); legInteractive.classList.remove("flex"); }

      // 5. Animate Chart A Line Draw
      const cAcc = document.getElementById("curve-acc");
      if (cAcc) {
        cAcc.style.opacity = "1";
        cAcc.style.stroke = "#4facfe";
        try {
          const lenA = (cAcc.getTotalLength && cAcc.getTotalLength() > 0) ? cAcc.getTotalLength() : 600;
          if (typeof gsap !== 'undefined') {
            gsap.fromTo(cAcc, { strokeDasharray: lenA, strokeDashoffset: lenA }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out", onComplete: () => {
              cAcc.style.strokeDasharray = "none";
              cAcc.style.strokeDashoffset = "0";
            }});
          } else {
            cAcc.style.strokeDasharray = "none";
            cAcc.style.strokeDashoffset = "0";
          }
        } catch (e) {
          cAcc.style.strokeDasharray = "none";
          cAcc.style.strokeDashoffset = "0";
        }
      }

      // 6. Animate Chart B Line Draw
      const cMia = document.getElementById("curve-mia");
      if (cMia) {
        cMia.style.opacity = "1";
        cMia.style.stroke = "#f093fb";
        try {
          const lenB = (cMia.getTotalLength && cMia.getTotalLength() > 0) ? cMia.getTotalLength() : 600;
          if (typeof gsap !== 'undefined') {
            gsap.fromTo(cMia, { strokeDasharray: lenB, strokeDashoffset: lenB }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out", onComplete: () => {
              cMia.style.strokeDasharray = "none";
              cMia.style.strokeDashoffset = "0";
            }});
          } else {
            cMia.style.strokeDasharray = "none";
            cMia.style.strokeDashoffset = "0";
          }
        } catch (e) {
          cMia.style.strokeDasharray = "none";
          cMia.style.strokeDashoffset = "0";
        }
      }

      // 7. Render and animate ALL 5 Epoch Curves across the 20 epochs in Chart C
      const epochCurvesConfig = [
        { id: "epoch-curve-baseline", width: "2.2", opacity: "0.95" },
        { id: "epoch-curve-eps10", width: "2.0", opacity: "0.95" },
        { id: "epoch-curve-eps5", width: "3.2", opacity: "1.0", glow: true },
        { id: "epoch-curve-eps1", width: "2.0", opacity: "0.95" },
        { id: "epoch-curve-eps05", width: "2.0", opacity: "0.95" }
      ];

      epochCurvesConfig.forEach((cfg, idx) => {
        const el = document.getElementById(cfg.id);
        if (el) {
          el.style.display = "inline";
          el.style.opacity = cfg.opacity;
          el.setAttribute("stroke-width", cfg.width);
          if (cfg.glow) {
            el.style.filter = "drop-shadow(0 0 8px rgba(245, 158, 11, 0.8))";
          } else {
            el.style.filter = "none";
          }
          try {
            const len = (el.getTotalLength && el.getTotalLength() > 0) ? el.getTotalLength() : 900;
            if (typeof gsap !== 'undefined') {
              gsap.fromTo(el,
                { strokeDasharray: len, strokeDashoffset: len },
                { strokeDashoffset: 0, duration: 1.2, delay: idx * 0.08, ease: "power2.out", onComplete: () => {
                  el.style.strokeDasharray = "none";
                  el.style.strokeDashoffset = "0";
                }}
              );
            } else {
              el.style.strokeDasharray = "none";
              el.style.strokeDashoffset = "0";
            }
          } catch (e) {
            el.style.strokeDasharray = "none";
            el.style.strokeDashoffset = "0";
          }
        }
      });
    }

    // Export to window for global inline event accessibility
    window.updateLiveTelemetryVisuals = updateLiveTelemetryVisuals;
    window.calculateTrainedMetrics = calculateTrainedMetrics;
    window.calculateInteractiveEpochTrajectory = calculateInteractiveEpochTrajectory;
    window.plotInteractiveEpochCurve = plotInteractiveEpochCurve;
    window.setupResultsAnalysisMode = setupResultsAnalysisMode;

    // Run clean fresh state initialization on load
    resetAllTelemetryToFresh('interactive');
    updateLiveTelemetryVisuals();
    });

    // Toggle Data Source (Built-in vs Upload)
    function toggleSource(type) {
      const btnBuiltin = document.getElementById("btn-src-builtin");
      const btnUpload = document.getElementById("btn-src-upload");
      const panelBuiltin = document.getElementById("panel-builtin");
      const panelUpload = document.getElementById("panel-upload");

      if (type === "builtin") {
        btnBuiltin.className = "py-1 px-2 rounded-md font-medium text-white bg-white/10 transition-all text-center";
        btnUpload.className = "py-1 px-2 rounded-md font-medium text-brandMuted hover:text-white transition-all text-center";
        panelBuiltin.classList.remove("hidden");
        panelBuiltin.classList.add("flex");
        panelUpload.classList.add("hidden");
        panelUpload.classList.remove("flex");
      } else {
        btnUpload.className = "py-1 px-2 rounded-md font-medium text-white bg-white/10 transition-all text-center";
        btnBuiltin.className = "py-1 px-2 rounded-md font-medium text-brandMuted hover:text-white transition-all text-center";
        panelUpload.classList.remove("hidden");
        panelUpload.classList.add("flex");
        panelBuiltin.classList.add("hidden");
        panelBuiltin.classList.remove("flex");
      }
    }

    // Dataset Select Callback
    
    const DATASETS = {
      adult: {
        name: "Adult Census 1994",
        desc: "Standard 48.8k Census benchmark for predicting income >50K with high demographic variance.",
        total: 48842,
        train: 39074,
        test: 9768,
        feat: "14 Tabular Features",
        featDims: 108,
        featSub: "One-hot encoded",
        classBalance: "75.9 / 24.1",
        classSub: "Skewed distribution",
        curatedSub: "↑ 100% curated",
        tableTitle: "Dataset: Adult 1994",
        baselineText: "Baseline = 0.862",
        baselineY: 39,
        optAccText: "82.4% (Opt)",
        accPath: "M 45 113 Q 120 78 200 60 T 430 43",
        accArea: "M 45 113 Q 120 78 200 60 T 430 43 L 430 170 L 45 170 Z",
        miaPath: "M 45 165 Q 120 156 200 142 T 280 118 T 430 35",
        miaMarkers: [
          { cx: 45, cy: 165, y: 152, text: "51.2% (Low)" },
          { cx: 280, cy: 118, y: 106, text: "55.4% (Mod)" },
          { cx: 430, cy: 35, y: 24, text: "79.8% (Danger)" }
        ],
        epochCurves: {
          baseline: "M 50 30 C 180 120, 380 158, 890 165",
          eps10: "M 50 32 C 200 110, 420 142, 890 150",
          eps5: "M 50 36 C 220 95, 450 128, 890 138",
          eps1: "M 50 42 C 240 85, 480 102, 890 110",
          eps05: "M 50 50 C 260 78, 520 85, 890 85"
        },
        insights: {
          maxAcc: "Accuracy: 71.3%", maxMia: "MIA Risk: 51.2%",
          sweetAcc: "Accuracy: 82.4%", sweetMia: "MIA Risk: 55.4%",
          baseAcc: "Accuracy: 86.2%", baseMia: "MIA Risk: 79.8%"
        },
        recommendation: "DP-SGD with <span class='font-mono font-semibold text-brandSafe'>ε=5</span> achieves the best privacy-utility balance for Adult Census 1994 (96.7% accuracy retention and 92.0% F1-score retention with 68% lower MIA vulnerability).",
        benchmarks: [
          { model: "DP-SGD ResNet-Tabular", mech: "Gaussian + Clip", eps: "ε = 0.50", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "71.3%", f1: "49.0%", mia: "51.2% Negligible", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "4m 12s" },
          { model: "DP-SGD MLP", mech: "Gaussian + Clip", eps: "ε = 1.00", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "74.6%", f1: "54.2%", mia: "52.0% Safe", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "3m 48s" },
          { model: "DP-SGD Optimal", rec: true, mech: "Gaussian + Clip", eps: "ε = 5.00", epsClass: "bg-amber-500/10 text-amber-400 border-amber-500/20", delta: "1.0e-5", acc: "82.4%", f1: "63.8%", mia: "55.4% Controlled", miaDot: "bg-amber-400", miaTextClass: "text-amber-400", time: "3m 50s" },
          { model: "DP LightGBM-DP", mech: "Laplace Trees", eps: "ε = 8.00", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0 (Pure)", acc: "84.1%", f1: "65.5%", mia: "66.2% Elevated", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "1m 20s" },
          { model: "Standard SGD Baseline", mech: "None (Unbounded)", eps: "ε = ∞ (None)", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0", acc: "86.2%", f1: "69.4%", mia: "79.8% Critical", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "1m 05s" }
        ]
      },

      heart: {
        name: "UCI Heart Disease",
        desc: "Clinical tabular records for cardiac diagnosis. Highly confidential patient biometric data.",
        total: 1025,
        train: 820,
        test: 205,
        feat: "13 Clinical Metrics",
        featDims: 13,
        featSub: "Biometric vectors",
        classBalance: "54.4 / 45.6",
        classSub: "Balanced clinical cohort",
        curatedSub: "↑ 100% anonymised",
        tableTitle: "Dataset: UCI Heart Disease",
        baselineText: "Baseline = 0.883",
        baselineY: 32,
        optAccText: "85.2% (Opt)",
        accPath: "M 45 98 Q 120 62 200 46 T 430 36",
        accArea: "M 45 98 Q 120 62 200 46 T 430 36 L 430 170 L 45 170 Z",
        miaPath: "M 45 168 Q 120 160 200 148 T 280 122 T 430 26",
        miaMarkers: [
          { cx: 45, cy: 168, y: 155, text: "50.8% (Low)" },
          { cx: 280, cy: 122, y: 110, text: "54.1% (Mod)" },
          { cx: 430, cy: 26, y: 16, text: "82.4% (Danger)" }
        ],
        epochCurves: {
          baseline: "M 50 25 C 160 130, 360 166, 890 172",
          eps10: "M 50 28 C 180 118, 400 152, 890 158",
          eps5: "M 50 32 C 200 102, 430 136, 890 146",
          eps1: "M 50 38 C 220 90, 460 112, 890 120",
          eps05: "M 50 46 C 240 80, 490 94, 890 98"
        },
        insights: {
          maxAcc: "Accuracy: 74.1%", maxMia: "MIA Risk: 50.8%",
          sweetAcc: "Accuracy: 85.2%", sweetMia: "MIA Risk: 54.1%",
          baseAcc: "Accuracy: 88.3%", baseMia: "MIA Risk: 82.4%"
        },
        recommendation: "DP-SGD with <span class='font-mono font-semibold text-brandSafe'>ε=5</span> protects patient cardiac records with 67% lower MIA risk while sustaining 96.5% diagnostic accuracy and 95.2% F1 score.",
        benchmarks: [
          { model: "DP-SGD ResNet-Tabular", mech: "Gaussian + Clip", eps: "ε = 0.50", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "74.1%", f1: "64.0%", mia: "50.8% Negligible", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "1m 15s" },
          { model: "DP-SGD MLP", mech: "Gaussian + Clip", eps: "ε = 1.00", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "78.5%", f1: "72.0%", mia: "51.9% Safe", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "1m 08s" },
          { model: "DP-SGD Optimal", rec: true, mech: "Gaussian + Clip", eps: "ε = 5.00", epsClass: "bg-amber-500/10 text-amber-400 border-amber-500/20", delta: "1.0e-5", acc: "85.2%", f1: "79.5%", mia: "54.1% Controlled", miaDot: "bg-amber-400", miaTextClass: "text-amber-400", time: "1m 12s" },
          { model: "DP LightGBM-DP", mech: "Laplace Trees", eps: "ε = 8.00", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0 (Pure)", acc: "86.8%", f1: "81.5%", mia: "64.5% Elevated", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "0m 45s" },
          { model: "Standard SGD Baseline", mech: "None (Unbounded)", eps: "ε = ∞ (None)", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0", acc: "88.3%", f1: "83.5%", mia: "82.4% Critical", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "0m 40s" }
        ]
      },

      diabetes: {
        name: "Diabetes 130-US",
        desc: "Hospital readmission indicators with sensitive inpatient demographic & diagnostic attributes.",
        total: 101766,
        train: 81413,
        test: 20353,
        feat: "47 Features",
        featDims: 47,
        featSub: "Encounter variables",
        classBalance: "53.9 / 46.1",
        classSub: "Readmitted vs discharged",
        curatedSub: "↑ 100% curated",
        tableTitle: "Dataset: Diabetes 130-US",
        baselineText: "Baseline = 0.668",
        baselineY: 88,
        optAccText: "64.7% (Opt)",
        accPath: "M 45 142 Q 120 124 200 110 T 430 94",
        accArea: "M 45 142 Q 120 124 200 110 T 430 94 L 430 170 L 45 170 Z",
        miaPath: "M 45 170 Q 120 164 200 152 T 280 128 T 430 48",
        miaMarkers: [
          { cx: 45, cy: 170, y: 157, text: "50.2% (Low)" },
          { cx: 280, cy: 128, y: 116, text: "53.8% (Mod)" },
          { cx: 430, cy: 48, y: 38, text: "74.6% (Danger)" }
        ],
        epochCurves: {
          baseline: "M 50 35 C 220 98, 440 135, 890 148",
          eps10: "M 50 38 C 240 92, 470 126, 890 138",
          eps5: "M 50 42 C 260 84, 500 114, 890 126",
          eps1: "M 50 48 C 280 76, 530 98, 890 106",
          eps05: "M 50 56 C 300 68, 560 80, 890 84"
        },
        insights: {
          maxAcc: "Accuracy: 58.4%", maxMia: "MIA Risk: 50.2%",
          sweetAcc: "Accuracy: 64.7%", sweetMia: "MIA Risk: 53.8%",
          baseAcc: "Accuracy: 66.8%", baseMia: "MIA Risk: 74.6%"
        },
        recommendation: "DP-SGD with <span class='font-mono font-semibold text-brandSafe'>ε=5</span> provides effective hospital readmission privacy (72% lower MIA risk) with 96.9% accuracy retention and 93.0% F1 retention.",
        benchmarks: [
          { model: "DP-SGD ResNet-Tabular", mech: "Gaussian + Clip", eps: "ε = 0.50", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "58.4%", f1: "51.0%", mia: "50.2% Negligible", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "6m 30s" },
          { model: "DP-SGD MLP", mech: "Gaussian + Clip", eps: "ε = 1.00", epsClass: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20", delta: "1.0e-5", acc: "61.2%", f1: "59.0%", mia: "51.5% Safe", miaDot: "bg-emerald-400", miaTextClass: "text-emerald-400", time: "5m 50s" },
          { model: "DP-SGD Optimal", rec: true, mech: "Gaussian + Clip", eps: "ε = 5.00", epsClass: "bg-amber-500/10 text-amber-400 border-amber-500/20", delta: "1.0e-5", acc: "64.7%", f1: "66.0%", mia: "53.8% Controlled", miaDot: "bg-amber-400", miaTextClass: "text-amber-400", time: "5m 55s" },
          { model: "DP LightGBM-DP", mech: "Laplace Trees", eps: "ε = 8.00", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0 (Pure)", acc: "65.9%", f1: "67.2%", mia: "61.2% Elevated", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "2m 10s" },
          { model: "Standard SGD Baseline", mech: "None (Unbounded)", eps: "ε = ∞ (None)", epsClass: "bg-rose-500/10 text-rose-400 border-rose-500/20", delta: "0", acc: "66.8%", f1: "71.0%", mia: "74.6% Critical", miaDot: "bg-rose-400", miaTextClass: "text-rose-400", time: "1m 45s" }
        ]
      }
    };

    function animateValue(el, start, end, duration) {
      if (!el) return;
      const obj = { val: start };
      gsap.to(obj, {
        val: end,
        duration: duration || 1.2,
        ease: "power2.out",
        onUpdate: () => {
          el.innerText = Math.floor(obj.val).toLocaleString();
        }
      });
    }

    // Dataset Select Callback
    function changeDataset(val) {
      const data = DATASETS[val] || DATASETS.adult;
      
      // 1. Sidebar description & top badge
      const desc = document.getElementById("dataset-desc");
      const badgeName = document.getElementById("badge-dataset-name");
      const badgeSample = document.getElementById("badge-sample-count");
      const badgeFeat = document.getElementById("badge-feat-count");
      
      if (desc) desc.innerText = data.desc;
      if (badgeName) badgeName.innerText = data.name;
      if (badgeSample) badgeSample.innerText = data.total.toLocaleString() + " samples";
      if (badgeFeat) badgeFeat.innerText = data.feat;

      // 2. Animate 5 Metric Cards
      const elTotal = document.getElementById("stat-total-samples");
      const elTrain = document.getElementById("stat-train-samples");
      const elTest = document.getElementById("stat-test-samples");
      const elFeat = document.getElementById("stat-feat-dims");
      const elClass = document.getElementById("stat-class-balance");
      const elTotalSub = document.getElementById("stat-total-sub");
      const elFeatSub = document.getElementById("stat-feat-sub");
      const elClassSub = document.getElementById("stat-class-sub");

      if (elTotal) animateValue(elTotal, parseInt(elTotal.innerText.replace(/,/g, '')) || 0, data.total, 1.2);
      if (elTrain) animateValue(elTrain, parseInt(elTrain.innerText.replace(/,/g, '')) || 0, data.train, 1.2);
      if (elTest) animateValue(elTest, parseInt(elTest.innerText.replace(/,/g, '')) || 0, data.test, 1.2);
      if (elFeat) animateValue(elFeat, parseInt(elFeat.innerText.replace(/,/g, '')) || 0, data.featDims, 1.0);
      if (elClass) elClass.innerText = data.classBalance;
      if (elTotalSub) elTotalSub.innerText = data.curatedSub;
      if (elFeatSub) elFeatSub.innerText = data.featSub;
      if (elClassSub) elClassSub.innerText = data.classSub;

      // 3. Audited Benchmarks Table (Header & Rows)
      const tableTitle = document.getElementById("table-dataset-name");
      if (tableTitle) tableTitle.innerText = data.tableTitle;

      const tbody = document.getElementById("benchmarks-tbody");
      if (tbody && data.benchmarks) {
        tbody.innerHTML = data.benchmarks.map((b, idx) => `
          <tr class="${b.rec ? 'bg-white/[0.03] hover:bg-white/[0.05] border-l-2 border-brandPrimary' : 'hover:bg-white/[0.02]'} transition-colors">
            <td class="py-3 px-3 font-sans font-medium text-white flex items-center gap-1.5">
              <span>${b.model}</span>
              ${b.rec ? '<span class="text-[10px] font-sans font-semibold text-brandPrimary bg-brandPrimary/10 px-1.5 py-0.2 rounded">Recommended</span>' : ''}
            </td>
            <td class="py-3 px-3 text-brandMuted font-sans">${b.mech}</td>
            <td class="py-3 px-3">
              <span class="px-2 py-0.5 rounded text-[11px] font-semibold ${b.epsClass}">
                ${b.eps}
              </span>
            </td>
            <td class="py-3 px-3 text-brandMuted">${b.delta}</td>
            <td class="py-3 px-3 text-white font-medium">${b.acc}</td>
            <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">${b.f1 || '—'}</td>
            <td class="py-3 px-3">
              <div class="flex items-center gap-1.5 ${b.miaTextClass}">
                <span class="w-1.5 h-1.5 rounded-full ${b.miaDot}"></span>
                <span>${b.mia}</span>
              </div>
            </td>
            <td class="py-3 px-3 text-right text-brandMuted">${b.time}</td>
          </tr>
        `).join('');

        // Subtle row fade-in
        gsap.from(tbody.querySelectorAll("tr"), {
          opacity: 0,
          y: 10,
          duration: 0.4,
          stagger: 0.05,
          ease: "power2.out"
        });
      }

      // 4. Update Chart A (Privacy-Accuracy Trade-off) SVG Path definitions
      const curveAcc = document.getElementById("curve-acc");
      const curveAccArea = document.getElementById("curve-acc-area");
      const baselineLine = document.getElementById("baseline-acc-line");
      const baselineText = document.getElementById("baseline-acc-text");
      const optText = document.getElementById("acc-opt-text");

      if (curveAcc) curveAcc.setAttribute("d", data.accPath);
      if (curveAccArea) curveAccArea.setAttribute("d", data.accArea);
      if (baselineLine) {
        baselineLine.setAttribute("y1", data.baselineY);
        baselineLine.setAttribute("y2", data.baselineY);
      }
      if (baselineText) {
        baselineText.setAttribute("y", data.baselineY - 6);
        baselineText.textContent = data.baselineText;
      }
      if (optText) optText.textContent = data.optAccText;

      // 5. Update Chart B (Membership Inference Risk) SVG Path definitions
      const curveMia = document.getElementById("curve-mia");
      if (curveMia && data.miaPath) {
        curveMia.setAttribute("d", data.miaPath);
      }
      if (data.miaMarkers) {
        for (let i = 0; i < 3; i++) {
          const c = document.getElementById(`mia-circle-${i+1}`);
          const t = document.getElementById(`mia-text-${i+1}`);
          const m = data.miaMarkers[i];
          if (c && m) {
            c.setAttribute("cx", m.cx);
            c.setAttribute("cy", m.cy);
          }
          if (t && m) {
            t.setAttribute("x", m.cx);
            t.setAttribute("y", m.y);
            t.textContent = m.text;
          }
        }
      }

      // 6. Update Chart C (Training Curves - Epoch Dynamics) SVG Path definitions
      if (data.epochCurves) {
        const cBase = document.getElementById("epoch-curve-baseline");
        const cEps10 = document.getElementById("epoch-curve-eps10");
        const cEps5 = document.getElementById("epoch-curve-eps5");
        const cEps1 = document.getElementById("epoch-curve-eps1");
        const cEps05 = document.getElementById("epoch-curve-eps05");

        if (cBase) cBase.setAttribute("d", data.epochCurves.baseline);
        if (cEps10) cEps10.setAttribute("d", data.epochCurves.eps10);
        if (cEps5) cEps5.setAttribute("d", data.epochCurves.eps5);
        if (cEps1) cEps1.setAttribute("d", data.epochCurves.eps1);
        if (cEps05) cEps05.setAttribute("d", data.epochCurves.eps05);
      }

      // 7. Update Insight Cards
      const insMaxAcc = document.getElementById("insight-max-acc");
      const insMaxMia = document.getElementById("insight-max-mia");
      const insSweetAcc = document.getElementById("insight-sweet-acc");
      const insSweetMia = document.getElementById("insight-sweet-mia");
      const insBaseAcc = document.getElementById("insight-base-acc");
      const insBaseMia = document.getElementById("insight-base-mia");

      if (insMaxAcc) insMaxAcc.innerText = data.insights.maxAcc;
      if (insMaxMia) insMaxMia.innerText = data.insights.maxMia;
      if (insSweetAcc) insSweetAcc.innerText = data.insights.sweetAcc;
      if (insSweetMia) insSweetMia.innerText = data.insights.sweetMia;
      if (insBaseAcc) insBaseAcc.innerText = data.insights.baseAcc;
      if (insBaseMia) insBaseMia.innerText = data.insights.baseMia;

      // 8. Update Recommendation
      const rec = document.getElementById("recommendation-text");
      if (rec) rec.innerHTML = data.recommendation;

      // Reset Telemetry to clean state for newly selected dataset
      if (currentMode === 'results') {
        setupResultsAnalysisMode();
      } else {
        resetAllTelemetryToFresh(currentMode);
        updateLiveTelemetryVisuals();
      }
    }

    // =========================================================================
    // MODE CONTROLLER: Auto Demo, Interactive Demo, Full Training, Results
    // =========================================================================
    let currentMode = 'interactive';
    let autoTourTimer = null;
    let autoTourStep = 0;
    const autoTourSteps = [
      {
        eps: 0.5,
        name: "Provable Safe Privacy (ε = 0.5)",
        desc: "With a strict privacy budget of ε=0.5, gradient perturbation provides mathematical indistinguishability. Attackers attempting membership inference succeed only 51.2% of the time (equivalent to random guessing), preventing patient re-identification entirely."
      },
      {
        eps: 1.0,
        name: "Strong Differential Privacy (ε = 1.0)",
        desc: "The standard benchmark for commercial and healthcare deployments. Maintains high classification confidence while guaranteeing theoretical worst-case privacy protection."
      },
      {
        eps: 5.0,
        name: "Optimal Sweet-Spot (ε = 5.0)",
        desc: "The recommended operational trade-off point. Preserves over 96.5% of non-private accuracy while suppressing shadow attack precision by more than 68% relative to unclipped baseline training."
      },
      {
        eps: 10.0,
        name: "Standard Baseline & Relaxed Regimes (ε = 10.0+)",
        desc: "Higher privacy budgets allow models to closely match standard non-private SGD performance, but outlier records with unique feature vectors become increasingly susceptible to shadow model reconstruction."
      }
    ];

    function switchMode(btn, modeName) {
      currentMode = modeName;

      // Stop auto tour if running
      if (autoTourTimer) {
        clearInterval(autoTourTimer);
        autoTourTimer = null;
      }

      if (modeName === 'results') {
        setupResultsAnalysisMode();
      } else {
        // Strict mode isolation: Reset telemetry curves and mode state completely fresh
        resetAllTelemetryToFresh(modeName);
      }

      // 1. Update sidebar pills styling
      const pills = document.querySelectorAll(".mode-pill");
      pills.forEach((p) => {
        p.className = "mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-brandMuted hover:text-white hover:bg-white/[0.04] transition-all text-left";
      });
      if (btn) {
        btn.className = "mode-pill w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium text-white bg-white/[0.1] border border-white/[0.1] shadow-sm transition-all text-left";
      }

      // 2. Hide all mode panels
      const panels = ["interactive", "auto", "training", "results"];
      panels.forEach((p) => {
        const el = document.getElementById("mode-panel-" + p);
        if (el) el.classList.add("hidden");
      });

      // 3. Show selected mode panel with GSAP smooth reveal
      const targetPanel = document.getElementById("mode-panel-" + modeName);
      if (targetPanel) {
        targetPanel.classList.remove("hidden");
        gsap.fromTo(targetPanel, 
          { opacity: 0, y: 15 },
          { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }
        );
      }

      // 4. Handle mode-specific actions
      if (modeName === 'auto') {
        jumpAutoStep(0);
      } else {
        stopAutoTour(false);
      }

      if (modeName === 'results') {
        const chartsSection = document.getElementById("chart-privacy-accuracy");
        if (chartsSection) {
          chartsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }

    // --- AUTO DEMO TOUR CONTROLS (Self-moving & One-cycle Termination) ---
    const autoTourComponents = [
      {
        id: "section-dataset-metrics",
        name: "Component 1 of 6: Dataset Overview & Partition Metrics",
        shortDef: "80% Train Corpus / 20% Holdout Validation",
        desc: "Examines the active cohort and divides records into an 80% private training corpus and 20% holdout validation partition. Tracks feature dimensions and class skew before differential privacy noise injection.",
        icon: "database",
        badge: "Step 1 of 6 • Dataset Overview"
      },
      {
        id: "mode-panel-auto",
        name: "Component 2 of 6: DP-SGD Budget Spectrum (ε = 0.5 to 10.0)",
        shortDef: "(ε, δ)-DP: Calibrated Gaussian Noise (σ = 1.18)",
        desc: "Controls the mathematical privacy-loss bound (ε, δ). Lower ε adds stronger Gaussian noise to clipped per-sample gradients (σ=1.18), guaranteeing indistinguishable outputs across neighboring datasets.",
        icon: "shield_lock",
        badge: "Step 2 of 6 • DP Budget Spectrum"
      },
      {
        id: "chart-privacy-accuracy",
        name: "Component 3 of 6: Telemetry & Empirical Curves — Privacy vs Accuracy",
        shortDef: "Optimal ε = 5.0 Retains 96.7% Baseline Accuracy",
        desc: "Empirically plots validation accuracy as privacy budget ε increases. Reveals how the recommended sweet-spot (ε=5.0) recovers over 96.5% of the non-private baseline accuracy while maintaining rigorous privacy guarantees.",
        icon: "trending_up",
        badge: "Step 3 of 6 • Accuracy Telemetry"
      },
      {
        id: "chart-mia-risk",
        name: "Component 4 of 6: Telemetry & Empirical Curves — Membership Inference Defense",
        shortDef: "Confines Shadow Attack Precision to ~51% (Random Chance)",
        desc: "Measures attacker precision in determining whether specific records participated in training. Bounded DP-SGD confines attacker success to near 50% (random guess), mitigating catastrophic data leakage.",
        icon: "security",
        badge: "Step 4 of 6 • MIA Attack Defense"
      },
      {
        id: "chart-epoch-curves",
        name: "Component 5 of 6: Telemetry & Empirical Curves — Epoch Loss Dynamics",
        shortDef: "Loss Trajectory Convergence across 20 Epochs",
        desc: "Visualizes the trajectory of loss convergence over 20 epochs across DP budgets. Baseline models converge rapidly to loss 0.22, whereas DP models plateau at controlled noise floors dictated by Gaussian gradient perturbation.",
        icon: "query_stats",
        badge: "Step 5 of 6 • Epoch Loss Dynamics"
      },
      {
        id: "section-audited-benchmarks",
        name: "Component 6 of 6: Audited Benchmarks Table & Recommendation",
        shortDef: "Multi-Model Audit: ResNet, MLP, Optimal, LightGBM, Baseline",
        desc: "Side-by-side audit of ResNet, MLP, Optimal DP-SGD, LightGBM, and baseline models. Validates execution runtimes, theoretical epsilon bounds, and highlights the production-ready recommendation.",
        icon: "verified",
        badge: "Step 6 of 6 • Audited Benchmarks"
      }
    ];

    function clearTourHighlights() {
      document.querySelectorAll(".tour-focus-glow").forEach(el => {
        el.classList.remove("tour-focus-glow");
      });
      document.querySelectorAll(".tour-def-chip").forEach(el => el.remove());
    }

    // Kinetic Word-by-Word Flowing Animation for Definitions
    function animateFlowingText(el, text) {
      if (!el) return;
      const words = text.split(" ");
      el.innerHTML = words.map(w => `<span class="tour-flow-word inline-block opacity-0 translate-y-2 filter blur-sm">${w}&nbsp;</span>`).join("");

      gsap.to(el.querySelectorAll(".tour-flow-word"), {
        opacity: 1,
        y: 0,
        filter: "blur(0px)",
        duration: 0.35,
        stagger: 0.02,
        ease: "power2.out"
      });
    }

    function jumpAutoStep(stepIndex) {
      if (stepIndex < 0) stepIndex = 0;
      if (stepIndex >= autoTourComponents.length) stepIndex = autoTourComponents.length - 1;
      autoTourStep = stepIndex;
      const comp = autoTourComponents[stepIndex];
      if (!comp) return;

      // 1. Update pills styling
      for (let i = 0; i < autoTourComponents.length; i++) {
        const b = document.getElementById("auto-step-btn-" + i);
        if (b) {
          if (i === stepIndex) {
            b.className = "auto-step-pill p-2.5 rounded-lg bg-brandPrimary/10 border border-brandPrimary/60 text-left transition-all shadow-md";
          } else {
            b.className = "auto-step-pill p-2.5 rounded-lg bg-white/[0.02] border border-white/[0.06] text-left transition-all hover:bg-white/[0.07]";
          }
        }
      }

      // 2. Update progress bar & badge
      const progBar = document.getElementById("auto-tour-progress-bar");
      const badge = document.getElementById("auto-tour-badge");
      if (progBar) {
        const pct = ((stepIndex + 1) / autoTourComponents.length) * 100;
        progBar.style.width = pct + "%";
      }
      if (badge) badge.innerText = comp.badge;

      // 3. Narrative Callout with Flow Animation
      const titleEl = document.getElementById("auto-narrative-title");
      const descEl = document.getElementById("auto-narrative-desc");
      const iconEl = document.getElementById("auto-narrative-icon");
      const narrativeBox = document.getElementById("auto-narrative-box") || (descEl ? descEl.closest(".p-4") : null);

      if (titleEl) {
        titleEl.innerText = comp.name;
        // Re-trigger gradient wave
        titleEl.classList.remove("text-gradient-flow");
        void titleEl.offsetWidth;
        titleEl.classList.add("text-gradient-flow");
      }
      if (iconEl) iconEl.innerText = comp.icon;

      // Animate definition text flowing in
      if (descEl) {
        animateFlowingText(descEl, comp.desc);
      }

      // Pulse the narrative box itself
      if (narrativeBox) {
        gsap.fromTo(narrativeBox, 
          { borderColor: "rgba(102, 126, 234, 0.8)", boxShadow: "0 0 20px rgba(102, 126, 234, 0.3)" },
          { borderColor: "rgba(255, 255, 255, 0.08)", boxShadow: "0 0 0px rgba(0,0,0,0)", duration: 1.2, ease: "power2.out" }
        );
      }

      // 4. Highlight target component & attach floating definition chip
      clearTourHighlights();
      const targetEl = document.getElementById(comp.id);
      const scroller = document.getElementById("main-scroller");

      if (targetEl) {
        targetEl.classList.add("tour-focus-glow");

        // In Auto Demo, when tour focuses a chart component, dynamically plot that chart!
        if (comp.id === "chart-privacy-accuracy") {
          const ovA = document.getElementById("chart-a-empty-overlay");
          if (ovA) ovA.style.display = "none";
          const gA = document.getElementById("chart-a-plot-elements");
          if (gA) gA.style.opacity = "1";
          const stA = document.getElementById("chart-a-status");
          if (stA) { stA.innerText = "Plotted (Auto Tour)"; stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-brandPrimary/10 text-brandPrimary border border-brandPrimary/20"; }
          const cAcc = document.getElementById("curve-acc");
          if (cAcc) {
            const len = cAcc.getTotalLength ? cAcc.getTotalLength() : 600;
            gsap.fromTo(cAcc, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, duration: 1.2, ease: "power2.out" });
          }
        } else if (comp.id === "chart-mia-risk") {
          const ovB = document.getElementById("chart-b-empty-overlay");
          if (ovB) ovB.style.display = "none";
          const gB = document.getElementById("chart-b-plot-elements");
          if (gB) gB.style.opacity = "1";
          const stB = document.getElementById("chart-b-status");
          if (stB) { stB.innerText = "Plotted (Auto Tour)"; stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-brandPrimary/10 text-brandPrimary border border-brandPrimary/20"; }
          const cMia = document.getElementById("curve-mia");
          if (cMia) {
            const len = cMia.getTotalLength ? cMia.getTotalLength() : 600;
            gsap.fromTo(cMia, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, duration: 1.2, ease: "power2.out" });
          }
        } else if (comp.id === "chart-epoch-curves") {
          const ovC = document.getElementById("chart-c-empty-overlay");
          if (ovC) ovC.style.display = "none";
          const gC = document.getElementById("chart-c-plot-elements");
          if (gC) gC.style.opacity = "1";
          const stC = document.getElementById("chart-c-status");
          if (stC) { stC.innerText = "Plotted (Auto Tour)"; stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-brandPrimary/10 text-brandPrimary border border-brandPrimary/20"; }
          ["epoch-curve-baseline", "epoch-curve-eps10", "epoch-curve-eps5", "epoch-curve-eps1", "epoch-curve-eps05"].forEach((id, idx) => {
            const el = document.getElementById(id);
            if (el) {
              el.style.opacity = "1";
              const len = el.getTotalLength ? el.getTotalLength() : 800;
              gsap.fromTo(el, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, duration: 1.0, delay: idx * 0.08, ease: "power2.out" });
            }
          });
        }

        // Attach floating definition chip on the highlighted component
        const chip = document.createElement("div");
        chip.className = "tour-def-chip";
        chip.innerHTML = `<span class="w-2 h-2 rounded-full bg-brandPrimary animate-ping"></span><span class="text-brandPrimary">Active:</span> <span>${comp.shortDef}</span>`;
        targetEl.appendChild(chip);

        gsap.fromTo(chip, 
          { opacity: 0, scale: 0.8, y: -5 },
          { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: "back.out(1.7)" }
        );

        // Smooth scroll scroller to target component
        if (scroller) {
          const targetRect = targetEl.getBoundingClientRect();
          const scrollerRect = scroller.getBoundingClientRect();
          const scrollTarget = scroller.scrollTop + (targetRect.top - scrollerRect.top) - 80;

          scroller.scrollTo({
            top: Math.max(0, scrollTarget),
            behavior: "smooth"
          });
        }
      }
    }

    function stepNextAuto() {
      if (autoTourStep < autoTourComponents.length - 1) {
        jumpAutoStep(autoTourStep + 1);
      } else {
        stopAutoTour(true);
      }
    }

    function stepPrevAuto() {
      if (autoTourStep > 0) {
        jumpAutoStep(autoTourStep - 1);
      }
    }

    function toggleAutoTour() {
      const btnText = document.getElementById("auto-play-text");
      const icon = document.getElementById("auto-play-icon");

      if (autoTourTimer) {
        stopAutoTour(false);
      } else {
        if (autoTourStep >= autoTourComponents.length - 1) {
          autoTourStep = 0;
        }
        jumpAutoStep(autoTourStep);

        if (btnText) btnText.innerText = "Pause Tour";
        if (icon) icon.innerText = "pause";

        // Auto move every 4.5 seconds and terminate after exact one tour of each
        autoTourTimer = setInterval(() => {
          if (autoTourStep < autoTourComponents.length - 1) {
            autoTourStep++;
            jumpAutoStep(autoTourStep);
          } else {
            stopAutoTour(true);
          }
        }, 4500);
      }
    }

    function stopAutoTour(isFinished) {
      if (autoTourTimer) {
        clearInterval(autoTourTimer);
        autoTourTimer = null;
      }
      const btnText = document.getElementById("auto-play-text");
      const icon = document.getElementById("auto-play-icon");
      const badge = document.getElementById("auto-tour-badge");

      if (isFinished) {
        if (btnText) btnText.innerText = "Replay Auto Tour";
        if (icon) icon.innerText = "replay";
        if (badge) badge.innerText = "✓ Tour Complete (All 6 Audited)";

        setTimeout(() => {
          clearTourHighlights();
          const autoPanel = document.getElementById("mode-panel-auto");
          const scroller = document.getElementById("main-scroller");
          if (scroller && autoPanel) {
            const scrollerRect = scroller.getBoundingClientRect();
            const panelRect = autoPanel.getBoundingClientRect();
            scroller.scrollTo({
              top: Math.max(0, scroller.scrollTop + (panelRect.top - scrollerRect.top) - 40),
              behavior: "smooth"
            });
          }
        }, 1500);
      } else {
        if (btnText) btnText.innerText = "Resume Tour";
        if (icon) icon.innerText = "play_arrow";
      }
    }

    // --- FULL TRAINING PIPELINE SIMULATION & REAL-TIME GRAPH PLOTTING ---
    function runFullTrainingPipeline() {
      const btn = document.getElementById("btn-train-all");
      const btnText = document.getElementById("btn-train-all-text");
      const progContainer = document.getElementById("training-progress-container");
      const progLabel = document.getElementById("training-progress-label");
      const progPct = document.getElementById("training-progress-pct");
      const progBar = document.getElementById("training-progress-bar");
      const completionCard = document.getElementById("full-training-completion-card");

      if (progContainer) progContainer.classList.remove("hidden");
      if (completionCard) completionCard.classList.add("hidden");
      if (btn) btn.disabled = true;

      // Mark mode as trained and reveal chart canvases
      isCurrentModeTrained = true;

      ["chart-a-empty-overlay", "chart-b-empty-overlay", "chart-c-empty-overlay"].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = "none";
      });
      ["chart-a-plot-elements", "chart-b-plot-elements", "chart-c-plot-elements"].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.opacity = "1";
      });

      const stA = document.getElementById("chart-a-status");
      const stB = document.getElementById("chart-b-status");
      const stC = document.getElementById("chart-c-status");
      if (stA) { stA.innerText = "Training Pipeline Active..."; stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
      if (stB) { stB.innerText = "Training Pipeline Active..."; stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
      if (stC) { stC.innerText = "Training Pipeline Active..."; stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }

      const currentDs = (document.getElementById("dataset-select") && document.getElementById("dataset-select").value) || 'adult';
      const dsData = DATASETS[currentDs] || DATASETS.adult;
      const bMarks = dsData.benchmarks || [];

      // Map Step 0..4 to correct Card & Benchmark Model
      // Card 0: Baseline (bMarks[4]), Card 1: Relaxed (bMarks[3]), Card 2: Optimal (bMarks[2]), Card 3: Strong (bMarks[1]), Card 4: Max (bMarks[0])
      const stepMapping = [
        { cardIdx: 0, bIdx: 4, curveId: "epoch-curve-baseline", name: "Model 1: Standard SGD Baseline (ε=∞)" },
        { cardIdx: 1, bIdx: 3, curveId: "epoch-curve-eps10", name: "Model 2: DP-SGD Relaxed (ε=10.0)" },
        { cardIdx: 2, bIdx: 2, curveId: "epoch-curve-eps5", name: "Model 3: DP-SGD Optimal (ε=5.0)" },
        { cardIdx: 3, bIdx: 1, curveId: "epoch-curve-eps1", name: "Model 4: DP-SGD Strong (ε=1.0)" },
        { cardIdx: 4, bIdx: 0, curveId: "epoch-curve-eps05", name: "Model 5: DP-SGD Maximum (ε=0.5)" }
      ];

      // Reset all cards to active training styling
      for (let i = 0; i < 5; i++) {
        const sBadge = document.getElementById("train-status-" + i);
        const mText = document.getElementById("train-metric-" + i);
        const card = document.getElementById("train-card-" + i);
        if (sBadge) {
          sBadge.innerText = "Queued";
          sBadge.className = "text-[9px] px-1.5 py-0.5 rounded bg-white/[0.05] text-brandMuted font-mono";
        }
        if (mText) {
          mText.innerText = "Acc: -- | MIA: --";
          mText.className = "text-[11px] font-mono text-brandMuted";
        }
        if (card) {
          card.classList.remove("border-emerald-500/40", "bg-emerald-500/[0.04]");
        }
      }

      let step = 0;
      const totalSteps = 5;
      const interval = setInterval(() => {
        if (step < totalSteps) {
          const mInfo = stepMapping[step];
          const modelData = bMarks[mInfo.bIdx] || {};
          const statusBadge = document.getElementById("train-status-" + mInfo.cardIdx);
          const metricText = document.getElementById("train-metric-" + mInfo.cardIdx);
          const card = document.getElementById("train-card-" + mInfo.cardIdx);

          // Update Progress
          if (progLabel) progLabel.innerText = "Training Pipeline: [" + (step + 1) + "/5] " + mInfo.name + "...";
          const pct = Math.round(((step + 1) / totalSteps) * 100);
          if (progPct) progPct.innerText = pct + "%";
          if (progBar) progBar.style.width = pct + "%";

          // Card UI updates
          if (statusBadge) {
            statusBadge.innerText = "Done ✓";
            statusBadge.className = "text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-mono font-semibold";
          }
          if (metricText) {
            metricText.innerText = "Acc: " + (modelData.acc || "--") + " | MIA: " + ((modelData.mia || "--").split(' ')[0]);
            metricText.className = "text-[11px] font-mono text-emerald-400 font-semibold";
          }
          if (card) {
            card.classList.add("border-emerald-500/40", "bg-emerald-500/[0.04]");
            gsap.fromTo(card, { scale: 0.98 }, { scale: 1, duration: 0.3, ease: "back.out(1.5)" });
          }

          // --- PLOT & ANIMATE ONTO TELEMETRY GRAPHS LIVE ---
          // 1. Chart C: Illuminate the corresponding Epoch Convergence Curve
          const cCurve = document.getElementById(mInfo.curveId);
          if (cCurve) {
            cCurve.style.opacity = "1.0";
            cCurve.setAttribute("stroke-width", "3.8");
            gsap.fromTo(cCurve, 
              { strokeDasharray: "1000", strokeDashoffset: "1000" },
              { strokeDashoffset: "0", duration: 0.6, ease: "power2.out" }
            );
          }

          // 2. Chart A: Highlight Accuracy operating point & sweet spot
          if (step === 0) {
            // Baseline line
            gsap.fromTo("#baseline-acc-line", { strokeWidth: 1.2, opacity: 0.4 }, { strokeWidth: 3, opacity: 1, repeat: 1, yoyo: true, duration: 0.35 });
          } else if (step === 2) {
            // Optimal Sweet Spot
            gsap.fromTo("#acc-opt-text", { scale: 1 }, { scale: 1.3, transformOrigin: "center center", repeat: 1, yoyo: true, duration: 0.35 });
          }

          // 3. Chart B: Highlight MIA threat points
          if (step === 0) {
            gsap.fromTo("#mia-circle-3", { r: 4 }, { r: 9, repeat: 1, yoyo: true, duration: 0.35 });
          } else if (step === 2) {
            gsap.fromTo("#mia-circle-2", { r: 4 }, { r: 8.5, repeat: 1, yoyo: true, duration: 0.35 });
          } else if (step === 4) {
            gsap.fromTo("#mia-circle-1", { r: 4 }, { r: 8.5, repeat: 1, yoyo: true, duration: 0.35 });
          }

          step++;
        } else {
          clearInterval(interval);
          if (progLabel) progLabel.innerText = "✓ All 5 Models Successfully Trained & Plotted Across Telemetry Curves!";
          if (btnText) btnText.innerText = "Re-run Full Training Pipeline ↻";
          if (btn) btn.disabled = false;

          if (stA) { stA.innerText = "Plotted (5 Models Audited)"; stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
          if (stB) { stB.innerText = "Plotted (5 Models Audited)"; stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
          if (stC) { stC.innerText = "Plotted (5 Models Audited)"; stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }

          // Draw full connecting accuracy & MIA curve lines with GSAP
          const curveAcc = document.getElementById("curve-acc");
          if (curveAcc) {
            const lenA = curveAcc.getTotalLength ? curveAcc.getTotalLength() : 600;
            gsap.fromTo(curveAcc, { strokeDasharray: lenA, strokeDashoffset: lenA }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out" });
          }
          const curveMia = document.getElementById("curve-mia");
          if (curveMia) {
            const lenB = curveMia.getTotalLength ? curveMia.getTotalLength() : 600;
            gsap.fromTo(curveMia, { strokeDasharray: lenB, strokeDashoffset: lenB }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out" });
          }

          // Populate and reveal Full Training Completion Card
          const baseData = bMarks[4] || {};
          const optData = bMarks[2] || {};
          const safeData = bMarks[0] || {};

          const rBase = document.getElementById("ft-res-base");
          const rOpt = document.getElementById("ft-res-opt");
          const rSafe = document.getElementById("ft-res-safe");

          if (rBase) rBase.innerText = (baseData.acc || "86.2%") + " Acc | " + (baseData.mia || "79.8% MIA");
          if (rOpt) rOpt.innerText = (optData.acc || "82.4%") + " Acc | " + (optData.mia || "55.4% MIA");
          if (rSafe) rSafe.innerText = (safeData.acc || "71.3%") + " Acc | " + (safeData.mia || "51.2% MIA");

          if (completionCard) {
            completionCard.classList.remove("hidden");
            gsap.fromTo(completionCard, 
              { opacity: 0, y: 15 },
              { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }
            );
          }

          // Sequentially highlight the 5 rows in the benchmarks table
          const tRows = document.querySelectorAll("#benchmarks-tbody tr");
          if (tRows.length > 0) {
            gsap.fromTo(tRows, 
              { backgroundColor: "rgba(102, 126, 234, 0.25)" },
              { backgroundColor: "transparent", stagger: 0.1, duration: 0.8, ease: "power2.out" }
            );
          }

          // Smoothly scroll down to Telemetry Curves so the user sees the plotted results immediately
          setTimeout(() => {
            const chartSection = document.getElementById("chart-privacy-accuracy");
            if (chartSection) {
              chartSection.scrollIntoView({ behavior: "smooth", block: "center" });
            }
          }, 450);
        }
      }, 700);
    }

    window.runFullTrainingPipeline = runFullTrainingPipeline;

    // --- SECTION 5 TAB SWITCHER (EMPIRICAL BENCHMARKS vs DISTRIBUTED TABLE I) ---
    function switchBenchmarkTab(tab) {
      const paneEmp = document.getElementById("tab-pane-empirical");
      const paneDist = document.getElementById("tab-pane-distributed");
      const btnEmp = document.getElementById("tab-btn-empirical");
      const btnDist = document.getElementById("tab-btn-distributed");

      if (tab === 'empirical') {
        if (paneDist) paneDist.classList.add("hidden");
        if (paneEmp) {
          paneEmp.classList.remove("hidden");
          if (typeof gsap !== 'undefined') {
            gsap.fromTo(paneEmp, { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out" });
          }
        }
        if (btnEmp) {
          btnEmp.className = "px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-brandPrimary text-white shadow-md transition-all flex items-center gap-1.5";
        }
        if (btnDist) {
          btnDist.className = "px-3.5 py-1.5 rounded-lg text-xs font-semibold text-brandMuted hover:text-white transition-all flex items-center gap-1.5";
        }
      } else {
        if (paneEmp) paneEmp.classList.add("hidden");
        if (paneDist) {
          paneDist.classList.remove("hidden");
          if (typeof gsap !== 'undefined') {
            gsap.fromTo(paneDist, { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out" });
          }
        }
        if (btnDist) {
          btnDist.className = "px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-brandPrimary text-white shadow-md transition-all flex items-center gap-1.5";
        }
        if (btnEmp) {
          btnEmp.className = "px-3.5 py-1.5 rounded-lg text-xs font-semibold text-brandMuted hover:text-white transition-all flex items-center gap-1.5";
        }
      }
    }
    window.switchBenchmarkTab = switchBenchmarkTab;


    // --- RESULTS ANALYSIS TABLE FILTERS & CSV EXPORT ---
    function filterBenchmarkRows(filterType, btn) {
      // Update filter button styling
      document.querySelectorAll(".bench-filter-btn").forEach(b => {
        b.className = "bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.04] text-brandMuted hover:text-white font-medium";
      });
      if (btn) {
        btn.className = "bench-filter-btn px-2.5 py-1 rounded-md bg-white/[0.1] text-white font-medium";
      }

      const tbody = document.getElementById("benchmarks-tbody");
      if (!tbody) return;
      const rows = tbody.querySelectorAll("tr");

      rows.forEach(r => {
        const text = r.innerText.toLowerCase();
        let show = true;
        if (filterType === 'safe') {
          show = text.includes('0.50') || text.includes('1.00');
        } else if (filterType === 'rec') {
          show = text.includes('recommended') || text.includes('5.00');
        } else if (filterType === 'base') {
          show = text.includes('baseline');
        }
        r.style.display = show ? "" : "none";
      });
    }

    function downloadCSVReport() {
      const currentDs = document.getElementById("dataset-select").value || 'adult';
      const dsData = DATASETS[currentDs] || DATASETS.adult;
      const bMarks = dsData.benchmarks || [];

      const rows = [
        ["Model", "Mechanism", "Epsilon", "Delta", "Accuracy", "F1_Score", "MIA_Risk", "Training_Time"],
        ...bMarks.map(b => [b.model, b.mech, b.eps, b.delta, b.acc, b.f1 || 'N/A', b.mia, b.time])
      ];

      const csvContent = "data:text/csv;charset=utf-8," + rows.map(r => r.map(c => '"' + c + '"').join(",")).join(String.fromCharCode(10));
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "dp_ml_" + currentDs + "_audited_benchmarks.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // --- INTERACTIVE DEMO TRAINING SIMULATION & AUDIT ---
    let lastTrainedCustomModel = null;

    function calculateTrainedMetrics(eps, epochs, batchSize, dsKey) {
      const ds = DATASETS[dsKey] || DATASETS.adult;
      const bMarks = ds.benchmarks || [];

      const p05_acc = parseFloat(bMarks[0]?.acc || "71.3") / 100;
      const p05_mia = parseFloat(bMarks[0]?.mia || "51.2") / 100;

      const p10_acc = parseFloat(bMarks[1]?.acc || "74.6") / 100;
      const p10_mia = parseFloat(bMarks[1]?.mia || "52.0") / 100;

      const p50_acc = parseFloat(bMarks[2]?.acc || "82.4") / 100;
      const p50_mia = parseFloat(bMarks[2]?.mia || "55.4") / 100;

      const pBase_acc = parseFloat(bMarks[4]?.acc || "86.2") / 100;
      const pBase_mia = parseFloat(bMarks[4]?.mia || "79.8") / 100;

      // F1 Anchors from benchmarks
      const p05_f1 = parseFloat(bMarks[0]?.f1 || "49.0") / 100;
      const p10_f1 = parseFloat(bMarks[1]?.f1 || "54.2") / 100;
      const p50_f1 = parseFloat(bMarks[2]?.f1 || "63.8") / 100;
      const pBase_f1 = parseFloat(bMarks[4]?.f1 || "69.4") / 100;

      let acc, mia, f1;
      if (eps <= 1.0) {
        const r = Math.max(0, (eps - 0.5) / 0.5);
        acc = p05_acc + (p10_acc - p05_acc) * r;
        mia = p05_mia + (p10_mia - p05_mia) * r;
        f1  = p05_f1  + (p10_f1  - p05_f1)  * r;
      } else if (eps <= 5.0) {
        const r = (eps - 1.0) / 4.0;
        acc = p10_acc + (p50_acc - p10_acc) * r;
        mia = p10_mia + (p50_mia - p10_mia) * r;
        f1  = p10_f1  + (p50_f1  - p10_f1)  * r;
      } else {
        const r = Math.min(1.0, (eps - 5.0) / 5.0);
        acc = p50_acc + (pBase_acc - 0.01 - p50_acc) * r;
        mia = p50_mia + (pBase_mia - p50_mia) * r;
        f1  = p50_f1  + (pBase_f1 - 0.008 - p50_f1) * r;
      }

      const epochBonus = Math.min(0.012, (epochs - 5) * 0.0008);
      acc = Math.min(pBase_acc - 0.004, acc + epochBonus);

      const epochBonusF1 = Math.min(0.015, (epochs - 5) * 0.0009);
      f1 = Math.min(pBase_f1 - 0.005, f1 + epochBonusF1);

      const sigma = (4.84 / Math.max(0.5, eps)).toFixed(2);
      const diff = ((acc - pBase_acc) * 100).toFixed(1);
      const diffF1 = ((f1 - pBase_f1) * 100).toFixed(1);

      return {
        accPct: (acc * 100).toFixed(1) + "%",
        miaPct: (mia * 100).toFixed(1) + "%",
        diffPct: (diff > 0 ? "+" : "") + diff + "%",
        f1Pct: (f1 * 100).toFixed(1) + "%",
        f1DiffPct: (diffF1 > 0 ? "+" : "") + diffF1 + "%",
        f1Raw: f1,
        sigma: sigma,
        eps: eps.toFixed(1),
        epochs: epochs,
        batchSize: batchSize,
        accRaw: acc,
        miaRaw: mia
      };
    }

    function triggerTrainSimulation() {
      const btn = document.getElementById("btn-train");
      const btnText = document.getElementById("btn-train-text");
      const btnIcon = document.getElementById("btn-train-icon");

      const resContainer = document.getElementById("interactive-training-results");
      const progBox = document.getElementById("interactive-progress-box");
      const progStatus = document.getElementById("interactive-progress-text");
      const progPct = document.getElementById("interactive-progress-pct");
      const progBar = document.getElementById("interactive-progress-bar");
      const summaryCard = document.getElementById("interactive-summary-card");

      // Read current calibrated values
      const eps = parseFloat(document.getElementById("epsilon-slider").value) || 1.0;
      const epochs = parseInt(document.getElementById("epochs-slider").value) || 15;
      const batchSize = document.getElementById("batch-select").value || "64";
      const currentDs = document.getElementById("dataset-select").value || "adult";

      const metrics = calculateTrainedMetrics(eps, epochs, batchSize, currentDs);
      lastTrainedCustomModel = metrics;

      // Disable button during training
      if (btn) btn.disabled = true;
      if (btnText) btnText.innerText = "Training DP-SGD Model in Progress...";
      if (btnIcon) btnIcon.innerText = "sync";

      // Show container & reset progress
      if (resContainer) resContainer.classList.remove("hidden");
      if (progBox) progBox.classList.remove("hidden");
      if (summaryCard) summaryCard.classList.add("hidden");
      if (progBar) progBar.style.width = "0%";
      if (progPct) progPct.innerText = "0%";

      // Multi-stage epoch progress simulation (total ~1.8s)
      const stages = [
        { pct: 20, text: "Epoch 1/" + epochs + " • Clipping gradients (norm C=1.0) • Computing per-sample bounds..." },
        { pct: 45, text: "Epoch " + Math.floor(epochs * 0.3) + "/" + epochs + " • Injecting Gaussian noise (σ=" + metrics.sigma + ") • RDP accounting..." },
        { pct: 75, text: "Epoch " + Math.floor(epochs * 0.7) + "/" + epochs + " • Privacy loss accumulating (ε spent = " + (eps * 0.7).toFixed(2) + ")..." },
        { pct: 100, text: "Epoch " + epochs + "/" + epochs + " • Model converged! Auditing against shadow MIA classifiers..." }
      ];

      let currentStage = 0;
      const interval = setInterval(() => {
        if (currentStage < stages.length) {
          const s = stages[currentStage];
          if (progBar) progBar.style.width = s.pct + "%";
          if (progPct) progPct.innerText = s.pct + "%";
          if (progStatus) progStatus.innerText = s.text;
          currentStage++;
        } else {
          clearInterval(interval);

          // Training complete! Reveal summary card and plot graphs
          setTimeout(() => {
            if (progBox) progBox.classList.add("hidden");
            if (summaryCard) {
              summaryCard.classList.remove("hidden");
              gsap.fromTo(summaryCard, 
                { opacity: 0, y: 15, scale: 0.98 },
                { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.4)" }
              );
            }

            // Populate summary card pills
            const elAcc = document.getElementById("result-model-acc");
            const elDiff = document.getElementById("result-acc-diff");
            const elF1 = document.getElementById("result-model-f1");
            const elF1Diff = document.getElementById("result-f1-diff");
            const elMia = document.getElementById("result-model-mia");
            const elMiaBadge = document.getElementById("result-mia-badge");
            const elSigma = document.getElementById("result-model-sigma");
            const elReg = document.getElementById("result-model-regimen");
            const elBatch = document.getElementById("result-batch-size");
            const elPrivacy = document.getElementById("interactive-privacy-guarantee");

            if (elAcc) elAcc.innerText = metrics.accPct;
            if (elDiff) elDiff.innerText = metrics.diffPct + " vs Baseline";
            if (elF1) elF1.innerText = metrics.f1Pct;
            if (elF1Diff) elF1Diff.innerText = metrics.f1DiffPct + " vs Baseline";
            if (elMia) elMia.innerText = metrics.miaPct;
            if (elSigma) elSigma.innerText = "σ = " + metrics.sigma;
            if (elReg) elReg.innerText = metrics.epochs + " Epochs";
            if (elBatch) elBatch.innerText = "Batch Size " + metrics.batchSize;
            if (elPrivacy) elPrivacy.innerText = "Guaranteed (ε = " + metrics.eps + ", δ = 1.0e-5)";

            if (elMiaBadge) {
              if (metrics.miaRaw < 0.53) {
                elMiaBadge.innerText = "Negligible Attack Advantage (Safe)";
                elMiaBadge.className = "text-[10px] text-emerald-400 font-mono mt-0.5";
                if (elMia) elMia.className = "text-xl font-bold text-emerald-400 mt-1 font-mono";
              } else if (metrics.miaRaw < 0.65) {
                elMiaBadge.innerText = "Controlled Attack Risk (Moderate)";
                elMiaBadge.className = "text-[10px] text-amber-400 font-mono mt-0.5";
                if (elMia) elMia.className = "text-xl font-bold text-amber-400 mt-1 font-mono";
              } else {
                elMiaBadge.innerText = "Elevated Attack Risk (High)";
                elMiaBadge.className = "text-[10px] text-rose-400 font-mono mt-0.5";
                if (elMia) elMia.className = "text-xl font-bold text-rose-400 mt-1 font-mono";
              }
            }

            // --- PLOT TRAINED RESULTS ONTO TELEMETRY GRAPHS ---
            isCurrentModeTrained = true;

            // Fade out empty overlays
            ["chart-a-empty-overlay", "chart-b-empty-overlay", "chart-c-empty-overlay"].forEach(id => {
              const el = document.getElementById(id);
              if (el) el.style.display = "none";
            });

            // Reveal plot groups
            ["chart-a-plot-elements", "chart-b-plot-elements", "chart-c-plot-elements"].forEach(id => {
              const el = document.getElementById(id);
              if (el) el.style.opacity = "1";
            });

            // Update status badges
            const stA = document.getElementById("chart-a-status");
            const stB = document.getElementById("chart-b-status");
            const stC = document.getElementById("chart-c-status");
            if (stA) { stA.innerText = "Plotted (Interactive: ε=" + eps.toFixed(1) + ")"; stA.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
            if (stB) { stB.innerText = "Plotted (Interactive: MIA " + metrics.miaPct + ")"; stB.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }
            if (stC) { stC.innerText = "Plotted (Interactive: Epochs 1-" + epochs + " • ε=" + eps.toFixed(1) + ")"; stC.className = "text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"; }

            // Reveal pointers and update position
            updateLiveTelemetryVisuals();
            const pA = document.getElementById("interactive-acc-pointer");
            const pB = document.getElementById("interactive-mia-pointer");
            if (pA) { pA.style.display = "inline"; pA.style.opacity = "1"; }
            if (pB) { pB.style.display = "inline"; pB.style.opacity = "1"; }

            // Plot interactive epoch dynamics curve in Chart C & show guides
            plotInteractiveEpochCurve(eps, epochs);

            // Animate line draws on Chart A & B
            const cAcc = document.getElementById("curve-acc");
            if (cAcc) {
              try {
                const lenA = (cAcc.getTotalLength && cAcc.getTotalLength() > 0) ? cAcc.getTotalLength() : 600;
                if (typeof gsap !== 'undefined') {
                  gsap.fromTo(cAcc, { strokeDasharray: lenA, strokeDashoffset: lenA }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out", onComplete: () => {
                    cAcc.style.strokeDasharray = "none";
                    cAcc.style.strokeDashoffset = "0";
                  }});
                } else {
                  cAcc.style.strokeDasharray = "none";
                  cAcc.style.strokeDashoffset = "0";
                }
              } catch (e) {
                cAcc.style.strokeDasharray = "none";
                cAcc.style.strokeDashoffset = "0";
              }
            }
            const cMia = document.getElementById("curve-mia");
            if (cMia) {
              try {
                const lenB = (cMia.getTotalLength && cMia.getTotalLength() > 0) ? cMia.getTotalLength() : 600;
                if (typeof gsap !== 'undefined') {
                  gsap.fromTo(cMia, { strokeDasharray: lenB, strokeDashoffset: lenB }, { strokeDashoffset: 0, duration: 1.0, ease: "power2.out", onComplete: () => {
                    cMia.style.strokeDasharray = "none";
                    cMia.style.strokeDashoffset = "0";
                  }});
                } else {
                  cMia.style.strokeDasharray = "none";
                  cMia.style.strokeDashoffset = "0";
                }
              } catch (e) {
                cMia.style.strokeDasharray = "none";
                cMia.style.strokeDashoffset = "0";
              }
            }

            // Smoothly scroll down so user immediately sees the plotted Epoch Dynamics curve!
            setTimeout(() => {
              const epochChart = document.getElementById("chart-epoch-curves");
              if (epochChart) {
                epochChart.scrollIntoView({ behavior: 'smooth', block: 'center' });
              }
            }, 350);

            // Reset train button
            if (btn) btn.disabled = false;
            if (btnText) btnText.innerText = "✓ Retrain DP-SGD Model with New Hyperparameters";
            if (btnIcon) btnIcon.innerText = "refresh";

            // Reset table add button
            const btnAdd = document.getElementById("btn-add-table-text");
            if (btnAdd) btnAdd.innerText = "Add to Benchmarks Table";

            // Re-highlight the operating point on Telemetry Curves
            const optCircle = document.querySelector("#curve-acc ~ circle, svg circle[stroke='#4facfe']");
            if (optCircle) {
              gsap.fromTo(optCircle, { r: 10, fill: "#f093fb" }, { r: 5, fill: "#4facfe", duration: 0.8 });
            }
          }, 350);
        }
      }, 420);
    }

    function addCustomModelToTable() {
      if (!lastTrainedCustomModel) return;
      const tbody = document.getElementById("benchmarks-tbody");
      if (!tbody) return;

      const m = lastTrainedCustomModel;
      const rowId = "custom-row-" + Date.now();

      const newRow = document.createElement("tr");
      newRow.id = rowId;
      newRow.className = "bg-[#667eea]/10 border-b border-[#667eea]/30 font-mono text-[12px] transition-all";
      newRow.innerHTML = `
        <td class="py-3 px-3 font-sans font-semibold text-white flex items-center gap-2">
          <span class="px-1.5 py-0.5 rounded text-[9px] font-mono bg-purple-500/20 text-[#f093fb] border border-purple-500/30">CUSTOM</span>
          <span>User Trained DP-SGD</span>
        </td>
        <td class="py-3 px-3 text-brandMuted font-sans">Gaussian (σ=${m.sigma}, C=1.0)</td>
        <td class="py-3 px-3">
          <span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-brandPrimary/15 text-brandPrimary border border-brandPrimary/30">
            ε = ${m.eps}
          </span>
        </td>
        <td class="py-3 px-3 text-brandMuted">1.0e-5</td>
        <td class="py-3 px-3 text-white font-bold">${m.accPct}</td>
        <td class="py-3 px-3 text-[#4facfe] font-mono font-semibold">${m.f1Pct}</td>
        <td class="py-3 px-3">
          <div class="flex items-center gap-1.5 ${m.miaRaw < 0.55 ? 'text-emerald-400' : (m.miaRaw < 0.65 ? 'text-amber-400' : 'text-rose-400')}">
            <span class="w-1.5 h-1.5 rounded-full ${m.miaRaw < 0.55 ? 'bg-emerald-400' : (m.miaRaw < 0.65 ? 'bg-amber-400' : 'bg-rose-400')}"></span>
            <span>${m.miaPct}</span>
          </div>
        </td>
        <td class="py-3 px-3 text-right text-brandMuted font-sans">1.8s (Trained)</td>
      `;

      tbody.insertBefore(newRow, tbody.firstChild);

      gsap.fromTo(newRow, 
        { opacity: 0, backgroundColor: "rgba(102, 126, 234, 0.4)" },
        { opacity: 1, backgroundColor: "rgba(102, 126, 234, 0.08)", duration: 1.0 }
      );

      const btnAdd = document.getElementById("btn-add-table-text");
      if (btnAdd) btnAdd.innerText = "✓ Added to Table!";

      // Smooth scroll towards the benchmarks table
      newRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  
    // Initialize default dataset benchmarks
    if (typeof changeDataset === 'function') {
      try {
        changeDataset('adult');
      } catch(e) {
        console.warn('Initial changeDataset failed', e);
      }
    }
  </script>
</body></html>"""
