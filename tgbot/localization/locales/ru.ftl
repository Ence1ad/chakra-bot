canceling_text = Ваше действие было отменено
exit_text = До скорой встречи!
options_text = Выберите кнопку
select_lang_text = Выберите язык
set_lang_text = ✅ Установлен английский язык!
settings_not_change_text = ❌ Уже установлен ❗️
use_bot_text = Чтобы воспользоваться ботом, вам необходимо зарегистрироваться в группе:
help_unknown_command_text = Извините, я не знаю этой команды. Пожалуйста, используйте '/help' для просмотра доступных команд
help_invalid_command_format_text = Неверный формат команды. Для получения справки по конкретным командам используйте команду '/help_<команда>'.

valid_data_text = ❗️ Пожалуйста укажите корректные данные ❗️
throttling_text = ❗️ Вы слишком быстро отправляете сообщения. Пожалуйста, подождите ❗️

# for command_start_handler func
user_in_db_text = 👋🏼 Приветствую друг, 🤖 я очень рад тебя видеть!
new_user_text = Привет, друг! Что я могу для вас сделать?

# text for categories handlers
new_category_text = Напишите название категории ниже!
added_new_category_text = ✅ Вы успешно добавили новую категорию!
show_categories_text = Ваши категории:
empty_categories_text = ❗️ У вас еще нет категорий ❗️
select_category_text = Выберите категорию
selected_category = Выбранная категория -> {$category_name}{$new_line}{$actions_list_text}
rm_category_text = ✅ Категория была удалена!
upd_category_text = ✅ Имя категории было обновлено на {$new_category_name}
correct_category_text = Пожалуйста, напишите правильное название категории. {$new_line}
                        ❗️ Название категории - это текст, не более 30 символов ❗️
categories_is_fake_text = ❗️ Выберите корректную категорию ❗️
category_exists_text = ❌ Не удалось обновить имя категории! {$new_line}❗️ Категория с именем - {$new_category_name} уже существует ❗️
category_limit_text = ❗️ Вы достигли предела количества категорий - {$category_limit} ❗️
valid_category_name_text = ❌ Не удалось обновить имя категории! {$new_line}❗️ Имя должно состоять из букв ❗️
valid_new_category_name_text = ❌ Не удалось создать новую категорию! {$new_line}❗️ Имя должно состоять из букв ❗️

# text for actions handlers
new_action_text = Напишите название действия ниже.
show_action_text = Ваши действия для категории -> {$category_name}{$new_line}{$actions_list_text}
to_delete_action_text = Выберите действие для удаления
select_action_text = Выберите действие
to_update_action_text = Выберите действие для обновления
empty_actions_text = ❗️ У вас пока нет никаких действий ❗️
rm_action_text = ✅ Вы удалили действие -> {$action_name}
upd_action_text = ✅ Вы обновили название своего действия
first_start_text = Пожалуйста, используйте кнопку "настройки" для настройки вашего трекера действий
correct_action_text = Пожалуйста, напишите правильное название действия. Название действия - это текст, не более 30 символов!
action_limit_text = ❗️ Вы достигли предела количества действий - {$action_limit} для этой категории. ❗️
action_exists_text = Действие с именем - {$new_action_name} уже существует!
action_not_exists_text = ❗️ Выберите корректное действие ❗️
added_new_action_text = ✅ Вы успешно добавили новое действие - {$new_action_valid_name}
valid_action_name = ❌ Не удалось обновить имя действия! {$new_line}❗️ Имя должно состоять из букв ❗️
new_valid_action_name = ❌ Не удалось создать новое действие! {$new_line}❗️ Имя должно состоять из букв ❗️

# text for tracker handlers
select_category_4_tracker = Выбранная категория -> {$category_name}. {$new_line} Выберите действие!
new_tracker_text = ✅ Вы запустили трекер для действия -> {$action_name}
not_launched_tracker_text = У вас еще нет ни одного запущенного трекера!
already_launch_tracker_text = У вас уже есть запущенный трекер:
answer_stop_tracker_text = Вы хотите остановить трекер?
empty_category_actions_text = ❗️ Убедитесь, что вы создали действие для категории ❗️
stop_tracker_text = ✅ Трекер остановлен:
daily_tracker_text = Удалить трекеры за день
empty_stopped_tracker_text = У вас нет еще остановленных трекеров
delete_tracker_text = ✅ Вы удалили трекер
just_one_tracker = Вы не можете запустить больше одного трекера за раз. Вы хотите остановить трекер?
not_enough_data_text = Я не могу создать трекер. Данные не определены.
already_delete_tracker_text = Вы уже удалили трекер
too_long_tracker = трекер на данное действие был автоматически остановлен и удален! Трекер не может работать дольше 23 часов!
tracker_daily_limit_text = Вы достигли дневного лимита количества трекеров
# for reports handlers
send_report_text = Это ваш недельный отчет!
empty_trackers_text = У вас нет никаких трекеров на эту неделю!

# для started_tracker_text функции
started_tracker_title = Запущенный трекер:
category_title = 🗄 Выбранная категория
action_title = 🎬 Выбранное действие
action_duration = ⏱ Продолжительность


# клавиатуры:
# ActionsButtonsData
USER_ACTIONS = 📋 Список действий
CREATE_ACTIONS = 🆕 Создать действие
UPDATE_ACTIONS = 🆙 Обновить действие
DELETE_ACTIONS = 🗑 Удалить действие


# CategoriesButtonsData
USER_CATEGORIES = 🗂 Список категорий
CREATE_CATEGORIES = 🆕 Создать категорию
UPDATE_CATEGORIES = 🆙 Обновить категорию
DELETE_CATEGORIES = 🗑 Удалить категорию


# GeneralButtonsData:
ACTIONS_BTN = 🎬 Действия
CATEGORIES_BTN = 🗄 Категории
REPORTS_BTN = 📊 Отчеты
TRACKERS_BTN = ⏱ Трекеры
YES_BTN = 🟩 Да
NO_BTN = 🟥 Нет
EXIT_BTN = ⬅️ выход
CANCEL_BTN = 🚫 отмена


# TrackersButtonsData
START_TRACKER_BTN = ▶️ Запуск трекера
DELETE_TRACKER_BTN = 🗑 Удалить трекеры
STOP_TRACKER_BTN = ⏹ Остановить трекер
DURATION_TRACKER_BTN = ⏳ Продолжительность


# ReportsButtonsData
WEEKLY_REPORT_BTN = 🗓 Недельный отчет

# SettingsButtonsData
LANGUAGE = 🌏 Язык
RUSSIA = 🇷🇺 Русский
X_RUSSIA = [X] 🇷🇺 Русский
ENGLISH = 🇬🇧 Английский
X_ENGLISH = [X] 🇬🇧 Английский