from telegram.ext import Updater, CommandHandler

TOKEN = "8468267497:AAHWMeqnKuQwKDC-CWHVZcEZMpegVxzxA9A"

def start(update, context):
    update.message.reply_text(
        "سلام! 👋\n"
        "من ربات مداستریم هستم.\n"
        "برای شروع /start رو زدی و آماده‌ام!"
    )

def main():
    updater = Updater(TOKEN, use_context=True, request_kwargs={'read_timeout': 20, 'connect_timeout': 20})
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("بات در حال اجراست...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
