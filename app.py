from component.default import *
from component.post_to_twicenest import *
from component.post_to_want import *
from component.post_to_wiki import *
from component.updateDB import *
from component.capture_wiki import *

version = "V2"
region = "ko"
documentName = "TWICE%2F뮤비%20조회수"
webdriver_path = '/usr/local/share/chromedriver'

testdriver = loadWebdriver(webdriver_path)


def doWork():
    db.ping(reconnect=True)  # DB 재연결

    try:
        data = updateDB("")

        driver = loadWebdriver(webdriver_path)
        editDocument(driver, data, region, documentName)
        captureDocument(driver, region, documentName)
        postImageToTN(driver, documentName)
        driver.quit()

        driver = loadWebdriver(webdriver_path)  # 드라이버 리로드
        postImageToWT(driver, documentName)
        driver.quit()

    except Exception as e:
        print(e)
        pass


schedule.every().day.at("07:59:40").do(doWork)

while True:
    schedule.run_pending()
    time.sleep(1)
