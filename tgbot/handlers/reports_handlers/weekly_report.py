from aiogram.types import CallbackQuery, FSInputFile, Message
from fluentogram import TranslatorRunner
from pandas import DataFrame
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from config import settings
from data_preparation.pd_prepare import pd_action_data, pd_category_data
from db.report.report_commands import select_weekly_trackers
from tgbot.keyboards.app_buttons import AppButtons
from tgbot.keyboards.inline_kb import menu_inline_kb
from data_preparation.create_report import create_fig


async def get_weekly_report(call: CallbackQuery, db_session: async_sessionmaker[AsyncSession],
                            buttons: AppButtons, i18n: TranslatorRunner) -> Message:
    user_id = call.from_user.id
    report = await select_weekly_trackers(user_id, db_session)
    markup = await menu_inline_kb(await buttons.report_menu(), i18n)
    if report:
        action_data: DataFrame = await pd_action_data(report)
        category_data: DataFrame = await pd_category_data(report)
        await create_fig(df_action=action_data, df_categories=category_data)
        await call.answer(text=i18n.get('send_report_text'))
        await call.message.delete()
        document = FSInputFile(settings.WEEKLY_XLSX_FILE_NAME)
        return await call.bot.send_document(chat_id=call.from_user.id, document=document)
    else:
        return await call.message.edit_text(text=i18n.get('empty_trackers_text'), reply_markup=markup)
