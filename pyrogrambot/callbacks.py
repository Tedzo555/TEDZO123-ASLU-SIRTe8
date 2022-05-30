from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client
from pyrogrambot.buttons import MENU_BUTTON, MOVIE_BUTTON, COMMM_BUTTON, KGF_BUTTON, S_BACK_BUTTO, SMENU_BUTTO, PMENU_BUTTN, button, VDENU_BUTTO
import asyncio
import pytz, datetime
from pyrogrambot.photos import PHOTOS
import random



@Client.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "next":
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )
    elif msg.data == "sticker":
        await msg.answer("Mode Chenged To Sticker")
        await msg.message.delete()
        await msg.message.reply_sticker(
            sticker="CAACAgIAAxkBAAECR5FiWgOUsaX2iRWuUtv8Y7AvIPoNuQAC-hAAAqHHKEg5ZXbrk1gHox4E",
            reply_markup=InlineKeyboardMarkup(SMENU_BUTTO)
        )

    elif msg.data == "video":
        await msg.answer("Mode Chenged To Video")
        await msg.message.delete()
        await msg.message.reply_video(
            video="https://telegra.ph/file/6734341d85690fd50f6b9.mp4",
            caption="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup(VDENU_BUTTO)
        )

    elif msg.data == "photo":
        await msg.answer("Mode Chenged To Photo")
        await msg.message.delete()
        await msg.message.reply_photo(
            photo=random.choice(PHOTOS),
            caption="Hᴇʀᴇ Is Yᴏᴜ'ʀᴇ Mᴇɴᴜ",
            reply_markup=InlineKeyboardMarkup(MENU_BUTTON)
        )

    elif msg.data == "id":
        await msg.answer(f"Fɪʀsᴛ Nᴀᴍᴇ : {msg.from_user.first_name}\nLᴀsᴛ Nᴀᴍᴇ : {msg.from_user.last_name}\nUsᴇʀɴᴀᴍᴇ : {msg.from_user.username}\nUsᴇʀ ɪᴅ : {msg.from_user.id}", show_alert=True)

    elif msg.data == "movies":
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text="Tᴏ Dᴏᴡɴʟᴏᴀᴅ Kɢғ 𝟸 Sᴇɴᴅ Tʜɪs Tᴇxᴛ `kgf 2`",
            reply_markup=InlineKeyboardMarkup(MOVIE_BUTTON)
        )
    elif msg.data == "close":
        await msg.answer("Closed")
        await msg.message.delete()

    elif msg.data == "commands":
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text="""╭────────────────⍟
│
│ /start - Tᴏ Sᴛᴀʀᴛ Tʜɪs Bᴏᴛ
│
│ /id - Tᴏ Gᴇᴛ Iᴅ ( ᵒⁿˡʸ ʷᵒʳᵏˢ ⁱⁿ ᵍʳᵒᵘᵖ )
│
╰────────────────⍟""",
            reply_markup=InlineKeyboardMarkup(COMMM_BUTTON)
        )
    elif msg.data == "downlod":
        await msg.message.edit(
            text="""<b>• Nᴀᴍᴇ : KGF
• Yᴇᴀʀ : 2022
• Sɪᴢᴇ : - 1400MB</b>""",
            reply_markup=InlineKeyboardMarkup(KGF_BUTTON)
        )

    elif msg.data == "smovies":
        await msg.answer("Tᴏ Dᴏᴡɴʟᴏᴀᴅ Kɢғ 𝟸 Sᴇɴᴅ Tʜɪs Tᴇxᴛ kgf 2", show_alert=True)

    elif msg.data == "scommands":
        await msg.answer("/start - Tᴏ Sᴛᴀʀᴛ Tʜɪs Bᴏᴛ\n/id - Tᴏ Gᴇᴛ Iᴅ ( ᵒⁿˡʸ ʷᵒʳᵏˢ ⁱⁿ ᵍʳᵒᵘᵖ )", show_alert=True)

    elif msg.data == "sback":
        await msg.message.delete()
        await msg.message.reply_sticker(
            sticker="CAACAgIAAxkBAAECR5liWidHhuUuJNcoJ_5QjliWb4I4kgAC1BEAA8CgSXknAeKPK_QMHgQ",
            reply_markup=InlineKeyboardMarkup(S_BACK_BUTTO)
        )
    elif msg.data == "pback":
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
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text=f"""<b>{get} 👋, {msg.from_user.mention}

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ [Tʜɪs Gᴜʏ](https://t.me/tedzo01)

Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Sᴇᴇ Mᴏʀᴇ</b>""",
        reply_markup=InlineKeyboardMarkup(button)
    )

    elif msg.data == "vback":
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
        await msg.message.edit("○○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●○○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●○○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●○○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●○")
        await asyncio.sleep(0.2)
        await msg.message.edit("●●●●●")
        await asyncio.sleep(0.2)
        await msg.message.edit(
            text=f"""<b>{get} 👋, {msg.from_user.mention}

Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ [Tʜɪs Gᴜʏ](https://t.me/tedzo01)

Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Sᴇᴇ Mᴏʀᴇ</b>""",
        reply_markup=InlineKeyboardMarkup(button)
    )



        

