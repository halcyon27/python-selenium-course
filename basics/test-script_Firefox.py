import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of geckodriver.exe
ff_driver_path = os.path.join("C:", "drivers", "Selenium")

# create a new Firefox session
driver = webdriver.Firefox(ff_driver_path + 'geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to a url
driver.get('http://google.com')