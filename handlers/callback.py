#(π) πΈπΆπΈπ·γ π°π»π΄ππ° πΌπππΈπ² γ
#γ π³π°ππΊπ°πΌπ°π½π» γγ π³π°ππΊπ°πΌπ°π½πΌ γ
#γ ππ΄π°πΌ γ= γ π°πΌπ°π½ πΆππΉπΉπ°π γ

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **ππ΄π»π²πΎπΌπ΄ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Cα΄Ι΄ PΚα΄Κ Mα΄sΙͺα΄ IΙ΄ Yα΄α΄Κ Oα΄ GΚα΄α΄α΄© Vα΄Ιͺα΄α΄ CΚα΄α΄π. Dα΄α΄ α΄Κα΄α΄©α΄α΄ BΚ [π³π°ππΊ π°πΌπ°π½](https://t.me/DARKAMAN)!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "γ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ γ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("γ π·πΎπ ππΎ πππ΄ πΌπ΄ γ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("γ π²πΎπΌπΌπ°π½π³π γ", callback_data="cbcmds"),
                    InlineKeyboardButton("π²ππ΄π°ππ΄π", url=f"https://t.me/{OWNER_NAME}"),
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


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **π·π΄π»π»πΎ** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Β» **press the button below to read the explanation and see the list of available commands !**

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("γ π±π°ππΈπ² γ", callback_data="cbbasic"),
                    InlineKeyboardButton("γ π°π³ππ°π½π²π΄π³ γ", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("γ π°π³πΌπΈπ½ γ", callback_data="cbadmin"),
                    InlineKeyboardButton("γ πππ³πΎ γ", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("γ πΎππ½π΄π γ", callback_data="cbowner")],
                [InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π±π°ππΈπ² π²πΎπΌπΌπ°π½π³π γ**

γ πΆππΎππΏ ππ² π²πΎπΌπΌπ°π½π³π γ

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

γ π²π·π°π½π½π΄π» ππ² π²πΎπΌπΌπ°π½π³π γ

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π°π³ππ°π½π²π΄π π²πΎπΌπΌπ°π½π³π γ**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π°π³πΌπΈπ½ π²πΎπΌπΌπ°π½π³π γ**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ πππ³πΎ π²πΎπΌπΌπ°π½π³π γ**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ πΎππ½π΄π π²πΎπΌπΌπ°π½π³π γ**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π note:all commands owned by this bot can be executed by the owner of the bot without any exceptionπ.

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·πΎπ ππΎ πππ΄ ππ·πΈπ π±πΎπ γ:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("γ π²πΎπΌπΌπ°π½π³ π»πΈππ γ", callback_data="cbhelp")],
                [InlineKeyboardButton("γ π²π»πΎππ΄ γ", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**γ π·π΄ππ΄ πΈπ ππ·π΄ π²πΎπ½πππΎπ» πΌπ΄π½π πΎπ΅ π±πΎπ γ:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("βΈ πΏπ°πππ΄", callback_data="cbpause"),
                    InlineKeyboardButton("βΆοΈ ππ΄πππΌπ΄", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("β© ππΊπΈπΏ", callback_data="cbskip"),
                    InlineKeyboardButton("βΉ πππΎπΏ", callback_data="cbend"),
                ],
                [InlineKeyboardButton("β π°π½ππΈ π²πΌπ³", callback_data="cbdelcmds")],
                [InlineKeyboardButton("π π²π»πΎππ΄", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ ππ·πΈπ πΈπ ππ·π΄ π΅π΄π°ππππ΄ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ γ:**
        
**π‘ Feature:** delete every commands sent by users to avoid spam in groups !

β usage:**

 1οΈβ£ to turn on feature:
     Β» type `/delcmd on`
    
 2οΈβ£ to turn off feature:
     Β» type `/delcmd off`
      
β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **π·π΄π»π»πΎ** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Β» **press the button below to read the explanation and see the list of available commands !**

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("γ π±π°ππΈπ² γ", callback_data="cblocal"),
                    InlineKeyboardButton("γ π°π³ππ°π½π²π΄π³ γ", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("γ π°π³πΌπΈπ½ γ", callback_data="cblamp"),
                    InlineKeyboardButton("πππ³πΎ", callback_data="cblab"),
                ],
                [InlineKeyboardButton("πΎππ½π΄π π²πΌπ³", callback_data="cbmoon")],
                [InlineKeyboardButton("π±π°π²πΊ", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·πΎπ ππΎ πππ΄ ππ·πΈπ π±πΎπ γ:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π±π°ππΈπ² π²πΎπΌπΌπ°π½π³π γ**

γ πΆππΎππΏ ππ² π²πΌπ³ γ

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

γ π²π·π°π½π½π΄π» ππ² π²πΌπ³ γ

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π°π³ππ°π½π²π΄π³ π²πΎπΌπΌπ°π½π³π γ**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ π°π³πΌπΈπ½ π²πΎπΌπΌπ°π½π³π γ**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ πππ³πΎ π²πΎπΌπΌπ°π½π³π γ**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**γ π·π΄ππ΄ πΈπ ππ·π΄ πΎππ½π΄π π²πΎπΌπΌπ°π½π³π γ**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

β‘ __πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π°.πΈ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("γ π±π°π²πΊ γ", callback_data="cbcmds")]]
        ),
    )
