import hmac, hashlib
from .config import settings
import requests

def verify_signature(raw: bytes, sig: str):
    hash_object = hmac.new(settings.GITHUB_WEBHOOK_SECRET.encode('utf-8'), msg=raw, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    return hmac.compare_digest(expected_signature, sig)


def make_a_call(url: str, headers: dict = None, data: dict = None):
    print("This is a call from utils.py")
    response = requests.get(url, headers=headers, json=data)
    return response.json()