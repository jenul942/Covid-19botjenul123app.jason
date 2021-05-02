import os
import logging
import telebot
import requests
import time
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)

HSbot = Client(
   "covid-19 Bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@HSbot.message_handler(commands=["start", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello New guy this is the covid-19 stats bot type /details")
    

@HSbot.message_handler(commands=["help", "hlp", "feedback"])
def hello(message):
    bot.send_message(message.chat.id, "Any feedback @JenulRanthisa")

@HSbot.message_handler(commands=['/details'])
def details(message):
  page = requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
  after_bs = BeautifulSoup(page.content, 'html.parser')
  find_data = after_bs.find_all(id="maincounter-wrap")
  output = ''
  for x in find_data:
      # print(x.text)
      output = output + x.text
  
  bot.reply_to(message, output)
  

HSbot.run()