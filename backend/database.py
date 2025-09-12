from collections.abc import AsyncGenerator
from typing import Annotated
from fastapi import Depends
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase
from settings import config
from sqlalchemy_utils import generic_repr
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)

# The typical form of a database URL is: dialect[+driver]://username:password@host:port/database
# https://docs.sqlalchemy.org/en/20/dialects/index.html

connection_url = URL.create(
    "mysql+aiomysql",
    username=config.db_user,
    password=config.db_password,
    host=config.db_host,
    port=config.db_port,
    database=config.db_name,
).render_as_string(hide_password=False)

# In fastapi, it is very normal to have more than 1 thread that can interact at the same time.
# That is why when SQLite db is used, set connect_args = {"check_same_thread": False} in engine as SQLite by default is single-threaded per connection. Not needed for other SQL databases.
engine = create_async_engine(
    connection_url,  # plain string or URL object
    pool_pre_ping=True,  # Checks connections before using them
    # echo=config.debug_mode,  # Logs SQL queries executed
)
# https://docs.sqlalchemy.org/en/20/orm/session_basics.html#what-does-the-session-do
# flushing refers to sending pending SQL (INSERT/UPDATE/DELETE) to the database but not committing the transaction. The autoflush option is False to stop SQLAlchemy from automatically flushing changes to the database. The expire_on_commit controls access of object attributes subsequent to commit; by default it is True, so all instances will be fully expired after each commit() and will need to be reloaded on the next access via session.refresh().
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

@generic_repr
class Base(DeclarativeBase):
    pass

# def init_db():
#     '''
#     Creates all tables stored in this metadata and, by default, will not attempt to recreate tables already present in the target database.
#     '''
#     Base.metadata.create_all(bind=engine)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        """
        Same as:
            db = SessionLocal()
            try: yield db
            finally: await db.close()
        The Python context manager (i.e. with: statement) automatically closes db at the end of the block;
        """
        yield db


# Dependency injection to get the database session
DB_Session = Annotated[AsyncSession, Depends(get_async_db)]
