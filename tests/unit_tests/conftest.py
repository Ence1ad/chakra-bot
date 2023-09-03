import asyncio
import sys

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from db.actions.actions_db_commands import create_actions, delete_action
from db.base_model import SqlAlchemyBase
from db.categories.categories_commands import create_category, delete_category
from db.users.user import UserModel
from db.users.users_commands import create_user

import sqlalchemy as sa


@pytest.fixture(scope="session")
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        # Avoid "RuntimeError: Event loop is closed" on Windows when tearing down tests
        # https://github.com/encode/httpx/issues/914
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def async_engine():
    engine = create_async_engine(
        url='postgresql+asyncpg://admin:asdfgh@localhost:5432/test_db'
    )
    yield engine
    engine.sync_engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def create_drop_models(async_engine):
    async with async_engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.drop_all)


@pytest_asyncio.fixture(scope="session")
async def session(async_engine, create_drop_models):
    async with AsyncSession(async_engine) as db_session:
        yield db_session


@pytest_asyncio.fixture(scope='module')
async def add_user(session):
    user_obj = None
    user_id: int = 1111111111
    for i in range(3):
        user_obj: UserModel = await create_user(user_id=user_id + i, first_name='', last_name='', username='', db_session=session)
    yield user_obj
    await session.execute(sa.delete(UserModel).where(UserModel.user_id == user_id))


@pytest_asyncio.fixture(scope='module')
async def add_category(session, add_user):
    category_name = 'best_category_ever'
    category_obj = await create_category(user_id=1111111111, category_title=category_name, db_session=session)
    yield category_obj
    await delete_category(user_id=1111111111, category_id=category_obj.category_id, db_session=session)


# @pytest_asyncio.fixture(scope='module')
# async def add_action(session, add_user, add_category):
#     action_name = 'my_action'
#     category_id = 1
#     action_obj = await create_actions(user_id=1111111111, action_name=action_name, category_id=category_id, db_session=session)
#     yield action_obj
#     await delete_action(user_id=1111111111, action_id=action_obj.action_id, db_session=session)
