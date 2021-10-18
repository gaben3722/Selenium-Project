import selenium
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.reddit.com/")


search = driver.find_element_by_name("")

driver.quit()