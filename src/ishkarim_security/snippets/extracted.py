"""
extracted.py — fragmenty kodu z WORK.md dla obszaru security.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 8 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Algorytm a dokładność obliczeń
# Zapis triala: before_*, after_*, delta_*, decision
trial = {
    "before_quality": best_quality,
    "after_quality": new_quality,
    "delta_quality": new_quality - best_quality,
    "decision": "ACCEPT" if new_quality - best_quality >= min_improvement else "REJECT"
}

# ────────────────────────────────────────────────────────────

# Source: Atak przez zaproszenia w Google Calendar
def naive_build_prompt(user_question, events):
    # BAD: opis eventu trafia wprost do promptu bez izolacji
    events_text = "\n\n".join(
        f"TITLE: {e.title}\nDESC: {e.description}" for e in events
    )
    return f"You are a helpful assistant.\n{user_question}\n{events_text}"

# ────────────────────────────────────────────────────────────

# Source: CLI Login with Device Code Fallback
# JWKS cache z kid-miss re-fetch
class JWKSCache:
    def get_key(self, kid: str):
        key = self._cache.get(kid)
        if key is None:
            self._refresh()          # wymuszone re-fetch
            key = self._cache.get(kid)
        return key

# ────────────────────────────────────────────────────────────

# Source: CLI z SSO i bezpiecznym kanałem aktualizacji
tm = TokenManager(cfg, store, leeway_seconds=60)
client = ApiClient(base_url=cfg.api_base_url, token_manager=tm, max_retries=2)
resp = client.request_json("GET", "/v1/data")

# ────────────────────────────────────────────────────────────

# Source: Hybrid CPU+GPU AGI Key Findings
# core/runtime/sandbox_backends/detect.py
def pick_backend(policy: SandboxPolicy) -> SandboxBackend:
    b = BwrapBackend(policy)
    if b.is_available(): return b
    f = FirejailBackend(policy)
    if f.is_available(): return f
    return FallbackBackend(policy)

# ────────────────────────────────────────────────────────────

# Source: Hybrid CPU+GPU AGI Key Findings
class SleepDecision(str, Enum):
    DEFER = "defer"        # odłóż ciężkie zadanie
    CONSOLIDATE = "consolidate"  # wykonaj lekkie teraz
    RUN = "run"

def decide(self, is_heavy: bool) -> SleepDecision:
    if self.in_sleep_window():  # 02:00–04:00
        return SleepDecision.DEFER if is_heavy else SleepDecision.CONSOLIDATE
    return SleepDecision.RUN

# ────────────────────────────────────────────────────────────

# Source: Sekcja ‘Non‑Goals’ w ARCHITECTURE md
@dataclass(frozen=True)
class ActionSpec:
    action_type: str
    capabilities: List[Capability]   # "network", "fs_write", "exec", "install", "schema_change"
    risk: Risk
    cmd: List[str]

class PolicyEngine:
    def decide(self, spec: ActionSpec) -> Decision:
        if "network" in spec.capabilities:
            return Decision(require_approval=True, require_exception_window=True,
                            sandbox_profile="net-allowed", ttl_seconds=900)
        if spec.risk == Risk.HIGH:
            return Decision(require_approval=True, require_exception_window=False,
                            sandbox_profile="no-net")
        return Decision(require_approval=False, require_exception_window=False,
                        sandbox_profile="no-net")

# ────────────────────────────────────────────────────────────

# Source: Sekcja ‘Non‑Goals’ w ARCHITECTURE md
# Test negatywny (pytest)
def test_no_network_calls(monkeypatch):
    import socket
    with pytest.raises(PermissionError):
        socket.create_connection(("example.com", 80), timeout=1)
