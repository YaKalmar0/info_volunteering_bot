from aiogram import types
from aiogram.dispatcher import FSMContext

from libs.common import keyboard as kb
from libs.common import states as st
from libs.common.keyboard.main import HelpProposalButtonTexts
from misc import bot, db, dp

from ..constants import user_roles


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_change_region),
    state=st.HelpProposalStates.waiting_for_region,
)
async def process_message_change_region_kb(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=1)
    message_id = callback_query.message.message_id
    user_id = callback_query.message.chat.id

    target_menu = int(callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_change_region, ""))
    await bot.edit_message_reply_markup(
        chat_id=user_id, message_id=message_id, reply_markup=kb.helpRequestMenu.batched_region_list[target_menu]
    )


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_region),
    state=st.HelpProposalStates.waiting_for_region,
)
async def process_message_region_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)

    region_name = callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_region, "")
    await state.update_data(region=region_name)
    region_id = db.regions_table.select_region(region_name)

    await callback_query.message.answer(
        text="Вкажіть ваш населений пункт (місто\село):",
        reply_markup=kb.helpRequestMenu.cities_keyboard(region_id=region_id),
    )
    await st.HelpProposalStates.waiting_for_city.set()


@dp.callback_query_handler(
    lambda c: c.data == HelpProposalButtonTexts.callback_data_own_city, state=st.HelpProposalStates.waiting_for_city
)
async def process_own_city(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)

    await callback_query.message.answer(text="Введіть назву населеного пункту:")
    await st.HelpProposalStates.waiting_for_city_input.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=st.HelpProposalStates.waiting_for_city_input)
async def process_city_input(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await bot.send_message(
        message.from_user.id, text="Вкажіть район в населеному пункті:"
    )
    await st.HelpProposalStates.waiting_for_district.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_city),
    state=st.HelpProposalStates.waiting_for_city,
)
async def process_city_key_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)

    city_name = callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_city, "")
    await state.update_data(city=city_name)
    await callback_query.message.answer(text="Вкажіть район в населеному пункті:")
    await st.HelpProposalStates.waiting_for_district.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.HelpProposalStates.waiting_for_district,
)
async def process_message_district_input(message: types.Message, state: FSMContext):
    await state.update_data(district=message.text)
    await bot.send_message(message.from_user.id, text="Вкажіть адресу:")
    await st.HelpProposalStates.waiting_for_address.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.HelpProposalStates.waiting_for_address,
)
async def process_address_input(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await bot.send_message(
        message.from_user.id,
        text="Тип допомоги:",
        reply_markup=kb.helpProposalMenu.help_inline_keyboard,
    )
    await st.HelpProposalStates.waiting_for_help_type_keys.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_for_help),
    state=st.HelpProposalStates.waiting_for_help_type_keys,
)
async def process_message_details_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    help_type = callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_for_help, "")
    await state.update_data(help_type=help_type)
    await callback_query.message.answer(
        text="Вкажіть деталі (які речі, їх кількість, тощо; вкажіть, чи є ви оптовим постачальником)",
    )
    await st.HelpProposalStates.waiting_for_help_details.set()


@dp.callback_query_handler(
    lambda c: c.data == HelpProposalButtonTexts.callback_data_own_help,
    state=st.HelpProposalStates.waiting_for_help_type_keys,
)
async def process_message_own_help(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)
    await callback_query.message.answer(text="Введіть інформацію:")
    await st.HelpProposalStates.waiting_for_help_type_input.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.HelpProposalStates.waiting_for_help_type_input,
)
async def process_message_details2_input(message: types.Message, state: FSMContext):
    await state.update_data(help_type="other", other_help=message.text)
    await bot.send_message(
        message.from_user.id,
        text="Вкажіть, будь ласка, деталі (речі, що можете надати, та, бажано, їх кількість):",
    )
    await st.HelpProposalStates.waiting_for_help_details.set()


@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.HelpProposalStates.waiting_for_help_details,
)
async def process_message_help_type_input(message: types.Message, state: FSMContext):
    await state.update_data(help_details=message.text)
    await bot.send_message(
        message.from_user.id,
        text="Чи потрібна оплата?",
        reply_markup=kb.helpProposalMenu.payment_inline_keyboard,
    )
    await st.HelpProposalStates.waiting_for_payment.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_payments),
    state=st.HelpProposalStates.waiting_for_payment,
)
async def process_message_payment_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    payment = callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_payments, "")
    await state.update_data(payment=payment)
    await callback_query.message.answer(
        text="Можливість доставки?", reply_markup=kb.helpProposalMenu.transfer_inline_keyboard
    )
    await st.HelpProposalStates.waiting_for_transfer.set()


@dp.callback_query_handler(
    lambda c: c.data.startswith(HelpProposalButtonTexts.callback_data_prefix_transfer),
    state=st.HelpProposalStates.waiting_for_transfer,
)
async def process_message_transfer_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    transfer = callback_query.data.replace(HelpProposalButtonTexts.callback_data_prefix_transfer, "")
    await state.update_data(transfer=transfer)

    user_id = callback_query.from_user.id
    data = await state.get_data()

    human_id = db.people_table.get_human_id(user_id)
    db.offer_help_table.create_offer_help_request(human_id, data)
    db.people_table.update_human_role(user_id, user_roles.get("offer_help"))

    await callback_query.message.answer(
        text="Дякуємо за звернення. Ваш запит передано адміністрації", reply_markup=kb.mainMenu.main_menu_kb
    )
    await state.reset_data()
    await st.MainMenuStates.in_Main_menu.set()


"""
EXCLUDED DUE TO CUSTOMER REQUEST

@dp.message_handler(
    content_types=types.ContentTypes.TEXT,
    state=st.HelpProposalStates.waiting_for_organization,
)
async def process_organization_input(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(org=message.text)
    data = await state.get_data()

    human_id = db.people_table.get_human_id(user_id)
    db.offer_help_table.create_offer_help_request(human_id, data)
    db.people_table.update_human_role(user_id, user_roles.get("offer_help"))

    await bot.send_message(
        message.from_user.id,
        text="Дякуємо за звернення. Ваш запит передано адміністрації",
        reply_markup=kb.mainMenu.main_menu_kb,
    )
    await state.reset_data()
    await st.MainMenuStates.in_Main_menu.set()


@dp.callback_query_handler(
    lambda c: c.data == HelpProposalButtonTexts.callback_data_skip_org,
    state=st.HelpProposalStates.waiting_for_organization,
)
async def process_skip_input(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer(cache_time=60)
    user_id = callback_query.from_user.id
    await state.update_data(org="none")
    data = await state.get_data()

    human_id = db.people_table.get_human_id(user_id)
    db.offer_help_table.create_offer_help_request(human_id, data)
    db.people_table.update_human_role(user_id, user_roles.get("offer_help"))

    await callback_query.message.answer(
        text="Дякуємо за звернення. Ваш запит передано адміністрації", reply_markup=kb.mainMenu.main_menu_kb
    )
    await state.reset_data()
    await st.MainMenuStates.in_Main_menu.set()"""
