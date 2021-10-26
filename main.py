import selenium
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.reddit.com/")


search = driver.find_element_by_name("wallstreetbets")
search.send_keys("test")
search.send_keys(Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except:
    driver.quit()

print(main.text)

driver.quit()