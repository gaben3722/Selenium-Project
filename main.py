import selenium
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (86)\chromedriver.exe"
wd = webdriver.Chrome(PATH)

def get_images_from_google(wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = "https://www.google.com/search?q=dogs&sxsrf=AOaemvIqf6FpU0Jq4_1uYXUxeEKp1YLggQ:1635733108946&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-qJ_XjPbzAhXylWoFHXoBDygQ_AUoAXoECAEQAw&biw=1536&bih=750&dpr=1.25"
	wd.get(url)

	image_urls = set()
	skips = 0

	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls

driver.quit()