from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from pyfiglet import figlet_format
import time

# demander le site où chercher (Amazon ne marche pas pour le moment)
suite = False
while suite == False:
    site = input(str("Veuillez choisir Amazon (non fonctionnel pour le moment) ou Aliexpress : \n"))
    if site.lower() == "amazon":
        print(figlet_format("AMAZON", font="big"))
        suite = True
    elif site.lower() == "aliexpress":
        print(figlet_format("AliExpress", font="big"))
        suite = True
    else:
        print("erreur de saisie !")


# demander l'élement à chercher et étudier
search_text = input(str("Veuillez entrer le mot recherché : \n"))

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/110.0.5481.178 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# driver Chrome
PATH = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

# liste contenant les liens utilent
href_clean = []

#Fonction mère qui permet l'extraction des URL
def Aliexpress_scraping(x):
    # site a scraper
    driver.get("https://fr.aliexpress.com/")

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    # acceder a la barre de recherche
    search = driver.find_element(By.NAME, "SearchText")

    # chercher dans la barre de recherche
    search.send_keys(x)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    # scroll down
    driver.execute_script("window.scrollBy(0, 2000);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(2000, 4000);")
    time.sleep(1)

    div_element = driver.find_element(By.CLASS_NAME, "list--gallery--34TropR")
    link_elements = div_element.find_elements(By.TAG_NAME, 'a')

    # stock tous les liens dans une liste et evite les None
    href_list = []
    for link_element in link_elements:
        href = link_element.get_attribute('href')
        if href not in [None, "None"]:
            href_list.append(href)

    # affiche que les liens utiles car entre chaque deux liens on trouve un lien de publicité
    j = 1
    for i in range(len(href_list)):
        if i % 2 == 0:
            print("Lien num", j, " = ", href_list[i], "\n")
            href_clean.append(href_list[i])
            j += 1

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    print("on a trouvé", len(href_list), "liens dans cette page, dont",
          len(href_clean), "sont utiles")


if site.lower() == "amazon":
    pass
    #    Amazon_scraping(x) a definire apres
elif site.lower() == "aliexpress":
    Aliexpress_scraping(search_text)



# # Possibilité d'ouvrir le premier lien extrait dans un nouvel onglet

# # Execute JavaScript to open a new tab and navigate to a new URL
# driver.execute_script('window.open("https://www.google.com","_blank");')
# # Basculer vers le nouvel onglet
# driver.switch_to.window(driver.window_handles[1])
# # Simulate a keyboard shortcut to open a new tab
# driver.get(href_clean[0])


# fermer le navigateur
driver.quit()


# Extraction des cles de l'URL
product_keys = []

for url in href_clean:
        #La clé se trouve dans un endroit bien précis de l'URL
        product_key = url.split("/")[-1].split(".")[0]
        product_keys.append(product_key)

# Définit le nom du fichier CSV
file_name = 'product_keys.csv'

# Ouvre le fichier CSV en mode écriture et configure le writer
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    # Écrit les données dans le fichier CSV
    writer.writerow(['Product Keys'])
    for item in product_keys:
        writer.writerow([item])
    print("fichier des 'product_keys' crée")