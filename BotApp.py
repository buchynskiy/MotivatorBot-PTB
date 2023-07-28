from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from telegram.chataction import ChatAction
from quotes import quotes
from dotenv import load_dotenv
from time import sleep
import datetime
import random
import os

load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
APIKEY = os.environ.get('APIKEY')
TOKEN = APIKEY

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""Hello, {update.effective_user.first_name} \U0001F44B \n\n1. To receive motivational quotes daily press /motivation.\n2. To get extra information use /info.""")

def main() -> None:

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()