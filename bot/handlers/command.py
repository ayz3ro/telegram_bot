from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.db.requests import new_user, get_users
from bot.kb.start_kb import start_kb

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    username = message.from_user.username
    chat_id = message.from_user.id
    user_first_name = message.from_user.first_name
    if chat_id not in get_users():
        new_user(chat_id, username, user_first_name)
    await message.reply(text="Hello 👋 Welcome to the Ayz3ro Support Chat!\n\nHow can we help you today?", reply_markup=start_kb)


@router.message(Command('admin_panel'))
async def admin_menu(message: Message):
    pass
