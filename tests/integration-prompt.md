# Integration Test Scenarios

These scenarios verify end-to-end behavior of the stress-test engine across campaigns.

## Scenario 1: Single Campaign Quick Validation

**Input artifact:**
```yaml
type: hypothesis
content: "LLMs can reliably detect logical fallacies in academic arguments with >90% accuracy when given sufficient context."
source: hypothesis-formation
```

**Expected behavior:**
1. Route to `multiagent-debate` (hypothesis → critic-defender-judge primary)
2. Select S budget tier (quick validation)
3. Execute dialectical-escalation tactic
4. Spawn: debate-architect, debate-critic, debate-defender, debate-judge
5. Run 4 debate rounds minimum
6. Call saturation-detection after rounds complete
7. Call weakness-classification for each finding
8. Call verdict-synthesis to produce DebateVerdict
9. context-checkpoint triggered (≥500 lines)

**Validations:**
- [ ] Budget met: ≥4 debate rounds, ≥3 agents, ≥3 dimensions
- [ ] State Ledger printed before escalation decision
- [ ] No user prompts during execution
- [ ] Output is valid DebateVerdict with: status, confidence, findings table
- [ ] context-checkpoint file created

---

## Scenario 2: Multi-Campaign Standard Validation

**Input artifact:**
```yaml
type: experiment-design
content: "A/B test comparing chain-of-thought prompting vs direct prompting on GSM8K. N=1000 problems, random split, measure accuracy and token cost. Hypothesis: CoT improves accuracy by >15% with <3x token cost increase."
source: convergence
```

**Expected behavior:**
1. Route to `red-teaming` + `failure-anticipation` (experiment-design with risk focus)
2. Select M budget tier

**Red-teaming execution:**
3. Execute structured-attack-campaign tactic
4. Spawn: threat-surface-mapping, attack-vector-generation, probe-execution, finding-aggregation
5. Run ≥6 probing rounds, ≥12 attack vectors
6. Call attack-resilience-scoring
7. Produce RedTeamReport

**Failure-anticipation execution:**
8. Execute premortem-to-fmea-pipeline tactic
9. Spawn: premortem-facilitation, failure-mode-extraction, severity-scoring, occurrence-scoring, detection-scoring
10. Identify ≥20 failure modes
11. Score all with S/O/D
12. Call action-priority-matrix
13. Produce FailureAnticipationReport

**Cross-campaign:**
14. Call verdict-synthesis with both campaign results
15. Produce StressTestSummary

**Validations:**
- [ ] Both campaigns execute independently
- [ ] Budget met for both (M tier floors)
- [ ] State Ledger printed in each campaign
- [ ] No user prompts during execution
- [ ] Two typed reports produced + one StressTestSummary
- [ ] context-checkpoint files created (one per campaign)

---

## Scenario 3: Full Deep Validation

**Input artifact:**
```yaml
type: claim
content: "Transformer attention is both necessary and sufficient for in-context learning. Without attention, models cannot perform ICL regardless of parameter count; with attention alone (even in simple architectures), ICL emerges."
source: deep-insight
```

**Expected behavior:**
1. Route to ALL 5 campaigns (strong causal claim requiring comprehensive validation)
2. Select L budget tier (deep validation)

**Campaign execution order** (CC decides, but all 5 must run):
- multiagent-debate: courtroom-structured (evidence-intensive claim)
- red-teaming: assumption-challenge + systematic-probing
- failure-anticipation: design-fmea (what if the claim is wrong?)
- counterfactual-probing: necessity-sufficiency + factor-removal
- adversarial-stress-testing: assumption-negation + boundary-enumeration

**Validations:**
- [ ] All 5 campaigns execute
- [ ] L budget floors met in each
- [ ] State Ledger printed in each campaign
- [ ] 5 typed reports produced
- [ ] StressTestSummary aggregates all 5
- [ ] Saturation detection called in each campaign
- [ ] context-checkpoint files created (5 total)
- [ ] No user prompts during execution
- [ ] Total findings classified by weakness-classification
- [ ] Mitigation proposals generated for fatal/major findings

---

## Validation Checklist (applies to all scenarios)

- [ ] Pre-conditions checked before entry (artifact exists, north-star complete)
- [ ] Execution boundaries respected (no artifact modification, no upstream work)
- [ ] Budget Gate enforced (±10% of floor)
- [ ] State Ledger printed before major decisions
- [ ] Context management integrated (init + checkpoints)
- [ ] Output matches expected typed report schema
- [ ] Weakness classification uses correct severity tiers (fatal/major/minor/cosmetic)
- [ ] Saturation detection terminates appropriately
