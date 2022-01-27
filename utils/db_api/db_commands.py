from typing import List

from sqlalchemy import and_

from utils.db_api.models import Button


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_button(**kwargs):
    new_button = await Button(**kwargs).create()
    return new_button


# Функция для вывода товаров с РАЗНЫМИ категориями
async def get_categories() -> List[Button]:
    return await Button.query.distinct(Button.category_name).gino.all()


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Button]:
    return await Button.query.distinct(Button.subcategory_name).where(Button.category_code == category).gino.all()

# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_buttons(category_code, subcategory_code) -> List[Button]:
    button = await Button.query.where(
        and_(Button.category_code == category_code,
             Button.subcategory_code == subcategory_code)
    ).gino.all()
    return button


# Функция для получения объекта товара по его айди
async def get_button(button_id) -> Button:
    button = await Button.query.where(Button.id == button_id).gino.first()
    return button
