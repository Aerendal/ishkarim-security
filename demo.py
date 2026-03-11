#!/usr/bin/env python3
"""
demo.py — demo ishkarim-security

Bezpieczeństwo systemów AI — OWASP-LLM Top-10, prompt injection, autoryzacja agentów

Uruchomienie:
    python projects/ishkarim-security/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_security as m

docs = m.load_knowledge_index()
# Znajdź wzorce ochrony przed prompt injection
injection_docs = [d for d in docs
                  if "injection" in d["name"].lower() or "prompt" in d["name"].lower()]
auth_docs = [d for d in docs
             if "auth" in d["name"].lower() or "oidc" in d["name"].lower()]
print(f"Bezpieczeństwo AI — {len(docs)} katalogów wiedzy")
print(f"  Prompt injection:  {len(injection_docs)} wzorców")
print(f"  Autoryzacja/OIDC:  {len(auth_docs)} wzorców")
print("\nTop 3 zagrożenia:")
for d in docs[:3]:
    print(f"  ⚠ {d['name'][:65]}")

