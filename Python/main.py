import requests as re
from bs4 import BeautifulSoup

site = re.get('https://play.google.com/store/apps/details?id=com.alibaba.aliexpresshd')
soup = BeautifulSoup(site.content, "html.parser")

# Trouver tous les div
divs = soup.find_all('div', {'class': 'RHo1pe'})

print(len(divs))

for i in divs:
    print(i)
    print("-----------------------------------------------")

# Parcourir les avis et extraire ceux des utilisateurs qui ont acheté le produit
# for review in reviews:
#     user = review.find("div", class_="feedback-item clearfix")
#     # L'utilisateur a acheté le produit, extraire l'avis
#     rating = review.find("div", class_="rating").text
#     comment = review.find("div", class_="comment").text
#     print("Rating: " + rating)
#     print("Comment: " + comment)

#print(soup)
#print(reviews)
