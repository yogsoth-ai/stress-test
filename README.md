<!-- markdownlint-disable -->

<div align="center">

> *"The unexamined hypothesis is not worth testing."*
> — adapted from Socrates

</div>

# 🔬 Stress Test

*Research Artifact Stress-Testing Engine*

**A five-campaign adversarial validation system that subjects any research artifact to systematic stress-testing — from structured multi-agent debate to logical boundary analysis — producing weakness-annotated verification reports with severity classification and mitigation proposals.**

> 🧭 **Part of the [De-Anthropocentric Research Engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine).** This repository is one of nine composable research packages that make up DARE — the full autonomous research-orchestration system. DARE bundles this package together with the others into a single self-contained clone, unified under one orchestrator. To use these skills as intended — with the spec-driven orchestrator and cross-package routing — clone the [main repository](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) rather than this repo alone.

---

## ⚡ What It Does

- 🗣️ **Multiagent Debate** — structured adversarial debate via critic-defender-judge, society-of-mind, and courtroom models (Irving, Du, Liang, Toulmin)
- 🎯 **Red-Teaming** — military/intelligence-tradition systematic attacks: assumption challenge, adversarial personas, groupthink mitigation (UFMCS, CIA SAT, NIST AI RMF)
- ⚠️ **Failure Anticipation** — Klein pre-mortem + AIAG-VDA FMEA: predict how artifacts will fail before they do
- 🔄 **Counterfactual Probing** — Pearl SCM + Lewis possible worlds: identify load-bearing factors and causal necessity
- 🧪 **Adversarial Stress-Testing** — Lakatos reductio + BVA boundary analysis: find where claims break under logical extremes

---

## 🎯 Design Philosophy

Strategy Book mode — skills are textbooks, not scripts. The orchestrator reads, internalizes principles, then autonomously constructs the validation approach for the specific artifact.

Hard constraints only:
- **Budget Gate** — meet the strategy's quantitative floor (±10%) before completing
- **State Ledger** — print progress against budget before each major iteration decision
- **Context Checkpoint** — triggered after each strategy completes (≥500 lines)
- **Saturation Detection** — terminate when no new weaknesses are being discovered

Everything else — execution order, iteration count, tactic selection, SOP combination — is autonomous.

---

## 🏗️ Architecture

```bash
┌─────────────────────────────────────────────────────────────┐
│                        ENTRY.md                              │
│              (routing + orchestration)                        │
└──────────────────────────┬──────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Campaign   │  │  Campaign   │  │  Campaign   │  ... (×5)
│  SKILL.md   │  │  SKILL.md   │  │  SKILL.md   │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Strategy   │  │  Strategy   │  │  Strategy   │  ... (×25)
│  SKILL.md   │  │  SKILL.md   │  │  SKILL.md   │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   Tactic    │  │   Tactic    │  │   Tactic    │  ... (×15)
│  SKILL.md   │  │  SKILL.md   │  │  SKILL.md   │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Subagent   │  │  Subagent   │  │  Subagent   │  ... (×53)
│  SKILL.md   │  │  SKILL.md   │  │  SKILL.md   │
│  prompt.md  │  │  prompt.md  │  │  prompt.md  │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## 📊 Scale

| Layer | Count |
|-------|-------|
| Campaigns | 5 |
| Strategies | 25 |
| Tactics | 15 |
| Import SOPs | 5 |
| Cross-campaign shared SOPs | 4 |
| Campaign-specific subagent SOPs | 49 |
| **Total skill directories** | **103** |

---

## 🔗 Dependencies

| Dependency | Provides |
|------------|----------|
| web-browsing | web-search, web-research (import SOPs) |
| literature-engine | paper-overview, paper-search, paper-research (import SOPs) |
| subagent-spawning | spawn-agent (execution runtime) |
| context-management | context-init, context-checkpoint (state persistence) |
| deep-insight | assumption-surfacing, evidence-synthesis, multi-stakeholder-simulation (cross-repo SOPs) |

---

## 🚀 Quick Start

**Quick validation** (single campaign):
```
Validate this hypothesis using multiagent-debate with S budget.
```

**Standard validation** (two campaigns):
```
Run red-teaming and counterfactual-probing on this experiment design.
```

**Deep validation** (all campaigns):
```
Full stress-test on this claim with L budget across all campaigns.
```

---

## 📄 License

[Apache-2.0](LICENSE)

---

*A component of the [De-Anthropocentric Research Engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine), part of the [Yogsoth AI](https://github.com/yogsoth-ai) ecosystem. Built by [Pthahnix](https://github.com/Pthahnix).*
