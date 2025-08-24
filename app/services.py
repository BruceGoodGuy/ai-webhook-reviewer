from fastapi import HTTPException
from .utils import verify_signature
import httpx
from .config import settings
from .github_api import get_github_client


async def validate_webhook(request, x_hub_signature_256: str, x_github_event: str):
    if not x_hub_signature_256:
        raise HTTPException(
            status_code=403, detail="x-hub-signature-256 header is missing!"
        )

    if x_github_event != "pull_request":
        return {"ok": True, "ignored": x_github_event}

    raw = await request.body()

    if not verify_signature(raw, x_hub_signature_256):
        raise HTTPException(status_code=403, detail="Request signatures didn't match!")


async def fetch_diff_data(patch_url: str):
    """
    Fetch the diff data from the provided patch URL.
    """
    try:
        token = settings.GITHUB_WEBHOOK_SECRET
        headers = {"Accept": "application/vnd.github.v3.patch"}
        if token:
            headers["Authorization"] = f"token {token}"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                patch_url, headers=headers, timeout=10.0, follow_redirects=True
            )
            response.raise_for_status()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Request failed: {exc}")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Error response {exc.response.status_code} while requesting {patch_url}",
        )

    return {"patch_content": response.text}


async def fetch_files(owner: str, repo: str, pr_number: int) -> list[dict]:
    token = settings.GITHUB_API
    GITHUB_API = "https://api.github.com"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "ai-review-bot",
    }
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}/files?per_page=100"
    items = []
    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        while url:
            r = await client.get(url, headers=headers)
            r.raise_for_status()
            items.extend(r.json())
            url = r.links.get("next", {}).get("url")
    return items


async def add_feedbacks(feedbacks: list[dict], repo_config: dict):
    if len(feedbacks) == 0:
        # Means there are no feedbacks to add.
        return

    gh = get_github_client()
    repo = gh.get_repo(repo_config["name"])
    pr = repo.get_pull(repo_config["pr_number"])

    last_commit = pr.get_commits()[pr.commits - 1]

    comments = [
        {
            "path": feedback["filename"],
            "line": feedback["line"],
            "side": "RIGHT",
            "body": feedback["content"],
        }
        for feedback in feedbacks
    ]

    pr.create_review(
        commit=last_commit,
        body="AI Code Review",
        event="COMMENT",
        comments=comments,
    )
