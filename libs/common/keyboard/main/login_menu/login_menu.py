from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .login_menu_button_texts import LoginMenuButtonTexts as ButtonsTexts


class LoginMenu:
    def __init__(self):
        request_contact_button = KeyboardButton(ButtonsTexts.request_contact, request_contact=True)
        self.__request_contact_inline_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(request_contact_button)

    @property
    def request_contact_inline_kb(self):
        return self.__request_contact_inline_kb
