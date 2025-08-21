from typing import Generator
from fastapi import HTTPException
from github import Github, Auth
from github.Repository import Repository
from .config import settings


def get_github_client() -> Generator[Github, None, None]:
    auth = Auth.Token(settings.GITHUB_API)
    return Github(auth=auth)


def get_repo() -> Repository:
    try:
        github = get_github_client()
        repo = github.get_repo("BruceGoodGuy/test-webhook")
        pulls = repo.get_pulls(state='open', sort='created', base='dev')
        print("Repo data:", pulls.totalCount, pulls[0].title if pulls.totalCount > 0 else "No open PRs")
        return repo
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Repo not found: {e}")
