# Amang Userbot
# Copyright (C) 2021-2022 amangtele
#
# This file is a part of < https://github.com/amangtele/AmangUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/amangtele/AmangUserbot/blob/main/LICENSE/>.

"""
◈ Perintah Tersedia

• `{i} rc/carbon` <balas teks>
     `rcarbon` Background Acak.

• `{i} ccarbon` <warna><balas teks>
     Carbon Dengan Kostum Warna.
"""


import random

from telethon.utils import get_display_name

from . import Carbon, eor, get_string, inline_mention, os, amang_cmd

_colorspath = "resources/colorlist.txt"

if os.path.exists(_colorspath):
    with open(_colorspath, "r") as f:
        all_col = f.read().split()
else:
    all_col = []


@amang_cmd(
    pattern="(rc|c)arbon",
)
async def crbn(event):
    xxxx = await event.eor(get_string("com_1"))
    te = event.pattern_match.group(1)
    col = random.choice(all_col) if te[0] == "r" else "White"
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            code = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            return await eor(xxxx, get_string("carbon_2"))
    xx = await Carbon(code=code, file_name="amang_carbon", backgroundColor=col)
    await xxxx.delete()
    await event.reply(
        f"Carbonised by {inline_mention(event.sender)}",
        file=xx,
    )


@amang_cmd(
    pattern="ccarbon( (.*)|$)",
)
async def crbn(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        return await event.eor(get_string("carbon_3"))
    msg = await event.eor(get_string("com_1"))
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            match = match.split(" ", maxsplit=1)
            code = match[1]
            match = match[0]
        except IndexError:
            return await eor(msg, get_string("carbon_2"))
    xx = await Carbon(code=code, backgroundColor=match)
    await msg.delete()
    await event.reply(
        f"Carbonised by {inline_mention(event.sender)}",
        file=xx,
    )


RaySoTheme = [
    "meadow",
    "breeze",
    "raindrop",
    "candy",
    "crimson",
    "falcon",
    "sunset",
    "midnight",
]

@amang_cmd(pattern="rayso")
async def pass_on(ay):
    spli = ay.text.split()
    theme, dark, title, text = None, True, get_display_name(ay.chat), None
    if len(spli) > 2:
        if spli[1] in RaySoTheme:
            theme = spli[1]
        dark = spli[2].lower().strip() in ["true", "t"]
    elif len(spli) > 1:
        if spli[1] in RaySoTheme:
            theme = spli[1]
        elif spli[1] == "list":
            text = "**List of Rayso Themes:**\n" + "\n".join(
                [f"- `{th_}`" for th_ in RaySoTheme]
            )

            await ay.eor(text)
            return
        else:
            try:
                text = ay.text.split(maxsplit=1)[1]
            except IndexError:
                pass
    if not theme:
        theme = random.choice(RaySoTheme)
    if ay.is_reply:
        msg = await ay.get_reply_message()
        text = msg.text
        title = get_display_name(msg.sender)
    await ay.reply(
        file=await Carbon(text, rayso=True, title=title, theme=theme, darkMode=dark)
    )