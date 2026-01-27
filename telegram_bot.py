# -- coding: utf-8 --
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from core import get_bot_reply

TOKEN = "8259950565:AAFHOS64YprzALSOmnScaa8CDfwhW0NWSR4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋\n"
        "Saya bot Sazkia Printing.\n\n"
        "Silakan tanya seputar:\n"
        "- Jam operasional\n"
        "- Alamat toko\n"
        "- Cara order\n"
        "- Produk yang tersedia"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    jawaban = get_bot_reply(user_text)
    await update.message.reply_text(jawaban)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot Telegram Sazkia Printing sedang berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
