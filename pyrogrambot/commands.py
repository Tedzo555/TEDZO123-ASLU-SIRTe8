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
    insert(int(message.chat.id))
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(DELAY)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/BETA_UPDATES")
            ],[            
            InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
            InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
            ],[
            InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 👨‍💻 ", callback_data="devs"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
            ]]
            )
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

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ [Tʜɪs Gᴜʏ](https://t.me/tedzo01)

Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Sᴇᴇ Mᴏʀᴇ</b>""",
        reply_markup=InlineKeyboardMarkup(button)
    )

@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    text = f"""Tɪᴛʟᴇ : {msg.chat.title}
Usᴇʀɴᴀᴍᴇ : @{msg.chat.username}
Cʜᴀᴛ ɪᴅ : `{msg.chat.id}`
Usᴇʀ ɪᴅ : `{msg.from_user.id}`"""
    await msg.reply_text(text=text)
