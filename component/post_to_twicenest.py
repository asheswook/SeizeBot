from .default import *


def postImageToTN(driver, documentName, specialComment=""):
    delay = 3

    driver.set_window_size(1920, 1080)
    print('access board link...')
    driver.get('https://www.twicenest.com/board')
    print('login...')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'user_id')))
    driver.find_element_by_name('user_id').send_keys(tnConfig('id'))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password')))
    driver.find_element_by_name('password').send_keys(tnConfig('password'))

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="fo_login_widget"]/input[6]')))
    driver.find_element_by_xpath('//*[@id="fo_login_widget"]/input[6]').click()
    print('access board write link...')
    driver.get('https://www.twicenest.com/index.php?mid=board&act=dispBoardWrite')
    time.sleep(3)
    try:
        result = Alert(driver)
        result.dismiss()
    except:
        pass
    driver.get('https://www.twicenest.com/index.php?mid=board&act=dispBoardWrite')
    driver.implicitly_wait(delay)
    try:
        print('alarm')
        result = Alert(driver)
        result.accept()
    except:
        print('pass alarm')
        pass

    #postImageToTN.printlog('switch to iframe...')
    #iframe = driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
    # driver.switch_to.frame(iframe)
    print('start to type data...')

    title = '[08:00] 트와이스 뮤비 조회수'

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'category_srl')))
    select_fr = Select(driver.find_element_by_name('category_srl'))
    select_fr.select_by_index(3)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'title')))
    driver.find_element_by_name('title').clear()
    driver.find_element_by_name('title').send_keys(title)

    contentData = specialComment + "뮤비 조회수 봇은 TWICEWIKI에 의해 운영되고 관리됩니다.\n" + \
        "https://ko.twice.wiki/w/" + documentName + "\n\n"

    print('Input content data...')
    basic_page_body_xpath = '//*[@id="cke_1_contents"]/iframe'
    ckeditor_frame = driver.find_element_by_xpath(basic_page_body_xpath)
    driver.switch_to.frame(ckeditor_frame)
    editor_body = driver.find_element_by_xpath("//body")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body")))
    editor_body.send_keys(contentData)
    driver.switch_to.default_content()

    filepath = os.getcwd() + '/cache/screenie.png'
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'xe-fileupload')))
    driver.find_element_by_id("xe-fileupload").send_keys(filepath)

    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(
        (By.XPATH, 'xefu-container-2')))  # Wait until file uploaded

    driver.find_element_by_xpath(
        '//*[@id="twnest_board_form"]/div[6]/input[2]').click()
    time.sleep(3)
    print('end')
