from fastapi import FastAPI

from app.core.config import webSetting, commonSetting

is_production = commonSetting.enviroment == "production"

app = FastAPI(
    title=webSetting.app_name,
    docs_url=None if is_production else "/docs",
    redoc_url=None if is_production else "/redoc",
    openapi_url=None if is_production else "/openapi.json",
)

from .api.items import router as itemRouter
from .api.welcome import router as welcomeRouter

app.include_router(itemRouter)
app.include_router(welcomeRouter)
