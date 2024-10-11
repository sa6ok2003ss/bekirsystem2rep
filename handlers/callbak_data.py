import asyncio
import json
import time

print(2)
from aiogram import types

from misc import dp, bot
from .sqlit import change_status,get_username,update_status, change_all
from .sqlit import reg_user, get_username, change_prokladka, get_data_tag
import random

text_dogon = """<b>Аяяй я смотрю, кто-то решил
пошалить 😏

Посмотри сначала видео, чтобы полностью во всем разобраться🙏🙃</b>"""


text_stop = """<b>Даже Ванга не знает, <i>почему ты ещё не с нами🤯</i> </b>

Я вижу ты ещё не посмотрел(а) следующий пост, а ведь ты так хотел(а) начать действовать, видимо есть очередная отговорка... 
<b><i>Ты все еще можешь получить доступ к эксклюзивной информации.</i>

Жми кнопку ниже👇</b>
"""

time_flag = 1 # 0 - режим разработчика, где отключены тайм.слипы

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext




content = -1002175079539
reg_user(1,'1')  # Запуск в БД
class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()

async def check_time(id, time1):
    now_time = time.time()
    last_time = get_data_tag(id)

    if (now_time-float(last_time)) < time1:
        await bot.send_message(chat_id=id, text= text_dogon)
        return 0
    else:
        change_prokladka(id, now_time)
        return 1




async def progrev(state, chat_id, call_data, meta):
    markup_dogon = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="ПРОДОЛЖИТЬ⏯", callback_data = call_data)
    markup_dogon.add(bat_a)

    markup_dogon2 = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="ВОСКРЕСИТЬ💀", callback_data = call_data)
    markup_dogon2.add(bat_a)

    if time_flag == 1:
        await asyncio.sleep(60)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.send_message(chat_id = chat_id, text = text_stop, reply_markup = markup_dogon)
    else:
        return


    if time_flag == 1:
        await asyncio.sleep(3600)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id = chat_id, message_id = 163, reply_markup=markup_dogon)
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=chat_id, message_id = 165, reply_markup=markup_dogon)
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=chat_id, message_id = 167, reply_markup=markup_dogon2)
    else:
        return



async def progrev2(state, chat_id, call_data, meta):
    markup_dogon = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="ПРОДОЛЖИТЬ⏯", callback_data = call_data)
    markup_dogon.add(bat_a)

    markup_dogon2 = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="ВОСКРЕСИТЬ💀", callback_data = call_data)
    markup_dogon2.add(bat_a)

    if time_flag == 1:
        await asyncio.sleep(300)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.send_message(chat_id = chat_id, text = text_stop, reply_markup = markup_dogon)
    else:
        return


    if time_flag == 1:
        await asyncio.sleep(3600)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id = chat_id, message_id = 163, reply_markup=markup_dogon)
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=chat_id, message_id = 165, reply_markup=markup_dogon)
    else:
        return

    if time_flag == 1:
        await asyncio.sleep(86400)
    if ((await state.get_data())[meta]) != 'ready': # Человек бездействует 24 часа
        await bot.copy_message(from_chat_id=content, chat_id=chat_id, message_id = 167, reply_markup=markup_dogon2)
    else:
        return


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, '1')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    update_status(message.chat.id, 0)

    await state.update_data(v00='stop')

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text="🚀ПОГНАЛИ🚀", callback_data = 'go_02')
    markup.add(bat_a)

    q = await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=186)
    await asyncio.sleep(10)
    await bot.edit_message_reply_markup(message_id=q.message_id, chat_id=message.chat.id, reply_markup=markup)


    await progrev(state = state, chat_id = message.chat.id, call_data = 'go_2', meta = 'v0')



@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    await bot.answer_callback_query(call.id)
    if call.data == 'go_02':
        update_status(call.message.chat.id, 1)
        await state.update_data(v00='ready')
        await state.update_data(v01='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🔥Давай🔥', callback_data='go_03')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=188)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=190)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=192)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=193, reply_markup=markup)

        await progrev(state=state, chat_id=call.message.chat.id, call_data='go_03', meta='v01')



    if call.data == 'go_03':
        update_status(call.message.chat.id, 2)
        await state.update_data(v01='ready')
        await state.update_data(v02='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='А что за Идея❓', callback_data='go_04')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=195, reply_markup=markup)
        await progrev(state=state, chat_id=call.message.chat.id, call_data='go_04', meta='v02')


    if call.data == 'go_04':
        update_status(call.message.chat.id, 3)
        await state.update_data(v02='ready')
        await state.update_data(v03='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ДАЛЕЕ🔥', callback_data='go_05')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=197, reply_markup=markup)
        await progrev(state=state, chat_id=call.message.chat.id, call_data='go_05', meta='v03')


    if call.data == 'go_05':
        now_time = time.time()
        change_prokladka(call.message.chat.id, now_time)
        update_status(call.message.chat.id, 4)
        await state.update_data(v03='ready')
        await state.update_data(v04='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='💦ДАЛЬШЕ💦', callback_data='go_4')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=199,reply_markup=markup)
        await progrev(state=state, chat_id=call.message.chat.id, call_data='go_4', meta='v04')


        #-----------------------



    if call.data == 'go_4':
        now_time = time.time()
        change_prokladka(id, now_time)
        update_status(call.message.chat.id, 5)
        await state.update_data(v04='ready')
        await state.update_data(v3='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='🧠ТЕСТ🧠', callback_data='go_5')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=135, reply_markup=markup)
        await progrev2(state=state, chat_id=call.message.chat.id, call_data='go_5', meta='v3')


    if call.data == 'go_5':
        if (await check_time(call.message.chat.id, 40)) == 1:
            update_status(call.message.chat.id, 6)
            await state.update_data(v3='ready')
            await state.update_data(v4='stop')
            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='1️⃣', callback_data='go_6')
            bat_a2 = types.InlineKeyboardButton(text='2️⃣', callback_data='go_false')
            bat_a3 = types.InlineKeyboardButton(text='3️⃣', callback_data='go_false')
            markup.add(bat_a1, bat_a2, bat_a3)

            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=137, reply_markup=markup)
            await progrev2(state=state, chat_id=call.message.chat.id, call_data='go_6', meta='v4')


    if call.data == 'go_false':

        await bot.send_message(chat_id=call.message.chat.id, text="<b>Нет, это не арбитраж трафика. Пересмотри видео и попробуй ещё раз🙃</b>")


    if call.data == 'go_6':
        now_time = time.time()
        change_prokladka(id, now_time)

        update_status(call.message.chat.id, 7)
        await state.update_data(v4='ready')
        await state.update_data(v5='stop')
        markup = types.InlineKeyboardMarkup()
        bat_a1 = types.InlineKeyboardButton(text='📌КНОПОЧКА📌', callback_data='go_7')
        markup.add(bat_a1)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=140)
        await asyncio.sleep(1)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=143, reply_markup=markup)

        await progrev2(state=state, chat_id=call.message.chat.id, call_data='go_7', meta='v5')



    if call.data == 'go_7':
        if (await check_time(call.message.chat.id, 40 )) == 1:
            update_status(call.message.chat.id, 8)
            await state.update_data(v5='ready')

            markup = types.InlineKeyboardMarkup()
            bat_a1 = types.InlineKeyboardButton(text='Мой ТГ✅', url=f'https://t.me/StealthSystem')
            markup.add(bat_a1)

            markup2 = types.InlineKeyboardMarkup()
            bat_a2 = types.InlineKeyboardButton(text='ОТЗЫВЫ 💬✨',url=f'https://t.me/BekirOtzivi')
            markup2.add(bat_a2)

            markup3 = types.InlineKeyboardMarkup()
            markup3.add(bat_a1)
            markup3.add(bat_a2)



            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=146, reply_markup=markup)


            if time_flag == 1:
                await asyncio.sleep(300)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=160,reply_markup=markup2)

            if time_flag == 1:
                await asyncio.sleep(3600)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=170,reply_markup=markup3)


            if time_flag == 1:
                await asyncio.sleep(86400)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=172, reply_markup=markup3)

            if time_flag == 1:
                await asyncio.sleep(86400)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=174, reply_markup=markup3)
