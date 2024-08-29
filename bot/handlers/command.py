from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from bot_token import bot

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    username = message.from_user.username
    chat_id = message.from_user.id
    user_first_name = message.from_user.first_name
    await message.reply(f"Привіт користувачу {user_first_name, username, chat_id}, чим я можу тобі допомогти?")


@router.message(Command('admin_panel'))
async def admin_menu(message: Message):
    if message.from_user.id == 748450788:
        keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='6872674490')]], resize_keyboard=True)

        await message.reply('Виберіть користувача зі списку для надання допомоги:', reply_markup=keyboard)
    else:
        await message.reply('Команда доступна тільки адміністраторам')


@router.message(lambda message: message.text.isdigit())
async def select_user(message: Message):
    if message.from_user.id == 748450788:
        await message.reply(f"Ви вибрали користувача з ID: {message.text}")
    else:
        await message.reply("Ця команда доступна тільки адміністратору.")


@router.message(lambda message: message.from_user.id == 748450788)
async def forward_message_to_user(message: Message):
    await bot.send_message(6872674490, message.text)


@router.message(lambda message: message.from_user.id == 6872674490)
async def forward_message_to_admin(message: Message):
    await bot.send_message(748450788, f"Повідомлення від користувача {6872674490}: {message.text}")
