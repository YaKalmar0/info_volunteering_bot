from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_inline_keyboard(text_btn, call_btn, prefix="", row_width=1):
    keyboard = InlineKeyboardMarkup(row_width=row_width)
    for t, c in zip(text_btn, call_btn):
        callback = prefix + str(c)
        keyboard.insert(InlineKeyboardButton(str(t), callback_data=callback))
    return keyboard


__all__ = ["create_inline_keyboard"]
