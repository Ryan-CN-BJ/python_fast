from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)

from app.core.config import dbSetting

_engine: None | AsyncEngine = None


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


_session_factory = None


def get_sesstion_factory():
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(), class_=AsyncSession, expire_on_commit=False, autoflush=True
        )
    return _session_factory
