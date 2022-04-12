import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from libs.common import keyboard as kb
from libs.common import states as st
from misc import bot, db, dp

from ..constants import phone_reg, user_roles


@dp.message_handler(regexp=phone_reg, content_types=types.ContentTypes.TEXT, state=st.LoginStates.waiting_for_contact)
async def process_contact_response(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    phone_number = message.text

    phone_list = {"1": phone_number}
    await state.update_data(phone_list=phone_list)

    await bot.send_message(user_id, text="Введіть, будь ласка, ваш ПІП:", reply_markup=ReplyKeyboardRemove())
    await st.LoginStates.waiting_for_full_name.set()


@dp.message_handler(
    lambda message: not re.search(phone_reg, message.text),
    content_types=types.ContentTypes.TEXT,
    state=st.LoginStates.waiting_for_contact,
)
async def process_contact_error(message: types.Message):
    await message.reply(text="Перевірте введені дані")


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=st.LoginStates.waiting_for_full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.text

    data = await state.get_data()
    db.people_table.create_human(user_id, full_name, user_roles.get("regular_user"), data.get("phone_list"))

    await bot.send_message(
        user_id,
        text="Дякую за співпрацю!\n🏡 Головне меню. Використовуйте кнопки внизу👇",
        reply_markup=kb.mainMenu.main_menu_kb,
    )
    await st.MainMenuStates.in_Main_menu.set()
