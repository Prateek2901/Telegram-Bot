from telegram.ext import Updater, CommandHandler ,MessageHandler
from telegram import ChatAction
import telegram

from time import sleep
bot = telegram.Bot(token=TOKEN)
from telegram.ext import Updater
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
print(dispatcher)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
	bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	bot.send_message(chat_id=update.message.chat_id, text="I'm a _*FUZZBUZZ*_.\n I can keep you updated with:-\n - *Live Cricket Score*\n - *Recent News HeadLine*\n /help for more info",
	parse_mode=telegram.ParseMode.MARKDOWN)

def score(bot,update):
	from CricketScore import liveScore
	bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)

	(head,teams,matchType,status) = liveScore()
	for i,j,k,l in zip(head,teams,matchType,status):
		bot.send_message(chat_id=update.message.chat_id, text="*{}*\n - *Teams* {}\n - *Match Type* {}\n - *Status* {}".format(i,j,k,l),
		parse_mode=telegram.ParseMode.MARKDOWN)
		sleep(0.3)

def news(bot,update,args):
	from News import all_News
	bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	if len(args) != 0:
		(title,description,url) = all_News(args)
		for j,k,l in zip(title,description,url):
			print("[{}]({}) \n _{}_".format(j,l,k))
			bot.send_message(chat_id=update.message.chat_id,  text="[{}]({}) \n _{}_".format(j,l,k),
			parse_mode=telegram.ParseMode.MARKDOWN)
			sleep(0.3)
	else:
		bot.send_message(chat_id=update.message.chat_id,  text="Hay!! Seems you missed the Topic.\n Why not give it a try again?")

def help(bot, update):
	bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	bot.send_message(chat_id=update.message.chat_id, text="- /score for *Live Cricket Score* \n - /news _<TOPIC>_ for *Recent News*",
	parse_mode=telegram.ParseMode.MARKDOWN)

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('news', news,pass_args=True))
dispatcher.add_handler(CommandHandler('score', score))
dispatcher.add_handler(CommandHandler('help', help))
from telegram.ext import RegexHandler
dispatcher.add_handler(RegexHandler(r'/.*', unknown))

updater.start_polling()
