---
name: stress-test
description: Stress Test Engine with 5 campaigns (multiagent-debate, red-teaming, failure-anticipation, counterfactual-probing, adversarial-stress-testing). Use this skill whenever a user needs to adversarially validate any research artifact — hypotheses, claims, experiment designs, approaches, research questions, gaps, or ideas. Pre-condition: artifact exists + north-star-crystallization complete.
---

# Stress Test

Research Artifact Stress-Testing Engine — from structured debate to logical extreme, every claim must survive or be annotated. Five campaigns, each a self-contained adversarial validation domain. You provide a research artifact — the engine routes to the right campaign, selects a strategy, and executes autonomously with quantitative budget enforcement.

## Design Philosophy

兵法书 (Strategy Book) mode. This file is a textbook, not a script. CC reads, internalizes principles, then autonomously constructs the validation approach for the specific artifact.

Hard constraints only:
- **Budget Gate**: Meet the strategy's quantitative floor (±10%) before completing
- **State Ledger**: Print progress against budget before each major iteration decision
- **HARD-GATE**: Pre-conditions must be satisfied before entry
- **Context-checkpoint**: Triggered after each strategy completes (≥500 lines)

Everything else — execution order, iteration count, tactic selection, SOP combination — is CC's autonomous decision.

## Pre-conditions

1. Artifact exists (from knowledge-acquisition, deep-insight, hypothesis-formation, ideation, or convergence)
2. North-star-crystallization complete (provides scope constraint)

## Execution Boundaries

- Stop at validation and weakness annotation — do NOT modify the original artifact
- Do NOT perform upstream gap discovery or hypothesis generation
- May suggest correction directions, but actual corrections are executed by upstream repos

## Artifact Types Accepted

| Type | Description |
|------|-------------|
| `gap` | Research gap |
| `hypothesis` | Testable hypothesis |
| `research-question` | Research question |
| `idea` | Creative solution |
| `approach` | Selected method path |
| `experiment-design` | Experiment design |
| `claim` | Any research claim |

## Four-Level Hierarchy

```
ENTRY.md (this file)
  → Campaign (5): self-contained adversarial validation domain
    → Strategy: selected by validation purpose/intent
      → Tactic: multi-step orchestration pattern (reusable across strategies)
        → SOP: single operation (import or subagent)
```

CC can skip the tactic layer and use SOPs directly when the task is simple enough.

## Campaign Routing

| Signal | Campaign |
|--------|----------|
| 需要对抗辩论验证、多视角评审 | → multiagent-debate |
| 需要系统性攻击、假设挑战 | → red-teaming |
| 需要预测失败模式、风险评估 | → failure-anticipation |
| 需要探测关键依赖、因果必要性 | → counterfactual-probing |
| 需要逻辑证伪、边界测试 | → adversarial-stress-testing |

## Multi-Campaign Orchestration

Campaigns can be composed:
- **快速验证**: multiagent-debate (critic-defender-judge) 单轮
- **标准验证**: red-teaming + counterfactual-probing
- **深度验证**: 全部 5 campaigns 串联
- **特定风险**: failure-anticipation + adversarial-stress-testing

The orchestrator decides composition based on artifact type and validation needs.

## MCP Tools

| MCP Server | Tools | Purpose |
|------------|-------|---------|
| brave-search | brave_web_search, brave_news_search, brave_llm_context | Web discovery |
| apify | rag-web-browser | Full-text web retrieval |
| alphaxiv | discover_papers, get_paper_content, answer_pdf_queries | Paper access |
| semantic-scholar | relevanceSearch, paper, paperBatch, citations, references | Paper metadata |

## Context Management

- **Campaign start**: `context-init` — initialize context file
- **After each strategy**: `context-checkpoint` — append ≥500 lines
- One context file per campaign

## Output Types

Each campaign produces its own typed report:
- `DebateVerdict` (multiagent-debate)
- `RedTeamReport` (red-teaming)
- `FailureAnticipationReport` (failure-anticipation)
- `CounterfactualMap` (counterfactual-probing)
- `AdversarialStressReport` (adversarial-stress-testing)

`verdict-synthesis` SOP can aggregate multiple campaign results into a unified `StressTestSummary`.

## Dependencies

| Dependency | Provides |
|------------|----------|
| web-browsing | web-search, web-research (Import SOP) |
| literature-engine | paper-overview, paper-search, paper-research (Import SOP) |
| subagent-spawning | spawn-agent (execution runtime) |
| context-management | context-init, context-checkpoint (state persistence) |
| deep-insight | assumption-surfacing, evidence-synthesis, multi-stakeholder-simulation (cross-repo shared SOP) |
