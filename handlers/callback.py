#(𝚌) 𝟸𝟶𝟸𝟷『 𝙰𝙻𝙴𝚇𝙰 𝙼𝚄𝚂𝙸𝙲 』
#『 𝙳𝙰𝚁𝙺𝙰𝙼𝙰𝙽𝟻 』『 𝙳𝙰𝚁𝙺𝙰𝙼𝙰𝙽𝟼 』
#『 𝚃𝙴𝙰𝙼 』= 『 𝙰𝙼𝙰𝙽 𝙶𝚄𝙹𝙹𝙰𝚁 』

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
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music on groups through the new Telegram's voice chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**

❔ **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 』",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("『 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 』", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("『 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 』", callback_data="cbcmds"),
                    InlineKeyboardButton("𝙲𝚁𝙴𝙰𝚃𝙴𝚁", url=f"https://t.me/{OWNER_NAME}"),
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


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **𝙷𝙴𝙻𝙻𝙾** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("『 𝙱𝙰𝚂𝙸𝙲 』", callback_data="cbbasic"),
                    InlineKeyboardButton("『 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 』", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("『 𝙰𝙳𝙼𝙸𝙽 』", callback_data="cbadmin"),
                    InlineKeyboardButton("『 𝚂𝚄𝙳𝙾 』", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("『 𝙾𝚆𝙽𝙴𝚁 』", callback_data="cbowner")],
                [InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

『 𝙶𝚁𝙾𝚄𝙿 𝚅𝙲 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 』

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

『 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚅𝙲 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 』

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

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

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast (reply to message) - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("『 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙻𝙸𝚂𝚃 』", callback_data="cbhelp")],
                [InlineKeyboardButton("『 𝙲𝙻𝙾𝚂𝙴 』", callback_data="close")],
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
        "**『 𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙲𝙾𝙽𝚃𝚁𝙾𝙻 𝙼𝙴𝙽𝚄 𝙾𝙵 𝙱𝙾𝚃 :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ 𝙿𝙰𝚄𝚂𝙴", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ 𝚁𝙴𝚂𝚄𝙼𝙴", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ 𝚂𝙺𝙸𝙿", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ 𝚂𝚃𝙾𝙿", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ 𝙰𝙽𝚃𝙸 𝙲𝙼𝙳", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 𝙲𝙻𝙾𝚂𝙴", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**『 𝚃𝙷𝙸𝚂 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 』:**
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **𝙷𝙴𝙻𝙻𝙾** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("『 𝙱𝙰𝚂𝙸𝙲 』", callback_data="cblocal"),
                    InlineKeyboardButton("『 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 』", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("『 𝙰𝙳𝙼𝙸𝙽 』", callback_data="cblamp"),
                    InlineKeyboardButton("𝚂𝚄𝙳𝙾", callback_data="cblab"),
                ],
                [InlineKeyboardButton("𝙾𝚆𝙽𝙴𝚁 𝙲𝙼𝙳", callback_data="cbmoon")],
                [InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **turn on the voice chat first before start to play music.**

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

『 𝙶𝚁𝙾𝚄𝙿 𝚅𝙲 𝙲𝙼𝙳 』

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

『 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚅𝙲 𝙲𝙼𝙳 』

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 𝙰.𝙸__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

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

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("『 𝙱𝙰𝙲𝙺 』", callback_data="cbcmds")]]
        ),
    )
