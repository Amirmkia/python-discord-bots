from flask import *
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


app = Flask(__name__)

@app.route('/tradingview', methods=['GET', 'POST'])
def home():
   
    json_data = request.data
    w = ''.join(map(chr, json_data))
    message = "⭕️   Alarm Reached   ⭕️" + "\n\n" +"Name 👉 " + str(w) + "\n\n" 
    
    telegram_bot_sendText(message)
    return message

def telegram_bot_sendText(bot_message):
   
    bot_token = "5052530382:AAE_Iy92pnJXDO67ljI96CCIzSp_pbvdd_M"
    bot_chtID = "-1001309970230"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chtID +\
         "&parse_mode=Markdown&text="+ bot_message
    json_data = request.data
    CoinName = json_data.split()
    s = ''.join(map(chr, CoinName[0]))
    payload = {
    f'interval=4h&&studies=RSI&&studies=MA:200,close&studies=MA:50,close&symbol': str(s),
    'studies':
        [
     'RSI', 
     'MA:200,close'
        ]
    }
    requests.get(send_text, params = payload)
    url  = "https://api.chart-img.com/v1/tradingview/advanced-chart" 
    r = requests.get( url , params = payload)
    send_text2 = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chtID +\
         "&parse_mode=Markdown&text="+ str(r.url)
    requests.get(send_text2)

    

if __name__ == '__main__':
    app.run(debug=True) 
    home()
