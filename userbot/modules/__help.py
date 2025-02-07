import logging

from userbot import BOT_USERNAME
from userbot.utils import kyy_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@kyy_cmd(pattern="helpme(?: |$)(.*)")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@IdNyaKosong")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya tidak berfungsi! Silahkan atur Bot Token dan Username dengan benar. Modul telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat mengirim hasil sebaris dalam hal ini ke chat (disebabkan oleh Mengirim Inline Sebaris)\ngunakan perintah .inlineon`"
        )
