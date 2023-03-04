from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import execjs


from pyfiglet import figlet_format

import requests
from bs4 import BeautifulSoup

import time

#demander le site où chercher
suite = False
while suite == False:
    site = input(str("Veuillez choisir Amazon ou Aliexpress : \n"))
    if site.lower() == "amazon":
        print(figlet_format("AMAZON", font = "big" ))
        suite = True
    elif site.lower() == "aliexpress":
        print(figlet_format("AliExpress", font = "big" ))
        suite = True
    else:
        print("erreur de saisie !")
    #print("ana")

#demander l'élement à chercher et étudier
search_text = input(str("Veuillez entrer le mot recherché : \n"))

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/110.0.5481.178 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data 
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

def html_code(url):
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # display html code
    return (soup)

 #driver Chrome
PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

#liste contenant les liens utilent
href_clean=[]
def Aliexpress_scraping(x):
    #site a scraper
    driver.get("https://fr.aliexpress.com/")

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


    #acceder a la barre de recherche
    search = driver.find_element(By.NAME, "SearchText")

    #chercher dans la barre de recherche
    search.send_keys(x)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    #scroll down to get more articles
    driver.execute_script("window.scrollBy(0, 2000);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(2000, 4000);")
    time.sleep(1)

    div_element = driver.find_element(By.CLASS_NAME, "list--gallery--34TropR" )
    link_elements = div_element.find_elements(By.TAG_NAME, 'a')

    #stock tous les liens dans une liste et evite les None
    href_list = []
    for link_element in link_elements:
        href = link_element.get_attribute('href')
        if href not in [None, "None"]:
            href_list.append(href)


    #affiche que les liens utiles 
    j=1
    for i in range(len(href_list)):
        if i % 2 == 0:
            print("Lien num", j, " = ", href_list[i], "\n")
            href_clean.append(href_list[i])
            j+=1

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    print("on a trouvé", len(href_list), "liens dans cette page, dont", len(href_clean), "sont utiles")




if site.lower() == "amazon":
    pass
    #    Amazon_scraping(x) a definire apres
elif site.lower() == "aliexpress":
    Aliexpress_scraping(search_text)


# Execute JavaScript to open a new tab and navigate to a new URL
driver.execute_script('window.open("https://www.google.com","_blank");')
# Basculer vers le nouvel onglet
driver.switch_to.window(driver.window_handles[1])
# Simulate a keyboard shortcut to open a new tab
driver.get(href_clean[0])

#scroll down to get more articles
driver.execute_script("window.scrollBy(0, 4000);")
time.sleep(1)
driver.execute_script("window.scrollBy(4000, 8000);")
time.sleep(1)
driver.execute_script("window.scrollBy(8000, 12000);")
time.sleep(1)


customer_elements = driver.find_element(By.NAME, "feedback" )
print(customer_elements)

review_elements = customer_elements.find_elements(By.CLASS_NAME, "f-content")
print(review_elements)

reviews=[]
for review in review_elements:
    rating = review.find_element("span", {"class": "star-view"}).find_element("span").get_attribute('style')
    comment = review.find_element("dl", {"class": "buyer-feedback"}).text.strip()
    print("Note: {}\nCommentaire: {}\n".format(rating, comment))
    reviews.append(comment)


time.sleep(4)

#fermer le navigateur
driver.quit()






#didnt work for me
#reviews=[]
#for i in soup.findAll("dt",{'class':"buyer-feedback"}):   
 #reviews.append(i.text)

 #rev={'reviews':reviews}
 #review_data=pd.DataFrame.from_dict(rev)
 #pd.set_option('max_colwidth',800)
 #review_data.head(5)


# # Récupération du contenu HTML de la page
# soup=html_code(href_clean[0])

# reviews = soup.find_all("div", {"class": "feedback-item"})

# # Affichage des commentaires des utilisateurs
# for review in reviews:
#     rating = review.find("div", {"class": "star-view"}).get("title")
#     comment = review.find("div", {"class": "feedback-text"}).text.strip()
#     print("Note: {}\nCommentaire: {}\n".format(rating, comment))






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