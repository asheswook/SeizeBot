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


class Dcinside:
    def __init__(self, gallery):
        """Maybe works only minor gallery"""
        self.driver = get_driver()
        self.title: str = None
        self.comment: str = None
        self.gallery: str = gallery

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

    def _wait_for_cab(self, by: By, value: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value)))

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

        logger.info("Start to dcinside post process")
        self._change_windowsize(1920, 1080)

        self._get_page("https://dcinside.com")

        logger.info("login...")
        self._wait_for(By.NAME, "user_id").send_keys(env.get("DCINSIDE_ID"))
        self._wait_for(By.NAME, "pw").send_keys(
            env.get("DCINSIDE_PW"))

        self._wait_for(By.ID, 'login_ok').click()
        time.sleep(5)
        logger.info("login success")

        logger.warning("Start to writing")
        self._get_page(
            f"https://gall.dcinside.com/mgallery/board/write/?id={self.gallery}")
        time.sleep(3)

        self._check_alert()

        self._wait_for(By.CLASS_NAME, 'subject_list')
        self._wait_for(
            By.CSS_SELECTOR, '#write > div.clear > fieldset > div.write_subject.clear > ul > li:nth-child(5)').click()

        self._wait_for(By.ID, "subject").clear()
        self._wait_for(By.ID, "subject").send_keys(self.title)

        logger.info("Input content data to textarea")
        frame = self._wait_for(By.XPATH, '//*[@id="tx_canvas_wysiwyg"]')
        self.driver.switch_to.frame(frame)

        textarea = self._wait_for(By.XPATH, '//body')
        textarea.send_keys(content)

        self.driver.switch_to.default_content()
        logger.info("Input datas success")

        filepath = os.path.join(os.getcwd(), "src", "assets", "screen.png")

        logger.info("Start to upload file")
        self._wait_for(By.CSS_SELECTOR, "#tx_image > a").click()
        time.sleep(2)

        self.driver.switch_to.window(
            self.driver.window_handles[1])  # change window tab

        self._wait_for(By.CLASS_NAME, 'file_add').send_keys(filepath)
        logger.info("Uploading...")

        time.sleep(1)
        self._wait_for_inv(By.CSS_SELECTOR, '.loding_bar.bar')
        # wait until file uploaded

        self._wait_for(By.CLASS_NAME, 'btn_apply').click()
        time.sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[0])  # go back

        logger.info("Upload success")

        self._wait_for(
            By.CSS_SELECTOR, ".btn_blue.btn_svc.write").click()

        time.sleep(5)

        logger.warning("Post success")
