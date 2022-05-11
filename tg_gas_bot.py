#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 23:33:34 2022

@author: horden
"""

from etherscan import Etherscan
from telegram.ext import Updater,CommandHandler	,MessageHandler,Filters	,InlineQueryHandler,ChosenInlineResultHandler,CallbackQueryHandler,Filters
import telegram
from telegram import InlineQueryResultArticle,InputTextMessageContent,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
import requests
import threading
import time

eth=Etherscan("your etherscan api token")
gas_oracle = eth.get_gas_oracle()
print(gas_oracle["SafeGasPrice"])


bot_token="your telegram bot token"

updater = Updater(bot_token, use_context=True)
bot = telegram.Bot(bot_token)



#全域變數區
LatestSafeGas=gas_oracle["SafeGasPrice"]
userchatid_dict = dict()
user_index = list()


def start(update: Update, context: CallbackContext):
    update.message.reply_text("輸入/getprice以獲取目前GasPrice")




def getpricee(update: Update, context: CallbackContext):
    update.message.reply_text(gas_oracle["SafeGasPrice"])
    #update.sendMessage(chat_id = update.message.chat.id,text = gas_oracle["SafeGasPrice"] + str(chat['id']),reply_markup = button)

def getuserchatid(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.chat.id)



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('getprice', getpricee))
updater.dispatcher.add_handler(CommandHandler('id', getuserchatid))


updater.start_polling()
updater.idle()
