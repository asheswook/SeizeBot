from component.default import *
from component.post_to_dcinside import post_to_dcinside
from component.post_to_twicenest import *
from component.post_to_want import *
from component.post_to_wiki import *
from component.updateDB import *
from component.capture_wiki import *

version = "V2"
region = "ko"
documentName = "TWICE%2F뮤비%20조회수"
webdriver_path = '/usr/local/share/chromedriver'
testdriver = getWebdriver(webdriver_path)

def doWork():
    db.ping(reconnect=True)  # DB 재연결

    try:
        data = get_Vitaldata()

        driver = getWebdriver(webdriver_path)
        post_to_wiki(driver, data, region, documentName)
        capture_wiki(driver, region, documentName)
        post_to_twicenest(driver, documentName)
        driver.quit()

        driver = getWebdriver(webdriver_path)  # 드라이버 리로드
        post_to_want(driver, documentName)
        driver.quit()

        driver = getWebdriver(webdriver_path)  # 드라이버 리로드
        post_to_dcinside(driver, documentName)
        driver.quit()

    except Exception as e:
        print(e)
        pass


schedule.every().day.at("07:59:40").do(doWork)

while True:
    schedule.run_pending()
    time.sleep(1)
