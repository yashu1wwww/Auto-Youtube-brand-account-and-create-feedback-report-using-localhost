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

driver.get("https://www.youtube.com/watch?v=WNpio23EJhI") #replace video which you want to report it....

time.sleep(5)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#dot click

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[3]/tp-yt-paper-item').click()#report

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[4]/div[2]/div/yt-formatted-string').click()#1/11-you must select option 

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-dropdown-menu[4]/tp-yt-paper-menu-button/div/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]').click()#auto choose

time.sleep(2)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-dropdown-menu[4]/tp-yt-paper-menu-button/tp-yt-iron-dropdown/div/div/tp-yt-paper-listbox/tp-yt-paper-item[2]').click() #select first option

time.sleep(2)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/div/yt-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#next button

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-report-details-form-renderer/yt-report-details-form-content/div/div/tp-yt-paper-input-container/div[2]/div/tp-yt-iron-autogrow-textarea/div[2]/textarea').send_keys('in these video the heroine dont have respect to industry')

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-report-details-form-renderer/div[2]/div[2]/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#report

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[3]/yt-fancy-dismissible-dialog-renderer/div/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#close

time.sleep(30)


