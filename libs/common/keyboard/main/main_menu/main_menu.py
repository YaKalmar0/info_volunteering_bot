from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from .main_menu_button_texts import MainMenuButtonTexts as ButtonTexts


class MainMenu:
    def __init__(self):
        i_need_help = KeyboardButton(ButtonTexts.i_need_help_button)
        i_propose_help = KeyboardButton(ButtonTexts.i_want_to_offer_help)
        change_contacts = KeyboardButton(ButtonTexts.change_contacts)
        donate_button = KeyboardButton(ButtonTexts.donate_button)
        share_button = KeyboardButton(ButtonTexts.share_button)
        contact_admin_button = KeyboardButton(ButtonTexts.admin_contacts)

        self.__main_menu_kb = (
            ReplyKeyboardMarkup(resize_keyboard=True)
            .row(i_need_help, i_propose_help)
            .row(donate_button, share_button)
            .add(contact_admin_button)
            .add(change_contacts)
        )

        disapprove_contacts = InlineKeyboardButton(
            ButtonTexts.change_contacts,
            callback_data=ButtonTexts.callback_data_change_contacts,
        )
        self.__change_contacts = InlineKeyboardMarkup(row_width=1).row(disapprove_contacts)

        share_inline_button = InlineKeyboardButton(
            text=ButtonTexts.share_inline_button,
            url="https://telegram.me/share/url?url=http://t.me/volonterarmy_bot&"
            "text=Мета цього чат-боту — допомогти організувати безпечну, "
            "надійну роботу волонтерів та упорядкувати систему запитів. "
            "Тут твій запит на допомогу або готовність допомогти почують "
            "та скоординують люди. "
            "Долучайтесь!",
        )

        self.__share_inline_keyboard = InlineKeyboardMarkup(row_width=1).add(share_inline_button)

    @property
    def main_menu_kb(self):
        return self.__main_menu_kb

    @property
    def change_contacts_kb(self):
        return self.__change_contacts

    @property
    def share_inline_keyboard(self):
        return self.__share_inline_keyboard
