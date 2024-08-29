from os import getenv

from aiogram import Bot

bot = Bot(token=getenv('TELEGRAM_TOKEN'))
