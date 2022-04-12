from aiogram.types import InlineKeyboardButton

from ..base import BaseHelpButtonTexts as ButtonTexts
from ..base import BaseHelpMenu, create_inline_keyboard
from .constants import *


class HelpRequestMenu(BaseHelpMenu):
    def __init__(self):
        super().__init__()

        self.__help_inline_keyboard = create_inline_keyboard(
            help_types_btns, help_types_calls, prefix=ButtonTexts.callback_data_prefix_for_help
        ).add(self._own_help)

    @property
    def help_inline_keyboard(self):
        return self.__help_inline_keyboard
