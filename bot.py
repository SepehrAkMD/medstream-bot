import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# TOKEN را مستقیم اینجا هم میتونی قرار بدی یا از محیط بگیری
TOKEN = os.getenv("BOT_TOKEN")  # حتماً در Railway متغیر BOT_TOKEN تعریف شده باشد

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! بات MedStream فعال است! 🚀")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()  # فقط همین، هیچ Updater اضافه‌ای نیاز نیست

if __name__ == "__main__":
    main()
