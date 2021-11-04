from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **𝚆𝙴𝙻𝙲𝙾𝙼𝙴 {message.from_user.mention} !**\n
✨ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Oᴘ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ💖. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [𝙳𝙰𝚁𝙺 𝙰𝙼𝙰𝙽](https://t.me/DARKAMAN)!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿』",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("『 𝙱𝙰𝚂𝙸𝙲 』", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("『 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 』", callback_data="cbcmds"),
                    InlineKeyboardButton("『 𝙾𝚆𝙽𝙴𝚁 』", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "『 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 』", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "『 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 』", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "『 𝙰𝙻𝙴𝚇𝙰 𝚁𝙾𝙱𝙾𝚃 』", url="https://t.me/ALEXA_MANAGER_ROBOT"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("『 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 』", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "『 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 』", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**𝙷𝙴𝙻𝙻𝙾 {message.from_user.mention}, 𝙸'𝙼 {BOT_NAME}**

     **『 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 』 ➮ [{ALIVE_NAME}](https://t.me/{OWNER_NAME})**
    
     **『 𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 』➮ `v{__version__}`**

     **『 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 』➮ `{pyrover}`**
  
     **『 𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 』➮ `{__python_version__}`**

     **『 𝚄𝙿𝚃𝙸𝙼𝙴  』➮ `{uptime}`**
  
     **𝚃𝙷𝙰𝙽𝙺𝚂 𝙵𝙾𝚁 𝙰𝙳𝙸𝙽𝙶 𝙼𝙴 𝙷𝙴𝚁𝙴, 𝙵𝙾𝚁 𝙿𝙻𝙰𝚈𝙸𝙽𝙶 𝙼𝚄𝚂𝙸𝙲 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙹𝙾𝙸𝙽 [𝙳𝙰𝚁𝙺 𝚂𝚄𝙿𝙿𝙾𝚁𝚃]("https://t.me//DARKAMANSUPPORT")💖**"
 
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **𝙷𝙴𝙻𝙻𝙾** {message.from_user.mention()} !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="『 𝙱𝙰𝚂𝙸𝙲 𝙶𝚄𝙸𝙳𝙴 』", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("`〘 ♕ ᑭσɳց! ♕ 〙`\n" f"`〘 {delta_ping * 1000:.3f} ms 〙`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
