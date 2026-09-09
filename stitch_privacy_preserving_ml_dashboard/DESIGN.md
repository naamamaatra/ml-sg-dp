---
name: Cryptic Gradient Dark
colors:
  surface: '#10141a'
  surface-dim: '#10141a'
  surface-bright: '#353940'
  surface-container-lowest: '#0a0e14'
  surface-container-low: '#181c22'
  surface-container: '#1c2026'
  surface-container-high: '#262a31'
  surface-container-highest: '#31353c'
  on-surface: '#dfe2eb'
  on-surface-variant: '#c5c5d5'
  inverse-surface: '#dfe2eb'
  inverse-on-surface: '#2d3137'
  outline: '#8f909e'
  outline-variant: '#444653'
  surface-tint: '#b9c3ff'
  primary: '#b9c3ff'
  on-primary: '#002388'
  primary-container: '#7189f6'
  on-primary-container: '#001e78'
  inverse-primary: '#3c55bf'
  secondary: '#f8acff'
  on-secondary: '#570066'
  secondary-container: '#731f82'
  on-secondary-container: '#f093fb'
  tertiary: '#9bcbff'
  on-tertiary: '#003256'
  tertiary-container: '#3196e6'
  on-tertiary-container: '#002c4b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b9c3ff'
  on-primary-fixed: '#001356'
  on-primary-fixed-variant: '#1f3ba6'
  secondary-fixed: '#ffd6fe'
  secondary-fixed-dim: '#f8acff'
  on-secondary-fixed: '#350040'
  on-secondary-fixed-variant: '#731f82'
  tertiary-fixed: '#d0e4ff'
  tertiary-fixed-dim: '#9bcbff'
  on-tertiary-fixed: '#001d34'
  on-tertiary-fixed-variant: '#004a7a'
  background: '#10141a'
  on-background: '#dfe2eb'
  surface-variant: '#31353c'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.025em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.005em
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
    letterSpacing: -0.01em
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.06em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-2xs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4rem
  gutter-mobile: 1rem
  gutter-desktop: 1.5rem
  margin-mobile: 1rem
  margin-tablet: 2rem
  margin-desktop: 2.5rem
---

## Brand & Style

This design system expresses rigorous cryptographic engineering combined with refined, high-end artificial intelligence research. It targets ML engineers, privacy researchers, and enterprise compliance architects exploring Differential Privacy (DP-SGD) and verifiable privacy budgets.

The emotional signature is precise, scientific, and reassuringly secure—balancing dense technical telemetry with luminous ambient energy. The aesthetic unites deep, obsidian-grade dark surfaces with glassmorphism, hyper-fine 1px neon borders, and controlled atmospheric chromatic glows (violet, hot pink, and cyan). Rather than loud or distracting, the neon treatments act as functional spectral accents indicating privacy gradients, convergence thresholds, and mathematical certainty.

## Colors

The palette is engineered specifically for deep dark mode environments, using calibrated light emission against deep space obsidian foundations to prevent eye strain during long experimentation runs.

### Palette Architecture
- **Canvas Base (`#0d1117`)**: Primary viewport and canvas background. Absolute, quiet baseline that allows illuminated telemetry to surface effortlessly.
- **Card Surfaces (`#161b22`)**: Standard structural card background, paired with alpha blending (`rgba(22, 27, 34, 0.75)`) for frosted glass panels.
- **Surface Elevated (`#21262d`)**: Interactive control containers, input trays, table headers, and hover layers.
- **Primary Violet/Purple (`#667eea`)**: Primary brand anchor, model training telemetry, global actions, and primary gradient origins.
- **Secondary Vivid Pink (`#f093fb`)**: Noise injection indicators, epsilon ($\varepsilon$) budget exhaustion metrics, and gradient midpoints.
- **Tertiary Cyan (`#4facfe`)**: Delta ($\delta$) guarantees, sample rate metrics, convergence paths, and luminous highlights.

### Semantic Privacy & Risk Status
- **Private / Safe (`#10b981`)**: Optimal DP guarantees, clean differential privacy bounds ($\varepsilon \le 1.0$).
- **Moderate Warning (`#f59e0b`)**: Privacy budget depletion threshold approaching ($\varepsilon$ between $1.0$ and $5.0$).
- **High Risk / Leakage Alert (`#ef4444`)**: Insufficient noise scale, high privacy leakage probability ($\varepsilon > 5.0$).

## Typography

Typography pairs high-legibility sans-serif precision with strict monospaced data alignment.

- **Primary Interface Font (`Inter`)**: Deployed across displays, section headers, metadata labels, and body explanations. Its high x-height and clean geometry preserve clarity when illuminated over dark backgrounds.
- **Telemetry & Tabular Font (`JetBrains Mono`)**: Mandatory for mathematical parameter values, tensor shapes, gradient clip bounds ($C$), noise multipliers ($\sigma$), privacy losses ($\varepsilon, \delta$), step counters, and tabular log readouts.
- **Tabular Numerals**: In UI dashboards, always enforce `font-feature-settings: "tnum" 1, "zero" 1` to eliminate layout jitter when real-time training steps update.
- **Text Hierarchy & Colors**: Primary text uses `#f0f6fc` (high contrast), secondary context uses `#8b949e`, and tertiary disabled or structural tokens use `#484f58`.

## Layout & Spacing

The layout is built on a 12-column responsive fluid grid operating within a fixed viewport structure, optimized for analytics and control surfaces:

### Grid Structure
- **Desktop (1280px and above)**: 12-column grid, 24px gutters, max-width 1680px, with a persistent 280px parameter control drawer on the left and dynamic data telemetry spanning remaining columns.
- **Tablet (768px - 1279px)**: 8-column layout, 16px gutters, collapsible sliding parameter panel, chart visualizations stacked vertically.
- **Mobile (< 768px)**: 4-column layout, 16px gutters, tabs switching between parameter calibration and training visualization.

### Spacing Rhythm
Built upon an 8pt base grid with a 4pt micro-step system:
- **Card Internals**: 20px padding for standard telemetry cards; 24px padding for hero charts.
- **Metric Grouping**: 8px between labels and metric values; 16px to 24px between distinct parameter clusters.
- **Control Stacks**: 12px vertical gaps between hyperparameter sliders, gradient clip controls, and epoch pickers.

## Elevation & Depth

Visual hierarchy leverages frosted transparency, translucent backdrops, and selective neon edge lighting rather than standard drop shadows.

### Elevation Hierarchy
1. **Canvas Layer (Level 0)**: Background `#0d1117`. Flat, absorbing, non-interactive.
2. **Standard Surface (Level 1)**: `background: rgba(22, 27, 34, 0.75)`, `backdrop-filter: blur(16px)`, surrounded by a subtle 1px border `rgba(240, 246, 252, 0.1)`. Used for passive telemetry cards, data grids, and static monitors.
3. **Interactive / Hover Surface (Level 2)**: `background: rgba(33, 38, 45, 0.85)`, `backdrop-filter: blur(20px)`. Border illuminates to `rgba(102, 126, 234, 0.4)` with an ambient violet back-glow: `box-shadow: 0 0 20px -5px rgba(102, 126, 234, 0.25)`.
4. **Active Hero / Focus Layer (Level 3)**: Modals, parameter inspectors, and primary metrics. Bound with a dynamic gradient border (`linear-gradient(135deg, #667eea, #f093fb, #4facfe)`) paired with a concentrated multi-layer aura: `box-shadow: 0 0 35px -10px rgba(102, 126, 234, 0.35), 0 0 15px -2px rgba(240, 147, 251, 0.2)`.

## Shapes

The design system employs a refined Soft corner language (`0.25rem` / `4px` baseline) to reflect strict technical accuracy and scientific instrumentation.

- **Panels & Metric Cards**: `rounded-lg` (`0.5rem` / 8px). Creates crisp framing while softening the boundaries between glass layers.
- **Inputs, Buttons & Value Tills**: `rounded-md` (`0.375rem` / 6px) for an ergonomic, tactile hardware feel.
- **Status Tags, Badges & Privacy Indicators**: `rounded-full` (pill shape) to distinguish runtime status badges from structural data panels.
- **Slider Handles & Switch Knobs**: Exact circular geometry (`50%` radius) with embedded radial center glows.

## Components

### Buttons
- **Primary (Run Training / Deploy)**: Gradient background (`linear-gradient(135deg, #667eea 0%, #764ba2 100%)`), 1px translucent border (`rgba(255, 255, 255, 0.2)`), crisp white text (`#ffffff`), glowing drop-shadow on hover (`0 0 20px rgba(102, 126, 234, 0.4)`).
- **Secondary (Step / Export Logs)**: Surface `#21262d`, subtle border `#30363d`, text `#c9d1d9`. Hover state shifts border to `#8b949e` and background to `#30363d`.
- **Danger (Abort / Reset Budget)**: Background `rgba(239, 68, 68, 0.1)`, 1px border `rgba(239, 68, 68, 0.4)`, text `#ef4444`. Glows red on focus.

### DP Glow Sliders & Numeric Controls
- **Track**: 4px height, background `#21262d` with a filled track rendered in `#4facfe` to `#667eea` gradient.
- **Thumb**: 16px circle with a solid `#ffffff` core, 2px border `#667eea`, emitting an active radial halo (`0 0 12px #667eea`).
- **Value Tooltip**: Monospaced tabular readout hovering directly above thumb, displaying current value (e.g., `σ = 1.25`) in a `#161b22` pill.

### Privacy Status Badges & Chips
- **Private ($\varepsilon \le 1.0$)**: Background `rgba(16, 185, 129, 0.12)`, border `rgba(16, 185, 129, 0.3)`, text `#10b981`, leading dot pulse animation.
- **Moderate ($\varepsilon \le 5.0$)**: Background `rgba(245, 158, 11, 0.12)`, border `rgba(245, 158, 11, 0.3)`, text `#f59e0b`.
- **High Risk ($\varepsilon > 5.0$)**: Background `rgba(239, 68, 68, 0.15)`, border `rgba(239, 68, 68, 0.4)`, text `#ef4444`.

### Input Fields & Parameter Forms
- **Input Surfaces**: `#0d1117` inset, 1px border `#30363d`, text `#f0f6fc`, typography `JetBrains Mono`.
- **Focus State**: Border transitions to `#667eea` accompanied by a micro-ring: `box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.25)`.

### Cards & Telemetry Containers
- Built with `rgba(22, 27, 34, 0.75)` glass, 1px perimeter line `rgba(240, 246, 252, 0.08)`.
- Card headers feature a subtle top border gradient highlight running horizontally (`transparent` $\rightarrow$ `#667eea` $\rightarrow$ `transparent`).

### Interactive ML Visualizers & Epoch Graphs
- High-contrast canvas graphs displaying Loss vs. Epsilon curve overlays.
- Grid lines in `#21262d` at 50% opacity.
- Main curve rendered in neon cyan (`#4facfe`) with a soft glowing SVG filter blur behind it; DP-SGD differential noise band plotted as a translucent pink area (`rgba(240, 147, 251, 0.15)`).