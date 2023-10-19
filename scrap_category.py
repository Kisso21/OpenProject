import requests
from bs4 import BeautifulSoup
import csv
import re
from scrap_book import scrap_book


# Récupération des noms catégories et des urls de chaques catégories dans un Dictionnaire{key = CategoryName, Value = urlCategory}
def scrap_name_and_url_category():
    reponse = requests.get("http://books.toscrape.com/index.html")
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    site_category_temp = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')
    categoryKeyUrl = {}
    for x in range(len(site_category_temp)):
        categoryUrl = site_category_temp[x].find('a').get('href').replace("catalogue/","http://books.toscrape.com/catalogue/")
        nameCategory = site_category_temp[x].find('a').text.replace(" ","").replace("\n", "")
        categoryKeyUrl[nameCategory] = categoryUrl
    return categoryKeyUrl

# Récupération de tous les urls des differents livre sur la page
def scrap_all_urlBook_on_page(url_page):
    reponse = requests.get(url_page)
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")

    book_page_url_liste = []
    livre_url_temp = soup.find_all('h3')
    for link in livre_url_temp:
        a = link.find('a')
        links = a['href']
        book_page_url_liste.append(links.replace('../../../','http://books.toscrape.com/catalogue/'))

    return book_page_url_liste

# Récupération de tous les urls des differents livre de la catégorie
def scrap_all_urlBooks_in_categorie(url_category):

    reponse = requests.get(url_category)
    urlCategory = url_category.replace('index.html', '')
    page = reponse.content
    soup = BeautifulSoup(page, "html.parser")
    book_liste_categorie = scrap_all_urlBook_on_page(url_category)

    while soup.find('li', class_='next'):
        qPage = soup.find('li', class_='next')
        for link in qPage.find_all('a'):
            pageNext = link.get('href')
            nextUrl = urlCategory + pageNext
        pageScrapped = scrap_all_urlBook_on_page(nextUrl)
        book_liste_categorie += pageScrapped
        reponseNextUrl = requests.get(nextUrl)
        pageNextUrl = reponseNextUrl.content
        soup = BeautifulSoup(pageNextUrl, "html.parser")

    return book_liste_categorie





