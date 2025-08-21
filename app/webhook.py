from fastapi import APIRouter, Request, Header, HTTPException
from typing import Union
from app.config import settings
from .github_api import get_repo
from .utils import make_a_call, verify_signature
from .services import validate_webhook, fetch_diff_data, fetch_files, add_feedbacks
from .ai_chain import review_changes
import json


router = APIRouter()


@router.get("/")
def index():
    print("Webhook index accessed", settings.GITHUB_API)
    repo_name = get_repo()
    return {"message": "Webhook endpoint", "repo_name": repo_name.name}


@router.post("/")
async def handle_webhook(
    request: Request,
    x_github_event: str = Header(None),
    x_hub_signature_256: str = Header(None),
):
    await validate_webhook(request, x_hub_signature_256, x_github_event)

    payload = await request.json()

    action = payload.get("action")
    if action not in {"opened", "synchronize", "ready_for_review"}:
        return {"ok": False, "ignored_action": action}

    repo = payload["repository"]
    owner = repo["owner"]["login"]
    name = repo["name"]
    pr = payload["pull_request"]
    pr_number = pr["number"]
    
    print(f"Processing PR #{pr_number} in {owner}/{name} with action {action}")

    fetch_diff_data_result = await fetch_files(owner, name, pr_number)
    if not fetch_diff_data_result:
        return {"ok": False, "error": "Failed to fetch diff data"}
    if (len(fetch_diff_data_result) > 10000):
        return {"ok": False, "error": "Diff data is too large"}
    feedbacks = review_changes(fetch_diff_data_result)
    repo_config = {"name": f"{owner}/{name}", "pr_number": pr_number}
    print(f"Feedbacks generated: {feedbacks}")
    await add_feedbacks(json.loads(feedbacks), repo_config)
    return {"message": "Webhook processed successfully"}
