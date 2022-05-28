# @ismayilzadevuqar - < https://t.me/ismayilzadevuqar >
# Copyright (C) 2022
#
# Bu fayl, < https://github.com >'un parçasıdır.
# Zəhmət olmasa, GNU Affero Ümumi İctimai Lisenziyasını oxuyun;
# < https://www.github.com/XTQ067 >
#
#  Repodan nəsə əkib başqasına verən kimliyindən aslı olmayaraq peysərdi. # 


from bot import bot, qruplar
from telethon import * 
from telethon.events import *
import sys, os
from os import execl


@bot.on(CallbackQuery(data="cancel"))   # cr: @ismayilzadevuqar
async def cancel(event):
    global qruplar
    qruplar.append(event.chat_id)
    await bot.send_message(event.chat_id, "Oyun uğurla dayandırıldı!\nProblem Yarandıqda @NeonSUP'a gələrək əlaqə saxlayın! ✅",
    try:
        await bot.disconnect()
    except BaseException:
        pass

    execl(sys.executable, sys.executable, *sys.argv)
	
@bot.on(NewMessage(pattern="^/cancel|^/cancel@LuksCrocadilBot"))   # cr: @imperatorbey
async def handler(event):
    global qruplar
    qruplar.append(event.chat_id)
    await bot.send_message(event.chat_id, "Oyun uğurla dayandırıldı!\nProblem Yarandıqda @NeonSUP'a gələrək əlaqə saxlayın! ✅",
    try:
        await bot.disconnect()
    except:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)
