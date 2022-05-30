from pyrogram import Client, filters
from pyrogrambot.photos import PHOTOS
from pyrogrambot.buttons import button
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random
import asyncio
import pytz, datetime
FORCE_SUB = "AIOM_PYRO"


@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
	await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n _TEDZO SIR PYROGRAM BOT\nBy\naslu__",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([ [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/tedzobotz") ],               [InlineKeyboardButton("join 🧐", url="https://t.me/tedzomovies") ]   ]  ) )
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

@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    text = f"""Tɪᴛʟᴇ : {msg.chat.title}
Usᴇʀɴᴀᴍᴇ : @{msg.chat.username}
Cʜᴀᴛ ɪᴅ : `{msg.chat.id}`
Usᴇʀ ɪᴅ : `{msg.from_user.id}`"""
    await msg.reply_text(text=text)
