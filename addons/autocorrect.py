# Amang Userbot
# Copyright (C) 2021-2022 amangtele
#
# This file is a part of < https://github.com/amangtele/AmangUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/amangtele/AmangUserbot/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_autocorrect")

import string

from . import HNDLR, LOGS, get_string, udB, amang_bot, amang_cmd  # ignore: pylint

try:
    from gingerit.gingerit import GingerIt
except ImportError:
    LOGS.info("GingerIt not found")
    GingerIt = None

from google_trans_new import google_translator
from telethon import events


@amang_cmd(pattern="autocorrect", fullsudo=True)
async def acc(e):
    if not udB.get_key("AUTOCORRECT"):
        udB.set_key("AUTOCORRECT", "True")
        amang_bot.add_handler(
            gramme, events.NewMessage(outgoing=True, func=lambda x: x.text)
        )
        return await e.eor(get_string("act_1"), time=5)
    udB.del_key("AUTOCORRECT")
    await e.eor(get_string("act_2"), time=5)


async def gramme(event):
    if not udB.get_key("AUTOCORRECT"):
        return
    t = event.text
    if t[0] == HNDLR or t[0].lower() not in string.ascii_lowercase or t.endswith(".."):
        return
    tt = google_translator().detect(t)
    if tt[0] != "en":
        return
    xx = GingerIt()
    x = xx.parse(t)
    res = x["result"]
    try:
        await event.edit(res)
    except BaseException:
        pass


if GingerIt and udB.get_key("AUTOCORRECT"):
    amang_bot.add_handler(
        gramme, events.NewMessage(outgoing=True, func=lambda x: x.text)
    )
