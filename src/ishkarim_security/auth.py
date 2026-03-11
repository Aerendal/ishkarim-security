"""
auth.py — kod wyekstrahowany z WORK.md dla obszaru security.

Zawiera 3 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: CLI Login with Device Code Fallback
# Auto-fallback: PKCE jeśli jest przeglądarka, Device Code jeśli nie ma
def login(profile: str):
    if has_browser():
        return auth_pkce(profile)
    else:
        return auth_device_code(profile)

# Source: CLI z SSO i bezpiecznym kanałem aktualizacji
from auth.device_flow import start_device_authorization, poll_device_token
dr = start_device_authorization(cfg)
print(f"Wejdź na {dr['verification_uri']} i wpisz: {dr['user_code']}")
tokens = poll_device_token(cfg, dr['device_code'], dr['interval'], dr['expires_in'])
store.save(TokenSet(**tokens))

# Source: CLI z SSO i bezpiecznym kanałem aktualizacji
from auth.pkce import generate_code_verifier, code_challenge_s256
verifier = generate_code_verifier(64)  # 43-128 znaków
challenge = code_challenge_s256(verifier)
