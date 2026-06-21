"""One-shot acceptance check for the 7 falsification-first-stress-test skills.
Verifies frontmatter parses, type keys correct, no campaign:/used-by: keys,
deps alpha-sorted and matching expectation, every dep resolves in the DARE body."""
import sys, yaml
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent              # stress-test repo
BODY = PKG.parent / "de-anthropocentric-research-engine"

CAMPAIGN = "falsification-first-stress-test"
STRATEGIES = ["adversarial-debate-truthseeking", "circular-validation-audit",
              "elegance-trap-probe", "independent-convergence-audit",
              "isomorphism-falsification", "red-team-truthseeking"]
CAMPAIGN_SOPS = ["context-checkpoint", "context-init",
                 "stress-test-saturation-detection", "verdict-synthesis",
                 "weakness-classification"]
STRATEGY_DEPS = {
    "red-team-truthseeking": {"sops": ["devils-advocacy", "key-assumptions-check",
                                       "probe-execution", "threat-surface-mapping"]},
    "adversarial-debate-truthseeking": {"sops": ["cross-examination", "debate-architect"]},
    "isomorphism-falsification": {}, "circular-validation-audit": {},
    "independent-convergence-audit": {}, "elegance-trap-probe": {},
}

def fm_of(name):
    text = (PKG / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---"), f"{name}: no frontmatter"
    return text, yaml.safe_load(text.split("---", 2)[1])

def check_deps(name, deps):
    for grp, vals in deps.items():
        assert vals == sorted(vals), f"{name}.{grp} not alphabetical"
    missing = [d for grp in deps.values() for d in grp
               if not (BODY / "skills" / d).is_dir()]
    assert not missing, f"{name}: deps not resolvable in body: {missing}"

def main():
    text, fm = fm_of(CAMPAIGN)
    assert fm["name"] == CAMPAIGN, fm.get("name")
    assert fm["type"] == "campaign", fm.get("type")
    assert "execution" not in fm and "used-by" not in fm, "stray execution:/used-by:"
    deps = fm["dependencies"]
    assert deps["strategies"] == STRATEGIES, deps["strategies"]
    assert deps["sops"] == CAMPAIGN_SOPS, deps["sops"]
    check_deps(CAMPAIGN, deps)
    for s in STRATEGIES:
        text, fm = fm_of(s)
        assert fm["name"] == s, fm.get("name")
        assert fm["type"] == "strategy", f"{s}: type={fm.get('type')}"
        assert "campaign" not in fm, f"{s}: stray campaign: key"
        assert "used-by" not in fm, f"{s}: stray used-by: key"
        exp = STRATEGY_DEPS[s]
        got = fm.get("dependencies", {})
        assert got == exp, f"{s}: deps {got} != expected {exp}"
        check_deps(s, got)
    print("check_fft: OK — 7 skills valid, all deps resolve in body")

if __name__ == "__main__":
    sys.exit(main())
