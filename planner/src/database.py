from config import DB_PORT, DB_PASSWORD, DB_HOST, DB_NAME, DB_USER
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = (f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:'
                f'{DB_PORT}/{DB_NAME}')

engine = create_async_engine(DATABASE_URL)