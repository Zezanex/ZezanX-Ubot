""" Userbot help command """

from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_delete, edit_or_reply, kay_cmd
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@kay_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, "`Command` **Tidak Valid**")
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ‽ "
        await edit_or_reply(event, "**🐣ZezanX-υѕєявσт🐣**\n\n"
                            f"**◉ Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◉ Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                            "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                            f"◉ {string}◉\n\n☞   : https://t.me/zezanx")
        await event.reply(
            f"\n**Contoh Ketik** `{cmd}help animasi` **Untuk Melihat Informasi Module**"
        )
