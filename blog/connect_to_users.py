import asyncio     
from aiogram import Bot, Dispatcher  
from aiogram.filters import Command
from datetime import datetime
import time
 
import os  

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'blog.settings')

import django
django.setup()

from article.models import Article

# вот это вот всё ТОЛЬКО после подключения джанго
from secret import TOKEN 
dp = Dispatcher()         
bot = Bot(token=TOKEN) 

from asgiref.sync import sync_to_async
@sync_to_async
def get_data():
    return list(Article.objects.all())

@dp.message(Command("start"))
async def command_start_handler(message):
    print('Ура! Мне написал', message.chat.id)
    await message.answer(
        "Я веду канал космических событий! https://t.me/n_esse")

# Разбуди меня во время 
@dp.message(Command("writeme"))
async def command_writeme_handler(message):
    text = message.text
    texts = text.split(' ')
    text_date = str(texts[1]).split('-')
    text_time = str(texts[2]).split(':')

    date = datetime(int(text_date[0]), int(text_date[1]), int(text_date[2]), 
                    int(text_time[0]), int(text_time[1]))
    now_date = datetime.now()
    
    total_time = (date - now_date).total_seconds()

    await message.answer(f'Вы попросили разбудить вас в {str(date)}' )
    time.sleep(total_time)
    await message.answer(f'Бужу вас!' )

# Вывод заголовков из Article
@dp.message(Command("whatsnew"))
async def command_start_handler(message):
    data = await get_data()
    data_text = ''
    for d in data:
        print(d.title)
        data_text += (d.title + '\n')
    await message.answer(
        data_text)



from asgiref.sync import sync_to_async
@sync_to_async
def get_data():
    return list(Article.objects.all())
   

asyncio.run(           
    dp.start_polling(  
        bot))          



