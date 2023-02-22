from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#driver Chrome
PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

#site a scraper
driver.get("https://fr.aliexpress.com/")
#recup titre du site
print(driver.title)

#acceder a la barre de recherche
search = driver.find_element(By.NAME, "SearchText")

#chercher dans la barre de recherche
search.send_keys("phone")
search.send_keys(Keys.RETURN)

try:
    elements = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list--gallery--34TropR"))
    )

    hrefs = elements.find_element("href")
    print(elements.text)

finally:
    driver.quit()



# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Set the app ID and number of reviews to scrape
# app_id = 'com.alibaba.aliexpresshd'
# review_count = 100
#
# # Launch the browser and navigate to the app's review page
# driver = webdriver.Chrome()
# driver.get(f'https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true')
#
# # Scroll to the bottom of the page to load all the reviews
# while True:
#     reviews = driver.find_elements(By.XPATH, '//div[@class="jgIq1"]')
#     if len(reviews) >= review_count:
#         break
#     actions = ActionChains(driver)
#     actions.move_to_element(reviews[-1])
#     actions.perform()
#
# # Extract the reviews
# for review in reviews[:review_count]:
#     comment = review.find_element(By.XPATH, './/div[@class="h3YV2d"]').text
#     print('Comment:', comment)
#
# # Close the browser
# driver.quit()
#
# #Qeuel est le segment commercial qui est considéré comme une niche pour d'autre catégorie démographique ou age ou sexe ?