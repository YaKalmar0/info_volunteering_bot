from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminMenuStates(StatesGroup):
    in_Admin_menu = State()
    waiting_for_new_admin_id = State()
    waiting_for_ban_id = State()
    waiting_for_unban_id = State()


class MainMenuStates(StatesGroup):
    in_Main_menu = State()


class GiveMenuStates(StatesGroup):
    in_give_help_menu = State()


class UserStates(StatesGroup):
    banned_user = State()


class LoginStates(StatesGroup):
    waiting_for_contact = State()
    waiting_for_full_name = State()


class HelpRequestStates(StatesGroup):
    waiting_for_region = State()
    waiting_for_city = State()
    waiting_for_city_input = State()
    waiting_for_district = State()
    waiting_for_address = State()
    waiting_for_help_type_keys = State()
    waiting_for_help_type_input = State()
    waiting_for_payment = State()
    waiting_for_help_details = State()
    waiting_for_transfer = State()
    waiting_for_organization = State()


class HelpProposalStates(StatesGroup):
    waiting_for_region = State()
    waiting_for_city = State()
    waiting_for_city_input = State()
    waiting_for_district = State()
    waiting_for_address = State()
    waiting_for_help_type_keys = State()
    waiting_for_help_type_input = State()
    waiting_for_help_details = State()
    waiting_for_payment = State()
    waiting_for_transfer = State()
    waiting_for_organization = State()


class VolunteerRegisterStates(StatesGroup):
    waiting_for_region = State()
    waiting_for_city = State()
    waiting_for_city_input = State()
    waiting_for_district = State()
    waiting_for_address = State()
    waiting_for_military_experience = State()
    waiting_for_medical_experience = State()
    waiting_for_i_can_help_keys = State()
    waiting_for_i_can_help_input = State()


class ChangeContactsStates(StatesGroup):
    waiting_for_contacts_check = State()
    waiting_for_new_phone = State()
    waiting_for_new_messenger = State()
