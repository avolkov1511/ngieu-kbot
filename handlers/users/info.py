from aiogram import types
from loader import dp


@dp.message_handler(text="Справка")
async def info(m: types.Message):
    text = ("Привет! Меня зовут Kbot - я помощник студентов и абитуриентов НГИЭУ!",
            "Я могу помочь тебе быстро найти нужную информацию в областях:",
            "1) поступление",
            "2) учебы",
            "3) здоровье и спорт",
            "4) новости универстета",
            "Больше не нужно долго ходить по сайтам в поиске нужной информации, ведь есть Я! )")

    await m.answer("\n".join(text))