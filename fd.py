from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver= webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://www.youtube.com/")

driver.find_element_by_id("avatar-btn").click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[5]/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item').click()#send feedback
time.sleep(3)
driver.find_element_by_css_selector('body > div:nth-child(3) > div > div > uf-describe-page > form > div:nth-child(2) > textarea').send_keys("hey youtube") #change to your feedback text to yours needed
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/sc-shared-material-popup/div/div/div/uv-feedback-feedback-manager/div/div/div[1]/uv-feedback-form/div/div[3]/div[3]/sc-shared-material-checkbox/label/div').click()#tick mark
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/sc-shared-material-popup/div/div/div/uv-feedback-feedback-manager/div/div/div[1]/uv-feedback-form/div/div[4]/div/sc-shared-material-button/div/button').click()#send button
time.sleep(30)