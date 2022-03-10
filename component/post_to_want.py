from .default import *

def postImageToWT(driver, documentName, specialComment=""):
  delay = 3
  
  driver.set_window_size(1920, 1080)
  print('####access login link...WANT')
  driver.get('https://want.twicenest.com/FREE/login')
  print('login...')

###### Alert ######
  try:
    result = Alert(driver)
    result.dismiss()
  except:
    pass

  try:
    print('alarm')
    result = Alert(driver)
    result.accept()
  except:
    print('pass alarm')
    pass
####################
  driver.save_screenshot('./cache/0.png')
  try:
    print('try to find userid element by name')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'user_id')))
    driver.find_element_by_name('user_id').send_keys(wtConfig('id'))
  except:
    print('failed')
    print('try to find userid element by xpath')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="uid"]')))
    driver.find_element_by_xpath('//*[@id="uid"]').send_keys(wtConfig('id'))

  try:
    print('try to find password element by name')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    driver.find_element_by_name('password').send_keys(wtConfig('password'))
  except:
    print('failed')
    print('try to find password element by xpath')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="upw"]')))
    driver.find_element_by_xpath('//*[@id="upw"]').send_keys(wtConfig('password'))

  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fo_member_login"]/fieldset/div[2]/input')))
  driver.find_element_by_xpath('//*[@id="fo_member_login"]/fieldset/div[2]/input').click()
  
  print('access write link')
  driver.get('https://want.twicenest.com/FREE/write')
  driver.save_screenshot('./cache/1.png')
  time.sleep(3)
  try:
    result = Alert(driver)
    result.dismiss()
  except:
    pass
  driver.get('https://want.twicenest.com/FREE/write')
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
  #driver.switch_to.frame(iframe)
  driver.save_screenshot('./cache/2.png')
  print('start to type data...')

  title = '[08:00] 트와이스 뮤비 조회수'
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'category_srl')))
    select_fr = Select(driver.find_element_by_name('category_srl'))
    select_fr.select_by_index(4)
  except:
    pass

  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'title')))
  driver.find_element_by_name('title').clear()
  driver.find_element_by_name('title').send_keys(title)

  contentData = specialComment + "뮤비 조회수 봇은 TWICEWIKI에 의해 운영되고 관리됩니다.\n" + "https://ko.twice.wiki/w/"+ documentName + "\n\n"

  print('Input content data...')
  basic_page_body_xpath = '//*[@id="cke_1_contents"]/iframe'
  ckeditor_frame = driver.find_element_by_xpath(basic_page_body_xpath)
  driver.switch_to.frame(ckeditor_frame)
  editor_body = driver.find_element_by_xpath("//body")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
  editor_body.send_keys(contentData)
  driver.switch_to.default_content()

  filepath = os.getcwd() + '/cache/screenie.png'
  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'xe-fileupload')))
  driver.find_element_by_id("xe-fileupload").send_keys(filepath)
  
  WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, 'xefu-container-2'))) # Wait until file uploaded

  driver.find_element_by_xpath('//*[@id="contents"]/div/div/form/div[4]/div[3]/button[3]').click()
  time.sleep(3)
  print('end')
