from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=ko_KR")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    return driver
