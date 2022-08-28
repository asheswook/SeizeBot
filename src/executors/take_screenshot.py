from selenium import webdriver
from src.utils.driver import get_driver
import os
import time


def take_screen(height: int):
    driver = get_driver()
    driver.set_window_size(700, height)

    index_file = os.path.join(os.getcwd(), 'src', 'assets', 'index.html')

    driver.get("file:///" + index_file)
    time.sleep(5)
    driver.save_screenshot("src/assets/screen.png")
    driver.quit()
