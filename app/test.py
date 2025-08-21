from fastapi import FastAPI, Depends, APIRouter

router = APIRouter()

@router.get("/test")
def test_endpoint():
    return {"message": "This is a test endpoint"}


# Dependency B
def get_message():
    return "Hello from B"

# Function A, depends on B
@router.get("/a")
def function_a(msg: str = Depends(get_message)):
    return {"from_a": "Method A executed", "from_b": msg}