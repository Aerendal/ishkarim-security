# ishkarim-security

> Bezpieczeństwo systemów AI: prompt injection, autoryzacja, OWASP-LLM, audyt.

## Instalacja

```bash
pip install -e projects/ishkarim-security
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-security
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_security as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **53 katalogów** obszaru `security`:

- `Algorytm a dokładność obliczeń`
- `Atak przez zaproszenia w Google Calendar`
- `Badania Microsoft: prywatność w modelach LLM`
- `Bezpieczna autoryzacja CLI dla AI‑łączników`
- `Bezpieczna autoryzacja CLI w AI API`
- `Bezpieczne aktualizacje i dostęp CLI`
- `Bezpieczne kopie zapasowe dla bazy RAG w SQLite`
- `Bezpieczne tie-breaki w re-rankingu - Borda i Condorcet`
- … i 45 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### Algorytm a dokładność obliczeń

# WORK: Algorytm a dokładność obliczeń
## 0-Metadane
- Katalog: Algorytm a dokładność obliczeń
- Pliki: 110 (bez placeholderów)
- Tagi: algorytmy, precyzja-obliczeniowa, kwantyzacja, PDCA, NLU, DSL, sandbox, R&D, Python, laptop-first

### Atak przez zaproszenia w Google Calendar

# WORK: Atak przez zaproszenia w Google Calendar
## 0-Metadane
- Katalog: Atak przez zaproszenia w Google Calendar
- Pliki: 15 (bez placeholderów)
- Tagi: bezpieczeństwo AI, prompt injection, Google Calendar, Gemini, LLM security, OWASP LLM01, agent security, DLP

### Badania Microsoft: prywatność w modelach LLM

# WORK: Badania Microsoft: prywatność w modelach LLM
## 0-Metadane
- Katalog: Badania Microsoft: prywatność w modelach LLM
- Pliki: 10 (bez placeholderów)
- Tagi: prywatność, LLM, contextual-integrity, microsoft-research, PrivacyChecker, CI-CoT, CI-RL, agenci-AI, PII, taint-tracking


## Struktura projektu

```
ishkarim-security/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 53 katalogów-źródeł
├── src/
│   └── ishkarim_security/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_security.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-security/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
