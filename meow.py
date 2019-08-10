from telegram.ext import Updater, CommandHandler
import logging
import requests
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelName)s - %(message)s', level=logging.INFO)

with open('config.json') as config_file:
    data = json.load(config_file)

def say_meow(bot, update):
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    reply_message = r.json()[0]['url']
    print('meow by {}'.format(update.message.from_user.first_name))
    update.message.reply_text(reply_message)

updater = Updater(data['bot_token'])

updater.dispatcher.add_handler(CommandHandler('meow', say_meow))
updater.start_polling()
updater.idle()