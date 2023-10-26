import requests
from bs4 import BeautifulSoup
import csv


def scrap_book(url_page):
	product_add = []
	reponse = requests.get(url_page)
	page = reponse.content

	# transforme (parse) le HTML en objet BeautifulSoup
	soup = BeautifulSoup(page, "html.parser")

	# Récupération du product_page_url
	product_page_url = url_page
	product_add.append(product_page_url)

	# universal_ product_code (upc)
	product_code_temp = soup.find_all('td')
	product_code = product_code_temp[0].text
	product_add.append(product_code)

	# title
	product_title = soup.find('h1').text.replace('/',' ')
	product_add.append(product_title)

	# price_including_tax
	product_price_in_tax = product_code_temp[3].text
	product_add.append(product_price_in_tax)

	# price_excluding_tax
	product_price_ex_tax = product_code_temp[2].text
	product_add.append(product_price_ex_tax)

	# number_available
	product_number_available = product_code_temp[5].text
	product_add.append(product_number_available)

	# product_description
	if soup.find(id='product_description'):
		product_description = soup.find(id='product_description').find_next_sibling().text
		product_add.append(product_description)
	else:
		product_add.append("")

	# category
	product_category = soup.find('ul', class_='breadcrumb')
	product_temp = product_category.find_all('a')
	product_category_description = product_temp[2].text
	product_add.append(product_category_description)

	# review_rating
	review_rating = 0
	if soup.find('div', class_='col-sm-6 product_main').find('p', class_='star-rating One'):
		review_rating = 1
	elif soup.find('div', class_='col-sm-6 product_main').find('p', class_='star-rating Two'):
		review_rating = 2
	elif soup.find('div', class_='col-sm-6 product_main').find('p', class_='star-rating Three'):
		review_rating = 3
	elif soup.find('div', class_='col-sm-6 product_main').find('p', class_='star-rating Four'):
		review_rating = 4
	elif soup.find('div', class_='col-sm-6 product_main').find('p', class_='star-rating Five'):
		review_rating = 5

	product_add.append(review_rating)


	# image_url
	product_img_url = soup.find('img')
	product_img_url_temp = product_img_url['src'].replace('../../','http://books.toscrape.com/')
	product_add.append(product_img_url_temp)

	return product_add
