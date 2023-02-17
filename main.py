import requests as re
from bs4 import BeautifulSoup

site = re.get('https://www.amazon.fr/NEWC-iPhone-Transparente-Silicone-Protection/dp/B09F86YGL3/ref=zg-bs_14055231_sccl_1/257-7964114-0310010?pd_rd_w=bekng&content-id=amzn1.sym.68f09fbb-e7d4-45e1-8e73-e92a01b6e860&pf_rd_p=68f09fbb-e7d4-45e1-8e73-e92a01b6e860&pf_rd_r=HAR8B656JP7XTCCQ0PY8&pd_rd_wg=iIYtf&pd_rd_r=7dd255a6-75ba-444b-a7cb-6ce5bc8e46bf&pd_rd_i=B09F86YGL3&th=1')
soup = BeautifulSoup(site.content, "html.parser")

# Trouver tous les div
divs = soup.find_all('div', class_='a-section review-views')

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
