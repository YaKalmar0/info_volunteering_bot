from aiogram import types

from libs.common import keyboard as kb
from libs.common import states as st
from libs.common.keyboard.main import GiveHelpMenuTexts as ButtonTexts
from misc import bot, dp


@dp.message_handler(text=[ButtonTexts.i_propose_resources_button], state=[st.GiveMenuStates.in_give_help_menu])
async def process_propose_resources_button(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(
        user_id,
        text="Важливо! Дайте відповідь на всі запитання. Це допоможе нам швидко знайти, кому саме ви потрібні!!",
        reply_markup=kb.helpProposalMenu.back_to_main_menu
    )
    await bot.send_message(
        user_id,
        text="Вкажіть область (територію), у якій Ви можете надати допомогу.",
        reply_markup=kb.helpProposalMenu.batched_region_list[0],
    )
    await st.HelpProposalStates.waiting_for_region.set()


@dp.message_handler(text=[ButtonTexts.i_want_to_volunteer], state=[st.GiveMenuStates.in_give_help_menu])
async def process_propose_help_button(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(
        user_id,
        text="Важливо! Дайте відповідь на всі запитання. Це допоможе нам швидко знайти, кому саме ви потрібні!!",
        reply_markup=kb.helpProposalMenu.back_to_main_menu
    )
    await bot.send_message(
        user_id,
        text="Вкажіть область (територію), у якій Ви можете надати допомогу.",
        reply_markup=kb.volunteerRegisterMenu.batched_region_list[0],
    )
    await st.VolunteerRegisterStates.waiting_for_region.set()


@dp.message_handler(text=ButtonTexts.back_button, state=st.GiveMenuStates.in_give_help_menu)
async def process_back_button(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="🏡 Головне меню. Використовуйте кнопки внизу👇",
        reply_markup=kb.mainMenu.main_menu_kb,
    )
    await st.MainMenuStates.in_Main_menu.set()
