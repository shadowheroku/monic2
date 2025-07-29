from pyrogram import filters
from pyrogram.types import Message

from ERISMUSIC import app
from ERISMUSIC.core.call import PRINCE
from ERISMUSIC.utils.database import is_music_playing, music_off
from ERISMUSIC.utils.decorators import AdminRightsCheck
from ERISMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await PRINCE.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
