from pyrogram import Client, filters
from pyrogrambot.photos import PHOTOS
from pyrogrambot.buttons import button,TEDZO_BUTTON
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random
import asyncio
import pytz, datetime
FORCE_SUB = "@tzobotz"


@Client.on_message(filters.command("start")) 
async def start_message(bot, message):
    await asyncio.sleep(0.6)
    if FORCE_SUB:
        try:
            user = await bot.get_chat_member(FORCE_SUB,message.chat.id)
            if user.status == "kicked out":
                await message.reply_text("<b>Aᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ 🚸</b>")
                return
        except UserNotParticipant:
             await message.reply_text(
                 text="Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ",
                 reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton(text="Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/tzobotz") ]])
             )
             return
    m = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    time = m.hour
    if time < 12:
        get="Gᴏᴏᴅ Mᴏʀɴɪɴɢ"
    elif time < 15:
        get="Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ"
    elif time < 20:
        get="Gᴏᴏᴅ Eᴠᴇɴɪɴɢ"
    else:
        get="Gᴏᴏᴅ Nɪɢʜᴛ"
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""<b>{get} 👋, {message.from_user.mention}

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ CƦᴇᴀᴛᴇᴅ Bʏ [OWNER](https://t.me/tedzo01)

cʟɪᴄᴋ bᴇʟᴏᴡ bᴜᴛᴛᴏɴ tᴏ sᴇᴇ mᴏʀᴇ</b>""",
        reply_markup=InlineKeyboardMarkup(button)
    )

@Client.on_message(filters.regex("about") & filters.private)
async def about_message(bot, message):
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        reply_markup=InlineKeyboardMarkup(TEDZO_BUTTON)
    )

@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    text = f"""Tɪᴛʟᴇ : {msg.chat.title}
Usᴇʀɴᴀᴍᴇ : @{msg.chat.username}
Cʜᴀᴛ ɪᴅ : `{msg.chat.id}`
Usᴇʀ ɪᴅ : `{msg.from_user.id}`"""
    await msg.reply_text(text=text)
