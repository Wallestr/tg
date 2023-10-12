from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from config import TOKEN
from config import ADMIN_ID
import mouse
from aiogram.types import InputFile

import pyautogui as pag
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import webbrowser
import keyboard
from aiogram.types.web_app_info import WebAppInfo
from glob import glob
import requests
from bs4 import BeautifulSoup 
import json


# ADMIN = 6615226705

    
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

main = ReplyKeyboardMarkup( resize_keyboard=True)
main.add('screenshot', 'Twitch on')
main.add('power off', 'power on')
main.add( types.KeyboardButton('WebSite', web_app=WebAppInfo(url='https://wallestr.github.io/tg/mainTg.HTML')))

main_powerOff = ReplyKeyboardMarkup( resize_keyboard=True)
main_powerOff.add('ok' , 'NO')

print(pag.size())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'{message.from_user.first_name } Добро пожаловать в панель управления компьютером', reply_markup=main)


    # if message.from_user.id == ADMIN_ID:
    #     await message.answer(f'Вы допущены', reply_markup=main)
    # else:
    #     await message.answer('Вы не допущены опездол')


@dp.message_handler(commands=['id'])
async def id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(text = 'screenshot')
async def scren(message: types.Message):

    

    
    screeen = pag.screenshot()
    print("сделан скрин")

    
    pag.screenshot('scren11.png')
    print("сохранение скрина")

    
    screeen = open('scren11.png', 'rb')
    print("открытие скрин")

    await message.answer_photo(screeen)
    print("отправка скрин")


@dp.message_handler(text = 'power off')
async def power(message: types.Message):

    
    
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Подтверждаю', callback_data="Off")
    ib2 = InlineKeyboardButton(text='отмена', callback_data="ON")
    ikb.add(ib1, ib2)
    
    await message.answer(f'Подтвердите выключение ПК ', reply_markup=ikb)

@dp.callback_query_handler()
async def confirm(callback: types.CallbackQuery):
    if callback.data == "Off":
         await callback.answer(text=f'Ваш ПК выключиться через 10 секунд {os.system ("shutdown /s /t 10")}', show_alert=True)
    if callback.data =="ON":
         await callback.answer(text="Отмена выключения ПК ", show_alert=True)



@dp.message_handler(text = 'power on')
async def powerOn(message: types.Message):
    
    pag.press('enter')
    print('нажат ентер')

    time.sleep(3)
    keyboard.write('1204', delay=0.5)
    
print(mouse.get_position())
@dp.message_handler(text = 'TikTok')
async def find(message: types.Message):
    os.startfile('C:\\Users\\Den4e\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Roblox\\Roblox Player')
    print('Roblox запущен')
    time.sleep(10)

    pag.moveTo(204, 600)
    
    time.sleep(5)
    
    
    mouse.click('left')
    mouse.wheel(-1)
    mouse.click('left')
    time.sleep(2)
    pag.moveTo(404, 575)
    time.sleep(5)
    mouse.click('left')
    print('прокликал')
    
   
    
@dp.message_handler(text = 'pars')
async def find(message: types.Message):

    url = "https://xn--80aegj1b5e.xn--p1ai/"


    headers ={
        "Accept": "*/*",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
    } 
    req = requests.get(url, headers=headers)
    src = req.text

    with open("pars.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_products_hrefs = soup.find_all('a')
    list = []
    index = 0
    all_cat_dict = {}
    for item in all_products_hrefs:
            # print(f" https://xn--80aegj1b5e.xn--p1ai/{item.get('href')}    {item.text}")
            # await message.answer(f" Ссылка:  https://xn--80aegj1b5e.xn--p1ai/{item.get('href')}  Название: {item.text}")
            item_href =  f"https://xn--80aegj1b5e.xn--p1ai/{item.get('href')}"
            item_text = item.text
            all_cat_dict[item_text] = item_href
            
    with open("all_cat_dict", "w", encoding="utf-8") as file:
        json.dump(all_cat_dict, file, indent=4, ensure_ascii=False  )

    path = "all_cat_dict"
    
    
    await message.answer_document(InputFile(path))


            
        

    
    
    


    




# 204 5

    
    
    

    
@dp.message_handler(text = 'Twitch on')
async def scren(message: types.Message):
    await message.answer(f'Открытие твича { webbrowser.open_new("https://www.twitch.tv")}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)













    