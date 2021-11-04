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
    lel = await message.reply_text("**『 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝚃𝙾 𝙳𝙰𝚁𝙺 𝚂𝙴𝚁𝚅𝙴𝚁𝚂 』**")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="『 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 』", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="『 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 』", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    audio = message.reply_to_message.audio if message.reply_to_message else None
    if not audio:
        return await lel.edit("**『𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝙳𝙸𝙾 𝙵𝙸𝙻𝙴』**")
    if round(audio.duration / 60) > DURATION_LIMIT:
        return await lel.edit(
            f"**『𝙼𝚄𝚂𝙸𝙲 𝚆𝙸𝚃𝙷 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 𝙼𝙾𝚁𝙴 𝚃𝙷𝙰𝙽** `{DURATION_LIMIT}` **𝙼𝙸𝙽𝚄𝚃𝙴𝚂, 𝙲𝙰𝙽'𝚃 𝙿𝙻𝙰𝚈』 !**"
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
            caption=f"**『 𝚃𝚁𝙰𝙲𝙺 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝚀𝚄𝙴𝚄𝙴 』»** `{position}`\n\n **『 𝙽𝙰𝙼𝙴 』:** {title[:50]}\n **『 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽』:** `{duration}`\n **『 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈 』:** {costumer}",
            reply_markup=keyboard,
        )
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
            photo=f"{AUD_IMG}",
            caption=f" **『 𝙽𝙰𝙼𝙴 』:** {title[:50]}\n **『 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 』:** `{duration}`\n **『 𝚂𝚃𝙰𝚃𝚄𝚂 』:** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n"
            + f"**『 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 』:** {costumer}",
            reply_markup=keyboard,
        )

    return await lel.delete()
