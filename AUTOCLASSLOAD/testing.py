import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/aryan/AppData/Local/Google/Chrome/User Data/Default") # change to profile path


driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://meet.google.com/ysy-pkoo-ijp?pli=1&authuser=2');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('e19J0b')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()