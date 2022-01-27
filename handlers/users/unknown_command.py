from aiogram import types
from loader import dp

@dp.message_handler()
async def unknown_command(m: types.Message):
    await m.answer(f"Прости, я тебя не понял :( \n"
                         f"Попробуй еще! Нажми “назад” или “главное меню”.")