import requests # URL로 요청을 날리는 모듈 (slack한테 요청)
import json # 클라이언트 - 서버가 통신하는 규율, 규격
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_google_news():
    browser = webdriver.Chrome("chromedriver")
    url = 'https://weather.naver.com/today/09410101?cpName=KMA'
    browser.get(url)

    weather_whole = browser.find_element(By.CLASS_NAME, 'summary_img')

    temp = weather_whole.find_element(By.CLASS_NAME, 'current')

    return temp.text


def send_slack_message():
    bot_url = 'https://hooks.slack.com/services/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'

    payload = {
        "text" : get_google_news()
    }

    # get, post => CRUD
    response = requests.post(
        bot_url,
        data = json.dumps(payload),
        headers = {"Content-Type": "application/json"}
    )


    print(response)

send_slack_message()

