import re

from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from libs.common import keyboard as kb
from libs.common import states as st
from libs.common.keyboard.main import MainMenuButtonTexts as ButtonTexts
from misc import bot, db, dp

from ..constants import admin_contact_text, donate_text, phone_reg, share_text


@dp.message_handler(text=[ButtonTexts.i_need_help_button], state=[st.MainMenuStates.in_Main_menu])
async def process_need_help_button(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(
        user_id,
        text="Важливо! Дайте відповідь на всі запитання. Це допоможе нам швидко знайти цільову допомогу!",
        reply_markup=kb.helpRequestMenu.back_to_main_menu
    )
    await bot.send_message(
        user_id,
        text="Вкажіть область (територію), у якій потрібна допомога.",
        reply_markup=kb.helpRequestMenu.batched_region_list[0],
    )
    await st.HelpRequestStates.waiting_for_region.set()


@dp.message_handler(text=[ButtonTexts.i_want_to_offer_help], state=[st.MainMenuStates.in_Main_menu])
async def process_give_help_button(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(
        user_id,
        text="Оберіть вид допомоги. Використовуйте кнопки внизу⬇",
        reply_markup=kb.giveHelpMenu.give_help_menu_kb,
    )
    await st.GiveMenuStates.in_give_help_menu.set()


@dp.message_handler(text=[ButtonTexts.donate_button], state=[st.MainMenuStates.in_Main_menu])
async def process_donate_button(message: types.Message):
    await message.answer(text=donate_text, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(text=[ButtonTexts.share_button], state=[st.MainMenuStates.in_Main_menu])
async def process_share_button(message: types.Message):
    await message.answer(text=share_text, reply_markup=kb.mainMenu.share_inline_keyboard)


@dp.message_handler(text=ButtonTexts.admin_contacts, state=st.MainMenuStates.in_Main_menu)
async def process_admin_contacts_button(message: types.Message):
    await message.answer(text=admin_contact_text, parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(text=[ButtonTexts.change_contacts], state=[st.MainMenuStates.in_Main_menu])
async def process_propose_help_button(message: types.Message):
    user_id = message.from_user.id
    phone_list = db.people_table.get_human_phone_list(user_id)
    phone_values = phone_list.values()
    await bot.send_message(
        user_id,
        text=f"Введені контакти\nТелефони: {', '.join(phone_values)}\n ",
        reply_markup=kb.mainMenu.change_contacts_kb,
    )


@dp.callback_query_handler(
    lambda c: c.data == ButtonTexts.callback_data_change_contacts,
    state=[st.MainMenuStates.in_Main_menu],
)
async def process_disapprove_contacts(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)
    await callback_query.message.answer(
        text="Вкажіть номер телефону у форматі +380XXXXXXXXX.'", reply_markup=ReplyKeyboardRemove()
    )
    await st.ChangeContactsStates.waiting_for_new_phone.set()


@dp.message_handler(
    regexp=phone_reg,
    content_types=types.ContentTypes.TEXT,
    state=st.ChangeContactsStates.waiting_for_new_phone,
)
async def process_message_new_phone_input(message: types.Message):
    user_id = message.from_user.id
    phone_list = db.people_table.get_human_phone_list(user_id)
    phone_list[len(phone_list) + 1] = message.text
    db.people_table.update_human_phone_list(user_id, phone_list)
    await bot.send_message(message.from_user.id, text="Дані успішно доповнено!", reply_markup=kb.mainMenu.main_menu_kb)
    await st.MainMenuStates.in_Main_menu.set()


@dp.message_handler(
    lambda message: not re.search(phone_reg, message.text),
    content_types=types.ContentTypes.TEXT,
    state=st.ChangeContactsStates.waiting_for_new_phone,
)
async def process_contact_response(message: types.Message):
    await message.reply(text="Перевірте введені дані")
