import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name("q").get_attribute('href')

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists = driver.find_elements_by_class_name("r")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i = 1
for listitem in lists:
    print(i, "-", listitem.find_element_by_css_selector('a').get_attribute('href'))
    i = i + 1
    if (i > 10):
        break

# close the browser window
driver.quit()