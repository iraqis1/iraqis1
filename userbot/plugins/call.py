"""Check if userbot call. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.call$")
async def amireallyalive(alive):
	
    """ For .alive command, check if the bot is running.  """
    await alive.edit("اهلا بك في سورس التليثيون العراقي\n"
"➖➖➖➖➖➖➖➖➖\n"
"استخدم امر .alive اذا اعتقدت ان البوت توقف!\n"
"➖➖➖➖➖➖➖➖➖\n"
"اشترك في قناة السورس لانها تطرح ملفات وشروحات مفيده\n"
"➖➖➖➖➖➖➖➖➖\n"
"يمكنك مراسلتنا لاي خلل حاصل\n"
"➖➖➖➖➖➖➖➖➖\n"
"لتنصيب السورس راسلني احد مطورين السورس\n"
"➖➖➖➖➖➖➖➖➖\n"
"مطورين السورس : \n"
"➖➖➖➖➖➖➖➖➖\n"
"احمد || @HHMHHH \n"
"➖➖➖➖➖➖➖➖➖\n"
"حسن || @VHHHHH \n"
"➖➖➖➖➖➖➖➖➖\n"
"حارث || @cCcYo \n"
"➖➖➖➖➖➖➖➖➖\n"
"قناة السورس الرسميه : @cqccqq\n")