from default import *


def post_to_wiki(driver: webdriver, EDITDATA: str, region: str, documentName: str):
    editURL = 'https://' + region + '.twice.wiki/edit/' + documentName
    loginURL = 'https://' + region + '.twice.wiki/login'
    delay = 3

    # login
    print('access loginURL...')
    driver.get(loginURL)
    driver.implicitly_wait(delay)
    driver.find_element_by_name('id').send_keys(wiki_config['id'])
    driver.find_element_by_name('pw').send_keys(wiki_config['password'])
    driver.find_element_by_xpath('//*[@id="content-card"]/form/button').click()
    print('success login')

    # editing
    driver.get(editURL)
    driver.implicitly_wait(delay)
    driver.find_element_by_id('content').clear()
    print('start to type data text....')
    driver.find_element_by_id('content').send_keys(EDITDATA)
    print('end to type data text.')
    driver.find_element_by_name('copyright_agreement').click()
    driver.find_element_by_id('save').click()
    time.sleep(3)
    print('saved.')
