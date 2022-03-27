import time
import os
import platform
import datetime as dt
from config import *

try:
    import pafy
    import schedule
    import pymysql
    import json

    # Selenium
    from selenium import webdriver
    from selenium.webdriver.common.alert import Alert
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.remote.webelement import WebElement

except:
    os.system(
        'python' + ('3' if platform.system() != 'Windows' else '') + ' ' +
        '-m pip install -r requirements.txt'
    )


def getConnection():
    print("connect to db")
    db = pymysql.connect(
        user=mysql_config['username'],
        passwd=mysql_config['password'],
        host=mysql_config['host'],
        port=mysql_config['port'],
        db=mysql_config['dbname'],
        charset=mysql_config['charset']
    )
    print("ok")
    return db


def getWebdriver(driverpath='/usr/local/share/chromedriver'):
    print('kill chrome')
    os.system("pkill -9 chrome")

    print('import chromedriver...')
    if os.path.isfile(driverpath):
        pass
    else:
        print('*WARNING* Chromedriver has not found. Please check your chromedriver path.')
        exit()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("lang=ko_KR")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    driver = webdriver.Chrome(driverpath, chrome_options=options)  # 크롬드라이버 위치
    driver.set_window_size(1920, 1080)  # /usr/local/share/chromedriver
    print('ok')
    return driver


db = getConnection()
cursor = db.cursor(pymysql.cursors.DictCursor)
