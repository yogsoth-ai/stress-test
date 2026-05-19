---
name: multi-perspective-panel
description: "Strategy: Multi-stakeholder review panel — diverse expert perspectives evaluate artifact simultaneously, then synthesize through structured deliberation."
type: strategy
used-by: [multiagent-debate]
tactics: [perspective-rotation]
---

# Multi-Perspective Panel Strategy

Diverse expert panel evaluates artifact from multiple stakeholder viewpoints.

## Method

1. **debate-architect** selects relevant perspectives based on artifact domain
2. Each **perspective-critic** evaluates from assigned stakeholder viewpoint
3. **divergence-detection** maps agreement/disagreement landscape
4. Panel deliberation: agents respond to each other's concerns
5. **confidence-calibration** determines if consensus reached or irreconcilable

## Budget Table

| Parameter | S | M | L |
|---|---|---|---|
| 辩论轮数 | 4 | 8 | 12 |
| 参与agent数 | 3 | 5 | 8 |
| 覆盖维度数 | 3 | 5 | 7 |
| 外部证据搜索次数 | 2 | 5 | 10 |

## Orchestration

```
debate-architect → [select panel perspectives]
→ [parallel]: perspective-critic × N (independent evaluation)
→ divergence-detection (map landscape)
→ [deliberation rounds]:
    perspective-critic responds to disagreements
    → divergence-detection → confidence-calibration
→ debate-transcript-analysis → verdict-synthesis
```

## Subagents

- debate-architect (panel composition)
- perspective-critic × N (stakeholder evaluation)
- divergence-detection (agreement mapping)
- confidence-calibration (consensus detection)
