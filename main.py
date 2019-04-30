import sys
import requests
import _thread
from time import time,localtime,strftime,sleep
from twilio.rest import Client
from flask import Flask,render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path

path_of_the_program = path.dirname(__file__)
app = Flask(__name__)
empty_base_code = "<h1>Nothing here</h1>"

updated_time = time()
# Now, we init the updated time by using updated_time = time()

twilio_account_sid = "AC48a5e19bc3216c8d989b6a49491fd2af"
twilio_auth_token = 'b78a6784b0efbe8352f5119cce866274'
twilio_client = Client(twilio_account_sid,twilio_auth_token)
# It's a kind of free sms service.

chrome_options = Options()
chrome_driver = webdriver.Chrome(chrome_options=chrome_options)

@app.route('/')
def index():
   return render_template('index.html')



if __name__ == "__main__":
    pass
