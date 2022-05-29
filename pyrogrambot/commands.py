from pyrogram import Client, filters
from pyrogrambot.photos import PHOTOS
from pyrogrambot.buttons import button
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random
import asyncio
import pytz, datetime
FORCE_SUB = "tzobotz"


@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):             
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",              
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardMarkup(button)
            ]]
            )
        )
@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    text = f"""Tɪᴛʟᴇ : {msg.chat.title}
Usᴇʀɴᴀᴍᴇ : @{msg.chat.username}
Cʜᴀᴛ ɪᴅ : `{msg.chat.id}`
Usᴇʀ ɪᴅ : `{msg.from_user.id}`"""
    await msg.reply_text(text=text)
