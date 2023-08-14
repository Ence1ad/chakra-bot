from aiogram import F

from .del_tracker import del_tracking_data, select_removing_tracker
from .stop_tracker import stop_tracker_handler
from .actions_tracker import display_actions_tracker
from .categories_tracker import select_category_tracker
from .launched import select_launched_tracker
from .menu_tracker import get_tracker_options, no_btn_handler
from .new_tracker import create_new_tracker
from tgbot.keyboards.buttons_names import yes_btn, no_btn
from tgbot.utils.callback_data_classes import SelectCategoryTrackerCallback, SelectActionTrackerCallback, \
    DeleteTrackerCallback


def register_tracker_handlers(router):
    router.callback_query.register(get_tracker_options, F.data == 'trackers_btn')
    router.callback_query.register(select_category_tracker, F.data == 'new_tracker_btn')
    router.callback_query.register(display_actions_tracker, SelectCategoryTrackerCallback.filter())
    router.callback_query.register(create_new_tracker, SelectActionTrackerCallback.filter())
    router.callback_query.register(select_launched_tracker, F.data == 'launched_btn')
    router.callback_query.register(stop_tracker_handler, F.data == yes_btn)
    router.callback_query.register(no_btn_handler, F.data == no_btn)
    router.callback_query.register(select_removing_tracker, F.data == 'delete_tracker_btn')
    router.callback_query.register(del_tracking_data, DeleteTrackerCallback.filter())