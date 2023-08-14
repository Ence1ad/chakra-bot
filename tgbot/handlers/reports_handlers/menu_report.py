from aiogram.types import CallbackQuery

from tgbot.keyboards.buttons_names import reports_buttons
from tgbot.keyboards.menu_kb import menu_inline_kb
from tgbot.utils.answer_text import options_text


async def get_report_options(call: CallbackQuery):
    await call.message.delete()
    markup = await menu_inline_kb(reports_buttons)
    await call.message.answer(text=options_text, reply_markup=markup)


