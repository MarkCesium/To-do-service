from aiogram import F, Router
import aiohttp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router_common = Router()


@router_common.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Hello!"
             "I am alive=)"
    )


@router_common.message(Command(commands=["ping"]))
async def ping_pong(message: Message, state: FSMContext):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('http://to-do-backend/ping') as response:
            msg_text = await response.json()
            await message.answer(
                text=str(msg_text["answer"])
            )


@router_common.message(Command(commands=["cancel"]))
@router_common.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено"
    )
