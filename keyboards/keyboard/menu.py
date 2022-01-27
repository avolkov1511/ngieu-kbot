from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню")
        ],
        [
            KeyboardButton(text="Справка")
        ],
    ],
    resize_keyboard=True, row_width= 1
)