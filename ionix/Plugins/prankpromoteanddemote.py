#Made by @helloji123bot. Keep credits cause it hurts...#editedforall. Original credits to @Kraken_The_BadASS


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ppromote ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`😈Userbot😈`:**PROMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**PROMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**PROMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**PROMOTED USER SUCCESSFULLY**")
        
        
@borg.on(admin_cmd(pattern="npromote ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`😈Userbot😈`:**PROMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**PROMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**PROMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**Not Enough Rights To Promote user to Admin**")
        
        
        
@borg.on(admin_cmd(pattern="ndemote ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`😈Userbot😈`:**DEMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**DEMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**DEMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**Not Enough Rights To Demote user **")
        
        
@borg.on(admin_cmd(pattern="pdemote ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("`😈Userbot😈`:**DEMOTING USER..**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**DEMOTING USER...**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**DEMOTING USER....**")
        await asyncio.sleep(1)
        await event.edit("`😈Userbot😈`:**DEMOTED USER SUCCESSFULLY**")
