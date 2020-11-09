#Made By @helloji123bot . Keep Credits. Cause It hurts. Join @testpy12 for more.



from telethon import events
import asyncio
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
import random
import re
from userbot import CMD_HELP
from collections import deque



@borg.on(admin_cmd(pattern=r"bheart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.3
    animation_ttl = range(0, 50)
    animation_chars = [
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "💔",
            "❤️",
            "💔",
            "❤",
            "Is their anyone to repair my broken heart?💔"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 20])  
            
            
