"""
ishkarim_security — moduł z obszaru security.

Bezpieczeństwo systemów AI: prompt injection, autoryzacja, OWASP-LLM, audyt.

Źródła: 53 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "security"



MODULES: list[str] = [
    'Algorytm a dokładność obliczeń',
    'Atak przez zaproszenia w Google Calendar',
    'Badania Microsoft: prywatność w modelach LLM',
    'Bezpieczna autoryzacja CLI dla AI‑łączników',
    'Bezpieczna autoryzacja CLI w AI API',
    'Bezpieczne aktualizacje i dostęp CLI',
    'Bezpieczne kopie zapasowe dla bazy RAG w SQLite',
    'Bezpieczne tie-breaki w re-rankingu - Borda i Condorcet',
    'Bezpieczny connector: aktualizacje, Device Code i podpisy artefaktów',
    'Bezpieczny renderer bloków w React z rejestrem wersji',
    'Bezpieczny test pochodzenia dla PoC',
    'Bezpieczny łącznik CI - CD z OIDC i rotacją sekretów',
    'Bezpieczny łącznik aktualizacji CLI z OIDC i Sigstore',
    'Bezpieczny łącznik aktualizacji CLI_02',
    'Bezpieczny łącznik aktualizacji i podpisy artefaktów',
    'CLI Login with Device Code Fallback',
    'CLI z SSO i bezpiecznym kanałem aktualizacji',
    'Clawdbot: co się dzieje, gdy agent ma root',
    'Fałszywy pakiet „sympy‑dev” kopał kryptowaluty',
    'Hybrid CPU+GPU AGI Key Findings',
    'Jak Vercel powstrzymał React2Shell',
    'Jak rozpoznać ryzykowne workflow w n8n',
    'Krytyczna luka RCE w n8n (CVE‑2026‑1470)',
    'Krytyczna luka\xa0n8n\xa0–\xa0CVE‑2026‑21858',
    'Krytyczna podatność RCE w n8n ujawniona',
    'Lekki inspektor różnic grafowych z podpisami i animacją',
    'Microsoft ujawnia klucze BitLockera pod nakazem',
    'Model zagrożeń dla Device Flow + JWKS',
    'Moltbot wywołuje ostrzeżenia o bezpieczeństwie agentów',
    'New experimental offline‑AI finds',
    'Nowe luki w glibc: CVE‑2026‑0915 i CVE‑2026‑0861',
    'Nowe: formalne planery i wzorce',
    'Nowy wektor phishingu trwałość przez RMM',
    'OIDC w CICD walidacja pola „aud” w tokenach',
    'Ochrona przed pośrednim prompt injection',
    'Offline WAL - snapshot z atestacją Cosign',
    'Offline‑first aktualizacje z autoryzacją CLI',
    'OpenID Federation\xa01.0\xa0zbliża się do zatwierdzenia',
    'Poprawki bezpieczeństwa kernela KVM dla Ubuntu 22.04 LTS',
    'Proaktywny Linux: od zdarzeń do polityk AI',
    'Ryzyka i mitigacje przy monitoringu aktualizacji',
    'Segmentacja tokenów w CLI',
    'Sekcja ‘Non‑Goals’ w ARCHITECTURE md',
    'System kodowania semantycznego IR i DSL',
    'Trwała pamięć agentów i inwarianty życia',
    'Tygodniowy radar CPU‑first: 30 XII–5 I',
    'Wnętrze pętli agenta Codex CLI',
    'Wzorce manifestów: od OCI do Frictionless',
    'Złośliwe rozszerzenia AI w VS\u202fCode kradły kod',
    'cURL kończy program bug bounty przez raporty AI',
    'n8n krytyczna luka RCE i fałszywe pakiety npm',
    'vLLM\xa0i\xa0ONNX\xa01.20.1\xa0–\xa0ścieżka\xa0CPU→GPU\xa0z\xa0kontrolą\xa0bezpieczeństwa',
    'Łańcuch zaufania dla aktualizacji CLI i Dockera',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "security"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
