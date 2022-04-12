from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .give_help_menu_texts import GiveHelpMenuTexts as ButtonTexts


class GiveHelpMenu:
    def __init__(self):
        i_propose_help = KeyboardButton(ButtonTexts.i_propose_resources_button)
        i_want_to_volunteer = KeyboardButton(ButtonTexts.i_want_to_volunteer)
        back_button = KeyboardButton(ButtonTexts.back_button)

        self.__give_help_menu_kb = (
            ReplyKeyboardMarkup(resize_keyboard=True).row(i_propose_help, i_want_to_volunteer).add(back_button)
        )

    @property
    def give_help_menu_kb(self):
        return self.__give_help_menu_kb
