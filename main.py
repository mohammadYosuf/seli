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

#find location inputs and button
username_location = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/form/div[1]/input")
password_location=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[1]/form/div[2]/input")
submit_button_location=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[1]/form/button")

#send data
username_location.send_keys(username)
password_location.send_keys(password)
submit_button_location.click()
time.sleep(30)
