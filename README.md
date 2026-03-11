# ishkarim-security

> **Bezpieczeństwo systemów AI — OWASP-LLM Top-10, prompt injection, autoryzacja agentów**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Katalog zagrożeń
- Wzorce ochrony przed prompt injection (input validation, output sanitization, sandboxing)
- Autoryzacja CLI z Device Code Flow + JWKS — bez statycznych kluczy API

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-security

# Demo (10 sekund)
python projects/ishkarim-security/demo.py
```

## Użycie w kodzie

```python
import ishkarim_security as m

# Wszystkie 53 katalogi wiedzy obszaru 'security'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_security.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Audyt bezpieczeństwa systemu AI przed wdrożeniem produkcyjnym (security review checklist)
- Checklist dla zespołu przed deploymentem agenta do klientów końcowych
- Wdrożenie podpisanych modeli ML z weryfikowalnym software bill of materials (SBOM)

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 53 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_security.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_security_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_security.py --quick
```

## Struktura projektu

```
ishkarim-security/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 53 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_security/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_security.py         ← testy jednostkowe
│   └── test_security_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_security.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 53 katalogów wiedzy obszaru `security`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
