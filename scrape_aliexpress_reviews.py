from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

x = input(str("Veuillez entrer le mot recherché : \n"))

#driver Chrome
PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)


#site a scraper
driver.get("https://fr.aliexpress.com/")
#recup titre du site
print(driver.title)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


#acceder a la barre de recherche
search = driver.find_element(By.NAME, "SearchText")

#chercher dans la barre de recherche
search.send_keys(x)
search.send_keys(Keys.RETURN)

time.sleep(2)
#scroll down to get more articles
driver.execute_script("window.scrollBy(0, 2000);")

time.sleep(1)
div_element = driver.find_element(By.CLASS_NAME, "list--gallery--34TropR" )
link_elements = div_element.find_elements(By.TAG_NAME, 'a')

#stock tous les liens dans une liste et evite les None
href_list = []
for link_element in link_elements:
    href = link_element.get_attribute('href')
    if href not in [None, "None"]:
        href_list.append(href)

#taille de la liste
print(len(href_list))

# n = len(href_list)
# for j in range(n):
#     # Check if the index is odd
#     if j % 2 == 1 and j <= len(href_list)-1:
#         # Delete the element at the current index
#         href_list.pop(j)


#affiche que les liens utiles 
j=0
for i in range(len(href_list)):
    if i % 2 == 0:
        print("Lien num", j+1, " = ", href_list[i], "\n")
        j+=1

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

print("on a toruvé", len(href_list), "liens dans cette page, dont", j, "sont utiles")

# try:
#     elements = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "list--gallery--34TropR"))
#     )

#     hrefs = elements.find_element("href")
#     print(driver.page_source)

# finally:
#     driver.quit()



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