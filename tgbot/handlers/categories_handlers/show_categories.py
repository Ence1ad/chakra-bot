from aiogram.types import CallbackQuery, Message
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from db.categories.categories_commands import select_categories

from tgbot.keyboards.app_buttons import AppButtons
from tgbot.keyboards.inline_kb import menu_inline_kb


async def display_categories(call: CallbackQuery, db_session: async_sessionmaker[AsyncSession],
                             buttons: AppButtons, i18n: TranslatorRunner) -> Message:
    user_id = call.from_user.id
    await call.message.delete()
    categories = await select_categories(user_id, db_session)
    if categories:
        cats_in_column = ''
        for idx, category in enumerate(categories, 1):
            cats_in_column += f"{idx}. {category.category_name}\n\r"
        markup = await menu_inline_kb(await buttons.category_menu_buttons(), i18n)
        return await call.message.answer(text=f"{i18n.get('show_categories_text')}\n\r{cats_in_column}", reply_markup=markup)
    else:
        markup = await menu_inline_kb(await buttons.new_category(), i18n)
        return await call.message.answer(text=i18n.get('empty_categories_text'), reply_markup=markup)