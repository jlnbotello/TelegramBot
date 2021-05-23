# Useful links
# https://github.com/python-telegram-bot/python-telegram-bot
# https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html#
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import logging
from telegram import Bot

with open('token.txt', 'rt') as f:
    token = next(f)
    token = token.strip('\n')
    colo_id = next(f)
    colo_id = colo_id.strip('\n')
    me_id = next(f)
    me_id = me_id.strip('\n')

updater = Updater(token = token)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Colito, soy el bot amigo de Junco")
    print(update.effective_chat.id)
    
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Por el momento solo puedo hacer eco de tus mensaje:\n"+update.message.text)

def photo(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = 'https://www.askideas.com/wp-content/uploads/2016/11/Funny-Dog-Face-During-Selfie.jpg')

start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hello', hello)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
photo_handler = CommandHandler('photo', photo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(photo_handler)

bot = Bot(token = token)
bot.send_message(chat_id = me_id, text = 'Bot Started')
#bot.send_message(chat_id = colo_id, text = 'Bot Started')

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
updater.start_polling()




