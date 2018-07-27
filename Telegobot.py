from flask import Flask, render_template
import telebot
from threading import Thread
import token

spylist = []

token = token.tk
bot = telebot.TeleBot(token = token)
telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}


@bot.message_handler(content_types = ['text'])
def read(message):
    chat_id = message.chat.id
    mes = message.text
    spylist.append({chat_id: mes})
    #print(spylist)

app = Flask(__name__)
@app.route('/')
def main():
    global spaylist
    return render_template('telegbotspy.html', mssgs=spylist)



def apprun():
    # Нашёл на stack overflow, почему не фласк просит использовать главный поток (main thread)
    # Дебаг включает перезагрузщик (reloader), которому нужен именно главный поток
    # Можно либо отключить дебаг, либо отключить перезагрузщик
    app.run(debug = True, use_reloader = False , port = 8080)



def polling():
    bot.polling(none_stop = True)

polling_threading = Thread(target = polling)
apprun_threading = Thread(target = apprun)
polling_threading.start()
apprun_threading.start()

#app.run(debug = True, port = 8080)
