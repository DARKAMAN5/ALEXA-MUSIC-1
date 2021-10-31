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
        f"""✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.mention()} !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜᴛ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛs!**

💡 **ғɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ,s ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♨️ǟɖɖ ʍɛ ȶօ ʏօʊʀ ɢʀօʊք♨️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("✨ɮǟֆɨƈ ɢʊɨɖɛ✨", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🥳ƈօʍʍǟռɖֆ🥳", callback_data="cbcmds"),
                    InlineKeyboardButton("☣️ƈʀɛǟȶɛʀ☣️", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🥰ֆʊքքօʀȶ ɢʀօʊք🥰", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🇮🇳ʊքɖǟȶɛֆ ƈɦǟռռɛʟ🇮🇳", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🖱️ǟʟɛӼǟ ʀօɮօȶ🖱️", url="https://t.me/ALEXA_MANAGER_ROBOT"
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
                InlineKeyboardButton("🥰ɢʀօʊք🥰", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "🇮🇳ƈɦǟռռɛʟ🇮🇳", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ʜᴇʟʟᴏ {message.from_user.mention()}, ɪ'ᴍ {BOT_NAME}**\n\n✨ ʙᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ ɴᴏʀᴍᴀʟʟʏ\n🍀 ᴍʏ ᴍᴀsᴛᴇʀ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n🍀 ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n✨ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n🍀 ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs: `{uptime}`\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ, ғᴏʀ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ** ❤"

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
        f"""✨ **ʜᴇʟʟᴏ** {message.from_user.mention()} !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="♨️ɮǟֆɨƈ ɢʊɨɖɛ♨️", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `քɨռɢ!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


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
