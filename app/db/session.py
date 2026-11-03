from sqlalchemy.engine import make_url
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

url = make_url(settings.database_url).set(query={})

engine = create_async_engine(
    url,
    connect_args={"ssl": "require"} if settings.db_ssl else {},
    pool_pre_ping=True,
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with SessionLocal() as session:
        yield session