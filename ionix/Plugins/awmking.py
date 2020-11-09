#Credit to @helloji123bot
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import CMD_HELP
from userbot.utils import admin_cmd
B = ("▄︻╦芫≡══-------------➖")
@borg.on(admin_cmd(pattern=r"awm"))
async def bluedevilawm(awm):
    await awm.edit(B)