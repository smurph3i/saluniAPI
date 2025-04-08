from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

URL_DATABASE = 'postgresql+asyncpg://postgres:demo123@localhost:5433/saluniAPI'

engine = create_async_engine(URL_DATABASE)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
