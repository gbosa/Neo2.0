import telebot
from telebot.types import Message
import cerebelo as celebro
import random as rd
import numpy as np
import time

bot = telebot.TeleBot('5842578280:AAHDluEsOqq0VKw2GZRomVfzQIdYAOgIUxM')
on = False
quem = 'neo2'

greet=['Hallo','Olá','Здравейте','Bonjour','Γεια','שלום (Shalom)','Ciao',
"こんにちは (Konnichiwa)",'안녕 (Annyeong)','Привет','Ahoj','你好 (Nǐ hǎo)',
'नमस्ते (Namaste)',' ٱلسَّلَامُ عَلَيْكُ (Salaam Aleikum)','¡Hola!']

@bot.message_handler(commands=['puta','mimir','quem','id','chance'])
def send_message(message):
    global on; global quem
    
    command = message.text.split()[0]
    
    c=celebro.Cerebelo('frases.db')
    try:
        c.add_status((int(message.chat.id), 0))
    except:
        pass
              
    if command == '/puta' and not c.get_status(message.chat.id):
        c.update_status((message.chat.id,1))
        bot.send_message(message.chat.id, f'{rd.choice(greet)} sherbas')
    
    elif command in ['/mimir'] and c.get_status(message.chat.id):
        c.update_status((message.chat.id,0))
        bot.send_message(message.chat.id, 'Vou me suicidar')
   
    on = c.get_status(message.chat.id)
    
    if on:
        if command == '/quem':
            quem = c.query_msg(message.reply_to_message.text)
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(1)            
            bot.send_message(message.chat.id, quem[0])
            print(message.reply_to_message.text)
        
        elif command == '/id':
            c=celebro.Cerebelo('frases.db')
            rowzap=c.query_rowid(message.text.split()[1])
            quem=rowzap[0]        
            bot.send_message(message.chat.id, rowzap[1])
        
        elif command == '/chance':
            abc = message.text.lstrip('/chance ')
            abc=abc.strip('?')
            prob = f'A chance é de aproximadamente {round(rd.uniform(0,1)*100,2)}% {abc}'
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(len(prob)*0.02)
            bot.send_message(message.chat.id, prob)
        
    c.close_conn()
    
@bot.message_handler(content_types=['text'])
def send_reply(message: Message):
    global on; p = 0.6; global quem
    c=celebro.Cerebelo('frases.db')
    
    if c.get_status(message.chat.id):
        if p <= rd.uniform(0,1) and not ('neo' in str(message.text)):
            chatzap=c.query_rowid(rd.randint(1,30145))
            quem=chatzap[0]
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(len(chatzap[1])*0.03)
            bot.send_message(message.chat.id, chatzap[1])  

        elif ('neo' in str(message.text).lower()):
            chatzap=c.query_rowid(rd.randint(1,30145))
            quem=chatzap[0]
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(len(chatzap[1])*0.03)
            bot.reply_to(message, chatzap[1])
        
        c.close_conn()
            
bot.infinity_polling()