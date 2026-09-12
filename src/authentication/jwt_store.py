import time

from django.core.cache import cache

def make_token_key(jti: str) -> str:
    return f"jwt:active:{jti}"

def register_token(token) -> None:
    jti = str(token["jti"])
    expires_at = int(token["exp"])
    ttl = max(expires_at - int(time.time()), 1)

    cache.set(
        make_token_key(jti),
        token["token_type"],
        timeout=ttl,
    )

def is_token_active(token) -> bool:
    jti = str(token["jti"])
    return cache.get(make_token_key(jti)) is not None

def revoke_token(token) -> None:
    jti = str(token["jti"])
    cache.delete(make_token_key(jti))