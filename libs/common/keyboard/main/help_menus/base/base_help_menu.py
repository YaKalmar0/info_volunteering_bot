from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from libs.database import db

from .base_help_button_texts import BaseHelpButtonTexts as ButtonTexts
from .shared import (
    create_inline_keyboard,
    delivery_types_btns,
    delivery_types_calls,
    payment_types_btns,
    payment_types_calls,
)


def create_regions_keyboard_list(batch_size: int):
    regions_list = db.regions_table.select_regions()
    regions_list.sort()
    batched_regions_list = [regions_list[d : d + batch_size] for d in range(0, len(regions_list), batch_size)]
    inline_keyboard_array_cities = [
        create_inline_keyboard(region_batch, region_batch, ButtonTexts.callback_data_prefix_region, 2)
        for region_batch in batched_regions_list
    ]
    amount_of_menus = len(inline_keyboard_array_cities)
    inline_keyboard_array_with_arrows = [
        inline_keyboard_array_cities[i].row(
            InlineKeyboardButton(
                ButtonTexts.regions_left,
                callback_data=ButtonTexts.callback_data_prefix_change_region + str((i - 1) % amount_of_menus),
            ),
            InlineKeyboardButton(
                ButtonTexts.regions_right,
                callback_data=ButtonTexts.callback_data_prefix_change_region + str((i + 1) % amount_of_menus),
            ),
        )
        for i in range(amount_of_menus)
    ]
    return inline_keyboard_array_with_arrows


class BaseHelpMenu:
    def __init__(self):
        back_to_main_menu = KeyboardButton(ButtonTexts.back_to_main_menu)
        self.__back_to_main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(back_to_main_menu)
        self._own_help = InlineKeyboardButton(ButtonTexts.own_help, callback_data=ButtonTexts.callback_data_own_help)

        self.__payment_inline_keyboard = create_inline_keyboard(
            payment_types_btns, payment_types_calls, ButtonTexts.callback_data_prefix_payments
        )

        self.__inline_can_help = create_inline_keyboard(
            delivery_types_btns, delivery_types_calls, ButtonTexts.callback_data_prefix_transfer
        )

        skip_org = InlineKeyboardButton(ButtonTexts.skip_org, callback_data=ButtonTexts.callback_data_skip_org)
        self.__inline_skip_org = InlineKeyboardMarkup(row_width=1).add(skip_org)

        self.__batched_region_list = create_regions_keyboard_list(6)

    @property
    def payment_inline_keyboard(self):
        return self.__payment_inline_keyboard

    @property
    def inline_skip_org(self):
        return self.__inline_skip_org

    @property
    def transfer_inline_keyboard(self):
        return self.__inline_can_help

    @property
    def batched_region_list(self):
        return self.__batched_region_list

    @property
    def back_to_main_menu(self):
        return self.__back_to_main_menu

    @staticmethod
    def cities_keyboard(region_id: int):
        cities_list = db.cities_table.get_cities(region_id)
        own_city = InlineKeyboardButton(ButtonTexts.own_city, callback_data=ButtonTexts.callback_data_own_city)
        return create_inline_keyboard(cities_list, cities_list, ButtonTexts.callback_data_prefix_city, 2).add(own_city)
