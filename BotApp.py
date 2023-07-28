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

def info(update: Update, context: CallbackContext) -> None:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(2)
    reply_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bot sent similar quotes", callback_data='similar')],
        [InlineKeyboardButton("Another language of quotes", callback_data='lang')],
        [InlineKeyboardButton("How many quotes are there", callback_data='amount')],
        [InlineKeyboardButton("Want to contact owner", callback_data='owner')],
    ])
    update.message.reply_text('Please, choose the topic that you need more information about:',
    reply_markup=reply_buttons)

def enough(update: Update, context: CallbackContext) -> None:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(1)
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    update.message.reply_text('If you want to stop receiving motivation from the bot --> just delete the chat with the bot.')

def echo(update: Update, context: CallbackContext) -> None:
    default_message = 'I am just a bot. Sometimes there are things I don\'t understand \U0001F916'
    update.message.reply_text(default_message, reply_to_message_id=update._effective_message.message_id)

def button(update: Update, context: CallbackContext) -> None:
    update.callback_query.answer()
    update.callback_query.message.edit_reply_markup(
    reply_markup=InlineKeyboardMarkup([])
    )
    if update.callback_query.data == 'similar':
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(1)
        update.callback_query.message.reply_photo(photo=open('images/botwant.jpg', 'rb'))
        update.callback_query.message.reply_text("Bot just wants you to keep your focus on certain things and not loose hope \U0001F607")

    elif update.callback_query.data == 'lang':
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(1)
        update.callback_query.message.reply_photo(photo=open('images/sadbot.jpg', 'rb'))
        update.callback_query.message.reply_text("Unfortunately, the only supported language is English.")

    elif update.callback_query.data == 'amount':
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(1)
        update.callback_query.message.reply_text(f'For now, the library of quotes consists of over {len(quotes)} motivational quotes.')
    
    elif update.callback_query.data == 'owner':
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(1)
        update.callback_query.message.reply_text('Here\'s a username of a developer of this bot: @petroszybkosc')

def main() -> None:

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(CommandHandler('enough', enough))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()