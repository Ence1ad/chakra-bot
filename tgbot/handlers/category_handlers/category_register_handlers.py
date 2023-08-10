from aiogram import F

from tgbot.handlers.category_handlers import new_category, get_category_name_from_user, get_categories_options, \
    display_categories, select_remove_category, del_category, select_update_category, select_category, upd_category
from tgbot.keyboards.buttons_names import categories_btn, user_categories, create_categories, delete_categories, \
    update_categories
from tgbot.keyboards.categories_kb import DeleteCategoryCallback, UpdateCategoryCallback
from tgbot.utils.states import CategoryState, UpdateCategoryState


def register_categories_handlers(router):
    router.callback_query.register(get_categories_options, F.data == categories_btn)
    router.callback_query.register(new_category, F.data == create_categories)
    router.message.register(get_category_name_from_user, CategoryState.GET_NAME)
    router.callback_query.register(display_categories, F.data == user_categories)
    router.callback_query.register(select_remove_category, F.data == delete_categories)
    router.callback_query.register(del_category, DeleteCategoryCallback.filter())
    router.callback_query.register(select_update_category, F.data == update_categories)
    router.callback_query.register(select_category, UpdateCategoryCallback.filter())
    router.message.register(upd_category, UpdateCategoryState.GET_NAME)
