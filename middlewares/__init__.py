# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from loguru import logger
# from aiogram import Dispatcher
#
#
# def setup(dp: Dispatcher):
#     dp.middleware.setup(LoggingMiddleware())
#     logger.info('Middlewares are successfully configured')

from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
