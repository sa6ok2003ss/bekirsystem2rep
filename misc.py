import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '7792778926:AAFwRe9mvRg5cOOZ3G6810H4zaliWB2Y9mQ'
memory_storage = MemoryStorage()
print(1)
bot = Bot(token=TOKEN,parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)
print(2)