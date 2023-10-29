from aiogram import Router
import aiohttp
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router_tasks = Router()


@router_tasks.message(Command(commands=["tasks"]))
async def get_tasks(message: Message, state: FSMContext):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('http://to-do-backend/tasks') as response:
            msg_text = await response.text()
            await message.answer(
                text=str(msg_text)
            )
