from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

I Aᴍ {me2},
Tʀᴜsᴛᴇᴅ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.
Fᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.
Nᴏ ᴇʀʀᴏʀ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Gᴇɴᴇʀᴀᴛᴇ Sᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" Sᴜᴘᴘᴏʀᴛ", url="https://t.me/Luxurious_Group"),
                    InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Luxurious_Network")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
