from fastapi import FastAPI
from .core.views import router as core_router
from .database import test_connection
app = FastAPI()

app.include_router(core_router, prefix="/core", tags=["Core"])


@app.on_event("startup")
async def startup_event():
    print("Testing database connection...")
    await test_connection()