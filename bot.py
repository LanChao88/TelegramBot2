from telegram import Update
import re
from telegram.ext import Application, MessageHandler, filters
import os

TOKEN = os.getenv("TOKEN")


async def calc(update, context):

    text = update.message.text.strip()

    # 地址功能
    if text in ["地址", "结算", "钱包"]:

        address = "TP88hmjvfxcvW4xQg3r53j5iTZfXXuuTDr"

        msg = f"""
LC-亓亓唯一收款地址

<code>{address}</code>

🔝点击地址可自动复制🔝

⚠️前6位：{address[:6]}
⚠️中6位：{address[6:12]}
⚠️后6位：{address[-6:]}

⚠️烦请核对好，若有账户差异请勿打入。
避免转到钓鱼山寨地址。
"""

        await update.message.reply_text(
            msg,
            parse_mode="HTML"
        )
        return

    # 加减乘除
   if (
    not re.fullmatch(r"[0-9+\-*/().\s]+", text)
    or not re.search(r"[+\-*/]", text)
):
    return

    try:
        result = eval(text)

        if isinstance(result, float):
            if result.is_integer():
                result = int(result)

        await update.message.reply_text(str(result))

    except:
        pass


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, calc)
)

print("机器人启动成功")

app.run_polling()

app.run_polling()
