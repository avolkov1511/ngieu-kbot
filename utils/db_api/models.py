from sqlalchemy import (Column, Integer, String, Sequence)
from sqlalchemy import sql
from utils.db_api.database import db


# Создаем класс таблицы товаров
class Button(db.Model):
    __tablename__ = 'buttons'
    query: sql.Select

    # Уникальный идентификатор кнопки
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # Код категории (для отображения в колбек дате)
    category_code = Column(String(50))

    # Название категории (для отображения в кнопке)
    category_name = Column(String(50))

    # Код подкатегории (для отображения в колбек дате)
    subcategory_code = Column(String(50))

    # Название подкатегории (для отображения в кнопке)
    subcategory_name = Column(String(50))

    # Кнопка и информация по кнопке
    info = Column(String(100000))
    button = Column(String(50))

    def __repr__(self):
        return f"""
 {self.id} - "{self.info}"""