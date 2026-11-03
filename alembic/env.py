import asyncio

from alembic import context

from app import models
from app.db.base import Base
from app.db.session import engine

target_metadata = Base.metadata


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    raise SystemExit("Modo offline não suportado neste projeto.")
else:
    asyncio.run(run_async_migrations())