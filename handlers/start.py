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
    await message.reply_photo("https://te.legra.ph/file/7503b8232fc07a8324289.jpg")
    await message.reply_text(
        f"""β¨ **ππ΄π»π²πΎπΌπ΄ {message.from_user.mention} !**\n
β¨ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Cα΄Ι΄ PΚα΄Κ Mα΄sΙͺα΄ IΙ΄ Yα΄α΄Κ Oα΄ GΚα΄α΄α΄© Vα΄Ιͺα΄α΄ CΚα΄α΄π. Dα΄α΄ α΄Κα΄α΄©α΄α΄ BΚ [π³π°ππΊ π°πΌπ°π½](https://t.me/DARKAMAN)!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "γ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏγ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("γ π±π°ππΈπ² γ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("γ π²πΎπΌπΌπ°π½π³π γ", callback_data="cbcmds"),
                    InlineKeyboardButton("γ πΎππ½π΄π γ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "γ πππΏπΏπΎππ γ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "γ π²π·π°π½π½π΄π» γ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "γ π°π»π΄ππ° ππΎπ±πΎπ γ", url="https://t.me/ALEXA_MANAGER_ROBOT"
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
                InlineKeyboardButton("γ πππΏπΏπΎππ γ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "γ π²π·π°π½π½π΄π» γ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**π·π΄π»π»πΎ {message.from_user.mention}, πΈ'πΌ {BOT_NAME}**

     **γ πΌπ πΌπ°πππ΄π γ β? [{ALIVE_NAME}](https://t.me/{OWNER_NAME})**
    
     **γ π±πΎπ ππ΄πππΈπΎπ½ γβ? `v{__version__}`**

     **γ πΏπππΎπΆππ°πΌ ππ΄πππΈπΎπ½ γβ? `{pyrover}`**
  
     **γ πΏπππ·πΎπ½ ππ΄πππΈπΎπ½ γβ? `{__python_version__}`**

     **γ ππΏππΈπΌπ΄  γβ? `{uptime}`**
  
     **ππ·π°π½πΊπ π΅πΎπ π°π³πΈπ½πΆ πΌπ΄ π·π΄ππ΄, π΅πΎπ πΏπ»π°ππΈπ½πΆ πΌπππΈπ² πΎπ½ ππΎππ πΆππΎππΏ πΉπΎπΈπ½ [π³π°ππΊ πππΏπΏπΎππ]("https://t.me//DARKAMANSUPPORT")π**" 
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
        f"""β¨ **π·π΄π»π»πΎ** {message.from_user.mention()} !

Β» **press the button below to read the explanation and see the list of available commands !**

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="γ π±π°ππΈπ² πΆππΈπ³π΄ γ", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("`γ β α­ΟΙ³Φ! β γ`\n" f"`γ {delta_ping * 1000:.3f} ms γ`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ bot status:\n"
        f"β’ **uptime:** `{uptime}`\n"
        f"β’ **start time:** `{START_TIME_ISO}`"
    )
