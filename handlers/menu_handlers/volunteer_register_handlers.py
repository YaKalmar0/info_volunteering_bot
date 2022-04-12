from aiogram import types
from aiogram.dispatcher import FSMContext

from libs.common import keyboard as kb
from libs.common import states as st
from libs.common.keyboard.main import VolunteerRegisterButtonTexts
from libs.database import db
from misc import bot, dp


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.callback_data_prefix_change_region),
    state=st.VolunteerRegisterStates.waiting_for_region,
)
async def process_message_change_region_kb(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=1)
    message_id = callback_query.message.message_id
    user_id = callback_query.message.chat.id

    target_menu = int(callback_query.data.replace(VolunteerRegisterButtonTexts.callback_data_prefix_change_region, ""))
    await bot.edit_message_reply_markup(
        chat_id=user_id, message_id=message_id, reply_markup=kb.helpRequestMenu.batched_region_list[target_menu]
    )


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.callback_data_prefix_region),
    state=st.VolunteerRegisterStates.waiting_for_region,
)
async def process_message_region_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)

    region_name = callback_query.data.replace(VolunteerRegisterButtonTexts.callback_data_prefix_region, "")
    await state.update_data(region=region_name)
    region_id = db.regions_table.select_region(region_name)

    await callback_query.message.answer(
        text="Вкажіть ваш населений пункт (місто\село):",
        reply_markup=kb.helpRequestMenu.cities_keyboard(region_id=region_id),
    )
    await st.VolunteerRegisterStates.waiting_for_city.set()


@dp.callback_query_handler(
    lambda c: c.data == VolunteerRegisterButtonTexts.callback_data_own_city,
    state=st.VolunteerRegisterStates.waiting_for_city,
)
async def process_own_city(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)

    await callback_query.message.answer(text="Введіть назву населеного пункту:")
    await st.VolunteerRegisterStates.waiting_for_city_input.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=st.VolunteerRegisterStates.waiting_for_city_input)
async def process_city_input(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await bot.send_message(
        message.from_user.id, text="Вкажіть район в населеному пункті:"
    )
    await st.VolunteerRegisterStates.waiting_for_district.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.callback_data_prefix_city),
    state=st.VolunteerRegisterStates.waiting_for_city,
)
async def process_city_key_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)

    city_name = callback_query.data.replace(VolunteerRegisterButtonTexts.callback_data_prefix_city, "")
    await state.update_data(city=city_name)
    await callback_query.message.answer(text="Вкажіть район в населеному пункті:")
    await st.VolunteerRegisterStates.waiting_for_district.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.VolunteerRegisterStates.waiting_for_district,
)
async def process_message_district_input(message: types.Message, state: FSMContext):
    await state.update_data(district=message.text)
    await bot.send_message(message.from_user.id, text="Вкажіть адресу:")
    await st.VolunteerRegisterStates.waiting_for_address.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.VolunteerRegisterStates.waiting_for_address,
)
async def process_address_input(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await bot.send_message(
        message.from_user.id,
        text="Чи маєте ви війсковий досвід?",
        reply_markup=kb.volunteerRegisterMenu.military_experience_check,
    )
    await st.VolunteerRegisterStates.waiting_for_military_experience.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.military_experience_present_prefix),
    state=st.VolunteerRegisterStates.waiting_for_military_experience,
)
async def process_military_experience(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    mil_exp = callback_query.data.replace(VolunteerRegisterButtonTexts.military_experience_present_prefix, "")
    await state.update_data(mil_exp=mil_exp)
    await callback_query.message.answer(
        text="Чи є у вас медичний досвід?", reply_markup=kb.volunteerRegisterMenu.medical_experience_check
    )
    await st.VolunteerRegisterStates.waiting_for_medical_experience.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.medical_experience_present_prefix),
    state=st.VolunteerRegisterStates.waiting_for_medical_experience,
)
async def process_medical_experience(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    med_exp = callback_query.data.replace(VolunteerRegisterButtonTexts.medical_experience_present_prefix, "")
    await state.update_data(med_exp=med_exp)
    await callback_query.message.answer(
        text="Чим ви можете допомогти?", reply_markup=kb.volunteerRegisterMenu.inline_can_help
    )
    await st.VolunteerRegisterStates.waiting_for_i_can_help_keys.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(VolunteerRegisterButtonTexts.callbackd_data_i_can_do_prefix),
    state=st.VolunteerRegisterStates.waiting_for_i_can_help_keys,
)
async def process_i_can_help_keys(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    user_id = callback_query.from_user.id
    i_can_help = callback_query.data.replace(VolunteerRegisterButtonTexts.callbackd_data_i_can_do_prefix, "")
    await state.update_data(i_can_do=i_can_help)

    data = await state.get_data()

    human_id = db.people_table.get_human_id(user_id)
    db.volunteer_table.create_volunteer(human_id, data)

    await state.reset_data()
    await callback_query.message.answer(
        text="Дякуємо за звернення. Ваш запит передано адміністрації", reply_markup=kb.mainMenu.main_menu_kb
    )
    await st.MainMenuStates.in_Main_menu.set()


@dp.callback_query_handler(
    lambda c: c.data == VolunteerRegisterButtonTexts.other_help_callback,
    state=st.VolunteerRegisterStates.waiting_for_i_can_help_keys,
)
async def process_i_can_help_own(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)
    await callback_query.message.answer(text="Введіть інформацію")
    await st.VolunteerRegisterStates.waiting_for_i_can_help_input.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT, state=st.VolunteerRegisterStates.waiting_for_i_can_help_input
)
async def process_i_can_help_input(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(i_can_do="other", other_help=message.text)

    data = await state.get_data()

    human_id = db.people_table.get_human_id(user_id)
    db.volunteer_table.create_volunteer(human_id, data)

    await state.reset_data()
    await bot.send_message(
        user_id, text="Дякуємо за звернення. Ваш запит передано адміністрації", reply_markup=kb.mainMenu.main_menu_kb
    )
    await st.MainMenuStates.in_Main_menu.set()
