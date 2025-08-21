from typing import Union

from fastapi import FastAPI
from app.webhook import router as webhook_router
from .test import router as test_router

app = FastAPI()

app.include_router(webhook_router)
app.include_router(webhook_router, prefix="/webhook", tags=["webhook"])
app.include_router(test_router, prefix="/test", tags=["test"])