from .default import *

def captureDocument(driver, region, documentName):
  file = 'screenie.png'
  path = './cache/' + file

  print('try to find screenshot file...')
  if os.path.isfile(path):
    print('found screenshot file.')
    os.remove(path)
    print('delete screenshot file.')
  else:
    print('cannot find screenshot file.')
  
  documentURL = 'https://' + region + '.twice.wiki/w/' + documentName
  delay = 3
    
  driver.set_window_size(500, 4000)
  #access
  print('access document url...')
  driver.get(documentURL)
  print('try to save screenshot.')
  driver.save_screenshot(path)
  print('screenshot saved.')
