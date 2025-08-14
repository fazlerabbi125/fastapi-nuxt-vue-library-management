from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from settings import config

# The typical form of a database URL is: dialect[+driver]://username:password@host:port/database
# https://docs.sqlalchemy.org/en/20/dialects/index.html

connection_url = URL.create(
    "mysql+pymysql",
    username=config.db_user,
    password=config.db_password,
    host=config.db_host,
    database=config.db_name,
)

# In fastapi, it is very normal to have more than 1 thread that can interact at the same time.
# That is why when SQLite db is used, set connect_args = {"check_same_thread": False} in engine as SQLite by default is single-threaded per connection. Not needed for other SQL databases.
engine = create_engine(
    connection_url,  # plain string or URL object
    pool_pre_ping=True,  # Checks connections before using them
)
# https://docs.sqlalchemy.org/en/20/orm/session_basics.html#what-does-the-session-do
# autocommit and autoflush are False to stop SQLAlchemy from automatically committing changes made within a session or flushing changes to the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase): pass

# def init_db():
#     '''
#     Creates all tables stored in this metadata and, by default, will not attempt to recreate tables already present in the target database.
#     '''
#     Base.metadata.create_all(bind=engine)

def get_db():
    with SessionLocal() as db:
        '''
        Same as:
            try: yield db
            finally: db.close()
        The Python context manager (i.e. with: statement) automatically closes db at the end of the block;
        '''
        yield db

# Dependency injection to get the database session
DB_Session = Annotated[Session, Depends(get_db)]
