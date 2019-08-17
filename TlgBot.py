import telebot
import requests
import json
import SolusVM as TS

TOKEN = "telegram bot token"
bot = telebot.TeleBot(TOKEN)
VMurl = "https://solusvm.gullo.me"
VMkey = "solusVm key"
VMtoken = "solusVm token"
solus = TS.SolusVMClient(VMurl, VMkey, VMtoken)

def random_joke(ctype=1):
    '''
    Sending random joke from rzhunemogu.ru in chat
    '''

    url = "http://rzhunemogu.ru/RandJSON.aspx"
    querystring = {"CType":str(ctype)}
    resp = requests.get(url, params=querystring)
    if resp.status_code == 200:
        utf8content = resp.content.decode("windows-1251").encode('utf-8').decode('utf-8')
        try:
            json_joke = json.loads(utf8content.replace('\r\n', '\\r\\n'))['content']
        except:
            json_joke = "Сервер прислал кривой JSON ответ"
    else:
        json_joke = "Сервер не доступен"
    print(json_joke)
    return json_joke

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Cписок доступных команд: \n /status - статус сервера \n /anecdot - анекдот")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, solus.status()['status'])

@bot.message_handler(commands=['anecdot'])
def send_status(message):
    bot.reply_to(message, random_joke(11))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

