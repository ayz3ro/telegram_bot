from aiogram import Router, types
from aiogram.filters.callback_data import CallbackData

router = Router()


class StartCallback(CallbackData, prefix="start_callback"):
    action: str


@router.callback_query(StartCallback.filter())
async def callback_handler(call: types.CallbackQuery, callback_data: StartCallback):
    if callback_data.action == "already_user":
        await call.message.answer("You are already user")
    elif callback_data.action == "newby":
        await call.message.answer("You are newby")
    await call.answer()
