from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ..base import BaseHelpMenu, create_inline_keyboard
from .constants import i_can_help_calls_btns, i_can_help_types_btns
from .volunteer_register_button_texts import VolunteerRegisterButtonTexts as ButtonTexts


class VolunteerRegisterMenu(BaseHelpMenu):
    def __init__(self):
        super().__init__()

        other_help_inline = InlineKeyboardButton(ButtonTexts.other_help, callback_data=ButtonTexts.other_help_callback)
        self.__inline_can_help = create_inline_keyboard(
            i_can_help_types_btns, i_can_help_calls_btns, ButtonTexts.callbackd_data_i_can_do_prefix
        ).add(other_help_inline)

        military_experience_present = InlineKeyboardButton(
            ButtonTexts.military_experience_present, callback_data=ButtonTexts.military_experience_present_callback
        )
        military_experience_missing = InlineKeyboardButton(
            ButtonTexts.military_experience_missing, callback_data=ButtonTexts.military_experience_missing_callback
        )

        self.__military_experience_check = InlineKeyboardMarkup(row_width=2).add(
            military_experience_present, military_experience_missing
        )

        medical_experience_present = InlineKeyboardButton(
            ButtonTexts.medical_experience_present, callback_data=ButtonTexts.medical_experience_present_callback
        )
        medical_experience_missing = InlineKeyboardButton(
            ButtonTexts.medical_experience_missing, callback_data=ButtonTexts.medical_experience_missing_callback
        )

        self.__medical_experience_check = InlineKeyboardMarkup(row_width=2).row(
            medical_experience_present, medical_experience_missing
        )

    @property
    def inline_can_help(self):
        return self.__inline_can_help

    @property
    def military_experience_check(self):
        return self.__military_experience_check

    @property
    def medical_experience_check(self):
        return self.__medical_experience_check
