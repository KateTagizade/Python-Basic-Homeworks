"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД.
"""
import asyncio
from typing import List, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import get_users_posts, USERS_DATA_URL, POSTS_DATA_URL
from homework_04.models import User, Base, async_engine, Post, Session



async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def create_user(session: AsyncSession, user):
    user = User(id = user["id"],name = user["name"], username = user["username"], email = user["email"])
    session.add(user)


async def create_post(session: AsyncSession, post):
    post = Post(id = post["id"],user_id = post["userId"], title = post["title"], body = post["body"])
    session.add(post)


async def async_main():
    await create_tables()
    users, posts = await asyncio.gather(get_users_posts(USERS_DATA_URL), get_users_posts(POSTS_DATA_URL))
    async with Session() as session:
        async with session.begin():
            for user in users:
                await create_user(session, user)
            for post in posts:
                await create_post(session, post)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
