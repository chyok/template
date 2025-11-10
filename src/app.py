from fastapi import FastAPI
from src.api.v1 import item

app = FastAPI(
    title="{{ project_name }}",
    description="{{ project_description }}",
    version="{{ project_version }}",
)

app.include_router(item.router, prefix="/api/v1", tags=["items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the {{ project_name }}"}
