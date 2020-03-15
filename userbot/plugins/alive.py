"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "   "

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("I'?M ALIVE...... JINDA HU SIR\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nFork by:` @TECHNICALHACKERZ\n"
                     "`Bot created by:` [SnapDragon](tg://user?id=719877937)\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     "This is [My Code](https://github.com/hackerzkali/user-bot)" You Create user-bot like me) 
