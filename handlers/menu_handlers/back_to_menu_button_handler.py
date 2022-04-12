from aiogram import types
from aiogram.dispatcher import FSMContext

from libs.common import keyboard as kb
from libs.common import states as st
from libs.common.keyboard.main.help_menus.base import BaseHelpButtonTexts as ButtonTexts
from misc import bot, dp, db


@dp.message_handler(text=ButtonTexts.back_to_main_menu, state="*")
async def process_back_button(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if db.people_table.human_exists(user_id):
        await bot.send_message(
            user_id,
            text="🏡 Головне меню. Використовуйте кнопки внизу👇",
            reply_markup=kb.mainMenu.main_menu_kb,
        )
        await state.reset_data()
        await st.MainMenuStates.in_Main_menu.set()
