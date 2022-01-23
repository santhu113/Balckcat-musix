import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg",
        caption=f"""**ʜᴇʟʟᴏ ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ ᴠᴘs  𝐒𝐀𝐍𝐓𝐇𝐔 𝐒𝐄𝐑𝐕𝐄𝐑 💞. 
┏━━━━━━━━━━━━━━━━━┓
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.
┣» [𝐃𝐄𝐏𝐋𝐎𝐘 𝐁𝐘 ❤️](https://t.me/santhu_music_bot)
┗━━━━━━━━━━━━━━━━━┛
[𝚂𝙰𝙽𝚃𝙷𝚄 𝙽𝙴𝚃𝚆𝙾𝚁𝙺 ❤️](https://t.me/santhuvc)



𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝙾𝚆𝙽𝙴𝚁 ❤️](https://t.me/santhu_music_bot)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😘 𝐍𝐀𝐍𝐔 𝐀𝐃𝐃 𝐂𝐇𝐄𝐒𝐔𝐊𝐎 ✨", url="http://t.me/Ramcharangroupmanagementbot?startgroup=true")
                    InlineKeyboardButton(
                        "💥 𝐎𝐖𝐍𝐄𝐑 💞", url=f"https://t.me/santhu_music_bot")
                    InlineKeyboardButton(
                        "😘 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 💞", url=f"https://t.me/santhuvc")
                    InlineKeyboardButton(
                        "😁 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 😘", url=f"https://t.me/santhubotupadates"
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐎𝐖𝐍𝐄𝐑 💞", url=f"https://t.me/santhu_music_bot")
                ]
            ]
        ),
    )
