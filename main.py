#install selenium with pip install selenium
#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#in this state create driver for google chrome and open login page
driver = webdriver.Chrome()
driver.get("https://panel.iranicard.ir/login")
time.sleep(70)

#add data of user
username="09913663202"
password="09913663202"

