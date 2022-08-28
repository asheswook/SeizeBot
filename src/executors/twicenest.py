from typing import Optional
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException
from src.utils.driver import get_driver
from src.utils.environment import Environment
from src.utils.logger import logger
import time
import os


class Twicenest:
    def __init__(self):
        self.driver = get_driver()
        self.title: str = None
        self.comment: str = None

    def _get_page(self, url: str):
        logger.info("get_page: %s" % url)
        self.driver.get(url)

    def _wait_for(self, by: By, value: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value)))

        return element

    def _wait_for_inv(self, by: By, value: str):
        element = WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located((by, value)))

        return element

    def _change_windowsize(self, width: int, height: int):
        """Change driver's window size"""
        self.driver.set_window_size(width, height)

    def _check_alert(self):
        try:
            result = Alert(self.driver)
            result.dismiss()

        except NoAlertPresentException:
            logger.info("No alert")
            pass

    def change_option(self, title: Optional[str] = None, comment: Optional[str] = None):
        if title:
            self.title = title
        if comment:
            self.comment = comment

    def POST(self):
        env = Environment()
        content = self.comment + "\n뮤비 조회수 봇은 TWICEWIKI에 의해 운영되고 관리됩니다.\n\n"

        logger.info("Start to twicenest post process")
        self._change_windowsize(1920, 1080)

        self._get_page("https://www.twicenest.com/board")

        logger.info("login...")
        self._wait_for(By.NAME, "user_id").send_keys(env.get("TWICENEST_ID"))
        self._wait_for(By.NAME, "password").send_keys(
            env.get("TWICENEST_PW"))

        self._wait_for(By.XPATH, '//*[@id="fo_login_widget"]/input[6]').click()
        time.sleep(5)
        logger.info("login success")

        logger.warning("Start to writing")
        self._get_page(
            "https://www.twicenest.com/index.php?mid=board&act=dispBoardWrite")
        time.sleep(3)

        self._check_alert()

        Select(self._wait_for(By.NAME, 'category_srl')).select_by_index(3)

        self._wait_for(By.NAME, "title").clear()
        self._wait_for(By.NAME, "title").send_keys(self.title)

        logger.info("Input content data to textarea")
        frame = self._wait_for(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.driver.switch_to.frame(frame)

        textarea = self._wait_for(By.XPATH, '//body')
        textarea.send_keys(content)

        self.driver.switch_to.default_content()
        logger.info("Input datas success")

        filepath = os.path.join(os.getcwd(), "src", "assets", "screen.png")

        logger.info("Start to upload file")
        self._wait_for(By.ID, 'xe-fileupload').send_keys(filepath)
        logger.info("Uploading...")
        self._wait_for_inv(By.CLASS_NAME, 'xefu-progress-status')
        logger.info("Upload success")

        self._wait_for(
            By.XPATH, '//*[@id="twnest_board_form"]/div[6]/input[2]').click()

        time.sleep(5)

        logger.warning("Post success")
