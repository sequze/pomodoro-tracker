from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from core.models.db_helper import db_helper

@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    yield
    await db_helper.dispose()
app = FastAPI(
    lifespan=lifespan,
)
app.include_router(
    api_router,
    prefix=settings.api_prefix.prefix,
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)