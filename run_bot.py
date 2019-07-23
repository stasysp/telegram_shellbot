from subprocess import check_output
import telebot
from telebot import apihelper
import time
import json


#apihelper.proxy = {'https': 'socks5://210929988:OOpkUQD1@orbtl.s5.opennetwork.cc:999'}
apihelper.proxy = {'https': 'socks5://telegram.vpn99.net:55655'}

with open('config.json', 'r') as conf:
     conf = json.load(conf)
token = conf['token']
user_id = conf['id']

bot = telebot.TeleBot(token)
print('lalala')

@bot.message_handler(content_types=["text"])
def main(message):
   if (user_id == message.chat.id):
      comand = message.text  
      try: 
         bot.send_message(message.chat.id, comand) #check_output(comand, shell = True))
      except:
         bot.send_message(message.chat.id, "Invalid input")
if __name__ == '__main__':
    #while True:
    #    try:
    bot.polling(none_stop=True, timeout=123)
    #    except:
    #        pass
    #        #time.sleep(10)
