import asyncio

from aiogram import Bot
from aiogram.types import FSInputFile
from pandas import DataFrame
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from cache.redis_tracker_commands import redis_delete_tracker, redis_hget_tracker_data, redis_decr_user_day_trackers
from cache.redis_schedule_command import redis_smembers_users
from config import settings
from data_preparation.create_report import create_fig
from data_preparation.pd_prepare import pd_action_data, pd_category_data
from db.report.report_commands import select_weekly_trackers
from db.tracker.tracker_db_command import delete_tracker
from tgbot.utils.answer_text import too_long_tracker


async def schedule_delete_tracker(bot: Bot, user_id: int, redis_client: Redis,
                                  async_session: async_sessionmaker[AsyncSession]) -> None:
    tracker_id = await redis_hget_tracker_data(user_id, redis_client, 'tracker_id')
    if tracker_id:
        action_name = (await redis_hget_tracker_data(user_id, redis_client, 'action_name')).decode(encoding='utf-8')
        await delete_tracker(user_id, tracker_id=int(tracker_id), db_session=async_session)
        await redis_delete_tracker(user_id, redis_client)
        await redis_decr_user_day_trackers(user_id, redis_client)
        await bot.send_message(chat_id=user_id, text=f'The tracker - {action_name} {too_long_tracker}')


async def schedule_weekly_report(
        bot: Bot, redis_client: Redis, async_session: async_sessionmaker[AsyncSession]
) -> None:
    members = await redis_smembers_users(redis_client)
    for user_id in members:
        report = await select_weekly_trackers(int(user_id), db_session=async_session)
        if report:
            action_data: DataFrame = await pd_action_data(report)
            category_data: DataFrame = await pd_category_data(report)
            await create_fig(df_action=action_data, df_categories=category_data)
            await asyncio.sleep(3)
            document = FSInputFile(settings.WEEKLY_XLSX_FILE_NAME)
            await bot.send_document(chat_id=user_id, document=document)
            await asyncio.sleep(2)
