import asyncio     
from aiogram import Bot, Dispatcher  
from aiogram.filters import Command
 
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
    
@dp.message(Command("writeme"))
async def command_writeme_handler(message):
    text = message.text
    texts = text.split(' ')
    print(texts)
    await message.answer('Вы попросили разбудить вас в ' + texts[1] + ' ' + texts[2])

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



