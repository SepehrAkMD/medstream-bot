import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8468267497:AAHWMeqnKuQwKDC-CWHVZcEZMpegVxzxA9A")  # TOKEN را از متغیر محیطی می‌خواند

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! بات MedStream فعال است! 🚀")

def main():
    app = ApplicationBuilder().token(TOKEN).build()  # بجای Updater
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
