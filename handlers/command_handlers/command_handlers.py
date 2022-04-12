from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from libs.common import keyboard as kb
from libs.common import states as st
from misc import bot, db, dp

from ..constants import help_text, welcome_text


@dp.message_handler(commands=["start"], state="*")
async def process_start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if not db.people_table.human_exists(user_id):
        await bot.send_message(user_id, text=welcome_text, parse_mode=types.ParseMode.MARKDOWN)
        await bot.send_message(
            user_id,
            text="Введіть номер телефону у форматі +380XXXXXXXXX:",
            reply_markup=ReplyKeyboardRemove(),
        )
        await st.LoginStates.waiting_for_contact.set()
    else:
        await state.reset_data()
        await bot.send_message(
            user_id,
            text="🏡 Головне меню. Використовуйте кнопки внизу👇",
            reply_markup=kb.mainMenu.main_menu_kb,
            parse_mode=types.ParseMode.MARKDOWN,
        )
        await st.MainMenuStates.in_Main_menu.set()


@dp.message_handler(commands=["help"], state="*")
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=help_text, parse_mode=types.ParseMode.MARKDOWN)
