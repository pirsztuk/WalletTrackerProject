import os
import time
import jwt
import httpx

JWT_SECRET = os.getenv("JWT_SERVICE_SECRET")
API_BASE_URL = os.getenv("API_DOMAIN", "http://web:8000")


def generate_jwt() -> str:
    now = int(time.time())
    payload = {
        "iat": now,
        "exp": now + 10,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token if isinstance(token, str) else token.decode("utf-8")


async def api_request(
    method: str,
    path: str,
    data: dict | None = None,
) -> httpx.Response:
    url = f"{API_BASE_URL}{path}"
    token = generate_jwt()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.request(method=method.upper(), url=url, json=data, headers=headers)
        return response