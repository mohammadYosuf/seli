#install selenium with pip install selenium
#import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#in this state create driver for google chrome and open login page
driver = webdriver.Chrome()
driver.get("https://panel.iranicard.ir/login")
