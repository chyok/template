from fastapi import FastAPI
from src.api.v1 import item

app = FastAPI(
    title="Web Project Template",
    description="A template project for FastAPI.",
    version="0.1.0",
)

app.include_router(item.router, prefix="/api/v1", tags=["items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Web Project Template"}
