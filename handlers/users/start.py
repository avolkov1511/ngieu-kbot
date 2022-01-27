from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db

from keyboards.keyboard.menu import menu

@dp.message_handler(CommandStart())
async def bot_start(m: types.Message):
    if (not db.subscriber_exists(m.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(m.from_user.id)

    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(m.from_user.id, True)

    await m.answer_sticker(r'CAACAgIAAxkBAAEDwM5h8FSAYXAxh54lpHdbZGIl5tSJUAACbwAD29t-AAGZW1Coe5OAdCME')
    await m.answer(f"Привет, {m.from_user.full_name}!\n"
                   f"Я K-bot, university mentor :-)\n"
                   f"Я помогаю студентам, абитуриентам НГИЭУ быстро находить нужную информацию.\n"
                   f"Скорее выбирай раздел в Главном меню – я знаю много интересного про университет!", reply_markup=menu)