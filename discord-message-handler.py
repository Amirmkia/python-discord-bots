
import discum
import requests
import os
from urllib.request import Request, urlopen
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json

bot = discum.Client(token= "mfa.W6KpZMPLWwMQszwfYgm0RGdjm1uXrcHuKDBkuQBvAAnXbFEW4ISidQ_x3ez0uXPEspjvOJFqpV1cjq07NSqb" , log = False )
token = "5043326687:AAHtuOLOHhGH-sJUYHgiVPhLjNlxC4LE-Ug"
channel = "-1001567582817"

# bot.sendMessage("435879828328022017" , "anyone know about bcoin?")
@bot.gateway.command
def home(resp):
     token = '5043326687:AAHtuOLOHhGH-sJUYHgiVPhLjNlxC4LE-Ug'
     bot = telegram.Bot(token=token)
     if resp.event.message:
         # general 
        if resp.raw['d']['channel_id'] == "435879828328022017": 
             text =  resp.raw['d']['content']
             try:
                if 'content' in resp.raw['d']:
                    if len(resp.raw['d']['content']) == 0:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                #discord-general
                                with open("general.jpg", "wb") as f:
                                    f.write(r.content)
                                    bot.send_photo("-1001255110447", open("./general.jpg",'rb') , caption = "#general")
                                #discord-general-meme
                                    bot.send_photo("-1001793492893", open("./general.jpg",'rb') , caption = "#general")
                                #discord-general-tradingchat
                                    bot.send_photo("-1001619388572", open("./general.jpg",'rb') , caption = "#general")
                                #discord-allchannel
                                    bot.send_photo("-1001600124884", open("./general.jpg",'rb') , caption = "#general")
                    else:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                text = resp.raw['d']['content']
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                with open("general.jpg", "wb") as f:
                                    f.write(r.content)
                                 #discord-general
                                bot.send_photo("-1001255110447", open("./picture.jpg",'rb') , caption = "#general" + "\n" + str(text))
                                #discord-general-meme
                                bot.send_photo("-1001793492893", open("./general.jpg",'rb') , caption = "#general" + "\n" + str(text))
                                #discord-general-tradingchat
                                bot.send_photo("-1001619388572", open("./general.jpg",'rb') , caption = "#general" + "\n" + str(text))
                                #discord-allchannel
                                bot.send_photo("-1001600124884", open("./general.jpg",'rb') , caption = "#general" + "\n" + str(text))
                            else:
                                text = resp.raw['d']['content']
                                #discord-general
                                bot.send_message("-1001255110447" , "#general" + "\n" + str(text) )
                                #discord-general-meme
                                bot.send_message("-1001793492893" , "#general" + "\n" + str(text) )
                                #discord-general-tradingchat
                                bot.send_message("-1001619388572" , "#general" + "\n" + str(text) )
                                #discord-allchannel
                                bot.send_message("-1001600124884" , "#general" + "\n" + str(text) )
                        else:
                            text = resp.raw['d']['content']
                            #discord-general
                            bot.send_message("-1001255110447" , "#general" + "\n" + str(text) )
                            #discord-general-meme
                            bot.send_message("-1001793492893" , "#general" + "\n" + str(text) )
                            #discord-general-tradingchat
                            bot.send_message("-1001619388572" , "#general" + "\n" + str(text) )
                            #discord-allchannel
                            bot.send_message("-1001600124884" , "#general" + "\n" + str(text) )
             except IndexError:
                print('index error')
        # trading-chat
        if resp.raw['d']['channel_id'] == "804507369588785192": 
             text =  resp.raw['d']['content']
             try:
                if 'content' in resp.raw['d']:
                    if len(resp.raw['d']['content']) == 0:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                with open("tradingchat.jpg", "wb") as f:
                                    f.write(r.content)
                                    #discord-trading-chat
                                    bot.send_photo("-1001767018543", open("./tradingchat.jpg",'rb') , caption = "#trading-chat")
                                    #discord-tradingchat-general
                                    bot.send_photo("-1001619388572", open("./tradingchat.jpg",'rb') , caption = "#trading-chat")
                                    #discord-tradingchat-meme
                                    bot.send_photo("-1001524043423", open("./tradingchat.jpg",'rb') , caption = "#trading-chat")
                                    #dicord-allchannel
                                    bot.send_photo("-1001600124884", open("./tradingchat.jpg",'rb') , caption = "#trading-chat")
                    else:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                text = resp.raw['d']['content']
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                with open("tradingchat.jpg", "wb") as f:
                                    f.write(r.content)
                                #discord-trading-chat
                                bot.send_photo("-1001767018543" , open("./tradingchat.jpg",'rb') , caption = "#trading-chat" + "\n" + str(text))
                                #discord-tradingchat-general
                                bot.send_photo("-1001619388572" , open("./tradingchat.jpg",'rb') , caption = "#trading-chat" + "\n" + str(text))
                                #discord-tradingchat-meme
                                bot.send_photo("-1001524043423" , open("./tradingchat.jpg",'rb') , caption = "#trading-chat" + "\n" + str(text))
                                #discord-allchannel
                                bot.send_photo("-1001600124884" , open("./tradingchat.jpg",'rb') , caption = "#trading-chat" + "\n" + str(text))
                            else:
                                text = resp.raw['d']['content']
                                #discord-trading-chat
                                bot.send_message("-1001767018543" , "#trading-chat" + "\n" + str(text) )
                                #discord-tradingchat-general
                                bot.send_message("-1001619388572" , "#trading-chat" + "\n" + str(text) )
                                #discord-tradingchat-meme
                                bot.send_message("-1001524043423" , "#trading-chat" + "\n" + str(text) )
                                #discord-allchannel
                                bot.send_message("-1001600124884" , "#trading-chat" + "\n" + str(text) )
                        else:
                            text = resp.raw['d']['content']
                            #discord-trading-chat
                            bot.send_message("-1001767018543" , "#trading-chat" + "\n" + str(text) )
                            #discord-tradingchat-general
                            bot.send_message("-1001619388572" , "#trading-chat" + "\n" + str(text) )
                            #discord-tradingchat-meme
                            bot.send_message("-1001524043423" , "#trading-chat" + "\n" + str(text) )
                            #discord-allchannel
                            bot.send_message("-1001600124884" , "#trading-chat" + "\n" + str(text) )
             except IndexError:
                print('index error')

        # memes
        if resp.raw['d']['channel_id'] == "804505783269720084": 
             text =  resp.raw['d']['content']
             try:
                if 'content' in resp.raw['d']:
                    if len(resp.raw['d']['content']) == 0:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                with open("memes.jpg", "wb") as f:
                                    f.write(r.content)
                                    #discord-memes
                                    bot.send_photo("-1001568892754", open("./memes.jpg",'rb') , caption = "#memes")
                                    #discord-memes-general
                                    bot.send_photo("-1001793492893", open("./memes.jpg",'rb') , caption = "#memes")
                                    #discord-memes-tradingchat
                                    bot.send_photo("-1001524043423", open("./memes.jpg",'rb') , caption = "#memes")
                                    #discord-allchannel
                                    bot.send_photo("-1001600124884", open("./memes.jpg",'rb') , caption = "#memes")
                    else:
                        if len(resp.raw['d']['attachments']) != 0 :
                            if 'url' in resp.raw['d']['attachments'][0]:
                                text = resp.raw['d']['content']
                                picture = resp.raw['d']['attachments'][0]['url']
                                r = requests.get(resp.raw['d']['attachments'][0]['url'])
                                with open("memes.jpg", "wb") as f:
                                    f.write(r.content)
                                #discord-memes
                                bot.send_photo("-1001568892754" , open("./memes.jpg",'rb') , caption = "#memes" + "\n" + str(text))
                                #discord-memes-general
                                bot.send_photo("-1001793492893" , open("./memes.jpg",'rb') , caption = "#memes" + "\n" + str(text))
                                #discord-memes-tradingchat
                                bot.send_photo("-1001524043423" , open("./memes.jpg",'rb') , caption = "#memes" + "\n" + str(text))
                                #discord-allchannel
                                bot.send_photo("-1001600124884" , open("./memes.jpg",'rb') , caption = "#memes" + "\n" + str(text))
                            else:
                                text = resp.raw['d']['content']
                                #discord-memes
                                bot.send_message("-1001568892754" , "#memes" + "\n" + str(text) )
                                #discord-memes-general
                                bot.send_message("-1001793492893" , "#memes" + "\n" + str(text) )
                                #discord-memes-tradingchat
                                bot.send_message("-1001524043423" , "#memes" + "\n" + str(text) )
                                #discord-allchannel
                                bot.send_message("-1001600124884" , "#memes" + "\n" + str(text) )
                        else:
                            text = resp.raw['d']['content']
                            #discord-memes
                            bot.send_message("-1001568892754" , "#memes" + "\n" + str(text) )
                            #discord-memes-general
                            bot.send_message("-1001793492893" , "#memes" + "\n" + str(text) )
                            #discord-memes-tradingchat
                            bot.send_message("-1001524043423" , "#memes" + "\n" + str(text) )
                            #discord-allchannel
                            bot.send_message("-1001600124884" , "#memes" + "\n" + str(text) )
             except IndexError:
                print('index error')
        
if __name__ == '__main__':
    bot.gateway.run()
    home()
