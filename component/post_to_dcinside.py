from .default import *


def post_to_dcinside(driver: webdriver, documentName: str, specialComment=""):
    delay = 3

    driver.set_window_size(1920, 1080)
    print('access board link...')
    driver.get('https://www.twicenest.com/board')
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

    """
    filepath = os.getcwd() + '/cache/screenie.png'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'xe-fileupload')))
    driver.find_element_by_id("xe-fileupload").send_keys(filepath)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(
        (By.XPATH, 'xefu-container-2')))  # Wait until file uploaded
    """

    driver.find_element_by_class_name(
        'write').click()
    time.sleep(3)
    print('end')
