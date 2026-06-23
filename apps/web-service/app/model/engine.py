from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from app.core.config import dbSetting

_engine = None


def get_engine() -> AsyncEngine:
    global _engine
    if _engine is None:
        url = (
            f"postgresql+asyncpg://{dbSetting.user}:{dbSetting.password}"
            f"@{dbSetting.host}:{dbSetting.port}/{dbSetting.name}"
        )
        _engine = create_async_engine(
            url, pool_size=10, max_overflow=20, pool_pre_ping=True, echo=True
        )
    return _engine
