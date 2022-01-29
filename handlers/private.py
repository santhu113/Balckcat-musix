import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAIC_mH1JUrL_s4kgKA5hiDk_Rrl0GYWAAIeCgACz9YRUXNuChP5kGjfIwQ")
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/cdb11db8885e10e042964.jpg",
        caption=f"""**━━━━━━━━━━━━ 🌺🌻🌹🌷━━━━━━━━━━
━━━━━━━━━━━━━ 🌺🌻🌹🌷━━━━━━━━━━━━━
😊ʜɪ ɪᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ... ᴅᴇᴘʟᴏʏ ʙʏ : @nenu_na_crush

┏━━━━━━━━━━━━━━━━━┓ 🌺🌻🌹🌷🌺🌻🌹
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ. 
┣» [𝐃𝐄𝐏𝐋𝐎𝐘 𝐁𝐘 ❤️](https://t.me/nenu_na_crush)
┗━━━━━━━━━━━━━━━━━┛
[𝐎𝐖𝐍𝐄𝐑 ❤️](https://t.me/nenu_na_crush)
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐒𝐀𝐍𝐓𝐇𝐔❤️](https://t.me/nenu_na_crush)
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞ᴀʀʏᴀ ɴɪ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ💞", url="https://t.me/iconstararyamusicadvancebot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "☹️ᴏᴡɴᴇʀ😘", url="https://t.me/@nenu_na_crush"
                    ),
                    InlineKeyboardButton(
                        "😇ɢʀᴏᴜᴘ💞", url="https://t.me/friends_life_forever"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😁ɴᴇᴛᴡᴏʀᴋ😊", url="https://t.me/friends_life_forever"
                    )]
            ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/cdb11db8885e10e042964.jpg",
        caption=f"""ᴘʀɪᴠᴀᴛᴇ ʀᴇᴘᴏ !🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕ᴏᴡɴᴇʀ💕", url=f"https://t.me/nenu_na_crush")
                ]
            ]
        ),
    )
