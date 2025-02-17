from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Environment variables for database configuration
DATABASE_NAME = os.environ.get("POSTGRES_DB", "fastapi_db")
DATABASE_USER = os.environ.get("POSTGRES_USER", "fastapi_user")
DATABASE_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "strong_password")
DATABASE_HOST = os.environ.get("POSTGRES_HOST", "postgres-db-fastapi")
DATABASE_PORT = os.environ.get("POSTGRES_PORT", "5432")

# Constructing the DATABASE_URL
DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Creating the async engine and session
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Declarative Base
Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

# Test database connection (without asyncio.run())
async def test_connection():
    try:
        async with engine.connect() as connection:
            await connection.execute("SELECT 1")
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
