from typing import List
from requests import Session
from schemas import ReadUser, CreateUser, Item

from fastapi import FastAPI
from item import router as item_router

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine
from models import User

app = FastAPI()

app.include_router(item_router, prefix='/item',
                   tags=['items'])

@app.get('/')
async def hello():
    return {'hello': 'world'}

@app.post('user/')
async def add_user(user, CreateUser) -> dict:
    with Session(engine) as session:
        stmt = User(name=user.name, fullname=user.fullname, nickname=user.nickname)
        session.add(stmt)
        await session.commit()
        return {'status': 'OK'}

@app.get('/user') #получить всех пользователей
async def user_list(offset: int=0, limit: int=0) ->List[ReadUser]:
    async with AsyncSession(engine) as session:
        stmt = select(User)
        result = await session.scalars(stmt)
        users = result.all()
        print(users, type(users[0]))
    return users

@app.get('/user/{user_id}')
async def get_user(user_id:int) -> ReadUser:
    async with AsyncSession(engine) as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.scalars(stmt)
    return result.first()

@app.delete('/user/{user_id}')
async def delete_user(user_id:int) -> dict:
    async with AsyncSession(engine) as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.scalars(stmt)
        user =  result.first()
        await session.delete(user)
        await session.commit()
    return {'status': 'OK'}

@app.put()
async def update_user(): pass #обновить все данные пользователя

@app.patch()
async def update_user(): pass #смена никнейма