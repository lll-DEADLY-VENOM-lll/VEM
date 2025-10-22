import asyncio as _asyncio

import uvloop as _uvloop

_asyncio.set_event_loop_policy(_uvloop.EventLoopPolicy())  # noqa

from DnsXMusic.core.bot import DnsBot
from DnsXMusic.core.dir import dirr
from DnsXMusic.core.git import git
from DnsXMusic.core.userbot import Userbot
from DnsXMusic.misc import dbb, heroku

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

app = DnsBot()
userbot = Userbot()

HELPABLE = {}
