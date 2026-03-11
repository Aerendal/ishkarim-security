# PROBLEMS — ishkarim-security

> Bezpieczeństwo systemów AI — OWASP-LLM Top-10, prompt injection, autoryzacja agentów

## ✅ Co ten projekt rozwiązuje

- ✅ Katalog zagrożeń **specyficznych dla LLM/agentów** z mitygacjami (OWASP LLM Top-10)
- ✅ Wzorce ochrony przed prompt injection (input validation, output sanitization, sandboxing)
- ✅ Autoryzacja CLI z Device Code Flow + JWKS — bez statycznych kluczy API
- ✅ Podpisywanie artefaktów (Cosign/Sigstore) — weryfikowalny łańcuch zaufania dla modeli
- ✅ Audit log który nie może być sfałszowany (append-only z hashami Merkle)

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Gotowe biblioteki do wdrożenia — to wzorce i dokumentacja, nie kod produkcyjny plug-and-play
- ❌ Penetration testing — dokumentuje zagrożenia, nie testuje aktywnie
- ❌ Compliance z GDPR/HIPAA automatycznie — wymaga dostosowania do konkretnego przypadku
- ❌ Zero-trust dla modeli multi-tenant (shared inference)

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **Prompt injection detection** jest heurystyczny — brak 100% skutecznej metody (znany problem branżowy)
- ⚠️ **Device Code Flow** ma timeout — długie operacje mogą wymagać re-auth
- ⚠️ **Cosign weryfikacja online** wymaga dostępu do rekor.sigstore.dev — dla air-gap potrzebna kopia lokalna
- ⚠️ **Wzorce Python 3.10+** — starsze środowiska wymagają portowania

---

## 🎯 Przypadki użycia

- 🎯 Audyt bezpieczeństwa systemu AI przed wdrożeniem produkcyjnym (security review checklist)
- 🎯 Checklist dla zespołu przed deploymentem agenta do klientów końcowych
- 🎯 Wdrożenie podpisanych modeli ML z weryfikowalnym software bill of materials (SBOM)
- 🎯 Bezpieczna autoryzacja dla narzędzi CLI używanych przez autonomicznych agentów

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
