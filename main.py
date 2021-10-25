import selenium
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.reddit.com/")


search = driver.find_element_by_name("wallstreetbets")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()