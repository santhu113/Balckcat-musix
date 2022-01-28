import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg",
        caption=f"""**ʜᴇʟʟᴏ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ ᴠᴘs sᴀɴᴛʜᴜ sᴇʀᴠᴇʀ. 
┏━━━━━━━━━━━━━━━━━┓
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.
┗━━━━━━━━━━━━━━━━━┛
[sᴀɴᴛʜᴜ 🥰](https://t.me/santhu_music_bot)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [sᴀɴᴛʜᴜ 😁](https://t.me/santhu_music_bot)**""",
  

  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞 sᴀɴᴛʜᴜ ɴɪ ᴀᴅᴅ ᴄʜᴇsᴜ ᴋᴏɴᴅɪ 🥺", url=f"https://t.me/Santhuadvancemusicbot?startgroup=true")
                ]
                
           ]
        ),
    )
    

@Client.on_message(filter(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴏᴡɴᴇʀ 💞", url=f"https://t.me/santhu_music_bot")
                ]
            ]
        ),
    )
