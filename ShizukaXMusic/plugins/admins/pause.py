from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ShizukaXMusic import app
from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import is_music_playing, music_off
from ShizukaXMusic.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"], disable_web_page_preview=True)
    await music_off(chat_id)
    await Shizuka.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), disable_web_page_preview=True
    )
