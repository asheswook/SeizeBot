from .default import *


def post_to_dcinside(driver: webdriver, documentName: str, specialComment=""):
    delay = 3

    driver.set_window_size(1920, 1080)
    print('access board link...')
    driver.get('https://dcinside.com')
    print('login...')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'user_id')))
    driver.find_element_by_name('user_id').send_keys(dc_config['id'])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'pw')))
    driver.find_element_by_name('pw').send_keys(
        dc_config['password'])

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, 'login_ok')))
    driver.find_element_by_id('login_ok').click()
    time.sleep(5)

    print('access board write link...')
    driver.get('https://gall.dcinside.com/mgallery/board/lists/?id=twiceyou')
    time.sleep(3)
    driver.get('https://gall.dcinside.com/mgallery/board/write/?id=twiceyou')
    time.sleep(3)

    print('start to type data...')

    title = '[08:00] 트와이스 뮤비 조회수'

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'subject_list')))
    driver.find_element_by_css_selector(
        '#write > div.clear > fieldset > div.write_subject.clear > ul > li:nth-child(5)').click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'subject')))
    driver.find_element_by_id('subject').clear()
    driver.find_element_by_id('subject').send_keys(title)

    contentData = specialComment + "뮤비 조회수 봇은 TWICEWIKI에 의해 운영되고 관리됩니다.\n" + \
        "https://ko.twice.wiki/w/" + documentName + "\n\n"

    print('Input content data...')
    basic_page_body_xpath = '//*[@id="tx_canvas_wysiwyg"]'
    ckeditor_frame = driver.find_element_by_xpath(basic_page_body_xpath)
    driver.switch_to.frame(ckeditor_frame)
    editor_body = driver.find_element_by_xpath("//body")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body")))
    editor_body.send_keys(contentData)
    driver.switch_to.default_content()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#tx_image > a"))).click()
    time.sleep(1)
    image_upload = driver.window_handles[1]
    driver.switch_to.window(image_upload)

    filepath = os.getcwd() + '/cache/screenie.png'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'file_add'))).send_keys(filepath)

    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, '.loding_bar.bar')))  # Wait until file uploaded

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn_apply'))).click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".btn_blue.btn_svc.write"))).click()
    time.sleep(3)
    print('end')
