import sys
import requests
import _thread
from time import time,localtime,strftime,sleep
from twilio.rest import Client
from flask import Flask,render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from os import path

path_of_the_program = path.dirname(__file__)
app = Flask(__name__)
webside_raw = "<h1>Nothing here</h1>"

updated_time = time()
# Now, we init the updated time by using updated_time = time()

twilio_account_sid = "AC48a5e19bc3216c8d989b6a49491fd2af"
twilio_auth_token = 'b78a6784b0efbe8352f5119cce866274'
twilio_client = Client(twilio_account_sid,twilio_auth_token)
# It's a kind of free sms service.


firefox_driver = webdriver.Firefox()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/now_code')
def now_code():
   global webside_raw,updated_time
   soup = BeautifulSoup(webside_raw)
   safe_code = soup.getText()
    #----Start deal with time
   timeArray = localtime(updated_time)
   styled_time = strftime("%Y-%m-%d %H:%M:%S", timeArray)
   return render_template('take_a_look_at_code.html', code=safe_code,updated_time=styled_time)

@app.route('/now_image')
def send_image():
   return render_template('screen_shot_view.html')


def make_screen_shot():
   global firefox_driver
   firefox_driver.get("https://cybersole.io")
   firefox_driver.maximize_window()
   sleep(1)
   scroll_js = "window.scrollTo(0,300)"
   firefox_driver.execute_script(scroll_js)
   firefox_driver.get_screenshot_as_file(path_of_the_program+r"\static\screen_shot.png")


def main():
   print("[BoT] The system now started to work.")
   global webside_raw,updated_time
   not_the_first_time_spy_on_the_webside_question_mark = False
   while True:
      sleep(30)
      # TODO: I want to make a config file whcih can set the time between every spy
      print("[BoT]The bot now started to spy.")
      updated_time = time()
      what_I_got_from_my_target = requests.get(url='https://cybersole.io').text
      if what_I_got_from_my_target != webside_raw:
         print("[BoT]Something very intersting heappend on:")
         webside_raw = what_I_got_from_my_target
         make_screen_shot()
         if not_the_first_time_spy_on_the_webside_question_mark:
            sms_message = twilio_client.messages.create(body="\n[SKY'sBOT TEST MESSAGE]Mr.HUGO, it's time to PURCHASE.",from_='+17867890385', to='+8618858298361')
            print(sms_message.sid)
         else:
            print("[BoT]The 1st move was successful.")
            not_the_first_time_spy_on_the_webside_question_mark = True

      

  

   

def startServer():
   _thread.start_new_thread(main,())
   app.run(debug=False,port=3000)

if __name__ == "__main__":
    startServer()
