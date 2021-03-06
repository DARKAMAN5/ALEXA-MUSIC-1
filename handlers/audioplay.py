# this module i created only for playing music using audio file, idk, because the audio player on play.py module not working
# so this is the alternative
# audio play function
# tede ganteng tq

from os import path

import converter
from callsmusic import callsmusic, queues
from config import (
    AUD_IMG,
    BOT_USERNAME,
    DURATION_LIMIT,
    GROUP_SUPPORT,
    QUE_IMG,
    UPDATES_CHANNEL,
)
from handlers.play import convert_seconds
from helpers.filters import command, other_filters
from helpers.gets import get_file_name
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(_, message: Message):
    costumer = message.from_user.mention
    lel = await message.reply_text("**γ π²πΎπ½π½π΄π²ππΈπ½πΆ ππΎ π³π°ππΊ ππ΄πππ΄ππ γ**")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="γ πππΏπΏπΎππ γ", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="γ π²π·π°π½π½π΄π» γ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    audio = message.reply_to_message.audio if message.reply_to_message else None
    if not audio:
        return await lel.edit("**γπΏπ»π΄π°ππ΄ ππ΄πΏπ»π ππΎ π° ππ΄π»π΄πΆππ°πΌ π°ππ³πΈπΎ π΅πΈπ»π΄γ**")
    if round(audio.duration / 60) > DURATION_LIMIT:
        return await lel.edit(
            f"**γπΌπππΈπ² ππΈππ· π³πππ°ππΈπΎπ½ πΌπΎππ΄ ππ·π°π½** `{DURATION_LIMIT}` **πΌπΈπ½πππ΄π, π²π°π½'π πΏπ»π°πγ !**"
        )

    # tede_ganteng = True
    title = audio.title
    file_name = get_file_name(audio)
    duration = convert_seconds(audio.duration)
    file_path = await converter.convert(
        (await message.reply_to_message.download(file_name))
        if not path.isfile(path.join("downloads", file_name))
        else file_name
    )
    # ambil aja bg
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
            photo=f"{QUE_IMG}",
            caption=f"**γ πππ°π²πΊ π°π³π³π΄π³ ππΎ πππ΄ππ΄ γΒ»** `{position}`\n\n **γ π½π°πΌπ΄ γ:** {title[:50]}\n **γ π³πππ°ππΈπΎπ½γ:** `{duration}`\n **γ ππ΄πππ΄ππ π±π γ:** {costumer}",
            reply_markup=keyboard,
        )
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
            photo=f"{AUD_IMG}",
            caption=f" **γ π½π°πΌπ΄ γ:** {title[:50]}\n **γ π³πππ°ππΈπΎπ½ γ:** `{duration}`\n **γ πππ°πππ γ:** `πΏπ»π°ππΈπ½πΆ`\n"
            + f"**γ ππ΄πππ΄πππ΄π³ π±π γ:** {costumer}",
            reply_markup=keyboard,
        )

    return await lel.delete()
