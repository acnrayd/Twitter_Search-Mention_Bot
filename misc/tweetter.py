# This is part of the main script which sends tweets on behalf of your account usign Selenium Py. Not needed for prod.
# Bu dosya yalnızca sizin hesabınız adına tweet atan scripti içermektedir.

from selenium import webdriver
import datetime
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains


user = "@Hurriyet" + "Sayın Kullanıcı"

mesaj = user + "   merhaba, bu bir test mesajıdır: www.google.com"

driver = webdriver.Chrome(executable_path='/Users/caner/PycharmProjects/Test1/chromedriver')
driver.get('https://twitter.com/login');
time.sleep(1)
search_box = driver.find_element_by_name('session[username_or_email]')
search_box.send_keys('TWITTER_USERNAME')
search_box = driver.find_element_by_name('session[password]')
search_box.send_keys('TWITTER_PASSWORD')
search_box.submit()

driver.get('https://twitter.com/compose/tweet')


autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
autotw1.click()

element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(element).send_keys(mesaj).perform()

sendTw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]/div/span/span')))
sendTw.click()
time.sleep(2)
driver.quit()


