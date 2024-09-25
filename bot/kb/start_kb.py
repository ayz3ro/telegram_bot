from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.start_callback import StartCallback

already_user = InlineKeyboardButton(text="I'm already a user",
                                    callback_data=StartCallback(action="already_user").pack())
newby = InlineKeyboardButton(text="I want to connect the service",
                             callback_data=StartCallback(action="newby").pack())
start_kb = InlineKeyboardMarkup(inline_keyboard=[[already_user], [newby]])
