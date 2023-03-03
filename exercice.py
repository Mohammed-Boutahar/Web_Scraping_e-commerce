import requests
from bs4 import BeautifulSoup

url = "https://fr.aliexpress.com/item/1005003500631524.html?algo_pvid=b32a1999-ad5d-4129-a461-b5dfad04"

# Récupération du contenu HTML de la page
response = requests.get(url)
html_content = response.text

# Extraction des commentaires des utilisateurs
soup = BeautifulSoup(html_content, "html.parser")
reviews = soup.find_all("div", {"class": "feedback-item"})

# Affichage des commentaires des utilisateurs
for review in reviews:
    rating = review.find("div", {"class": "star-view"}).get("title")
    comment = review.find("div", {"class": "feedback-text"}).text.strip()
    print("Note: {}\nCommentaire: {}\n".format(rating, comment))
