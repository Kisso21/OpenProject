from scrap_category import *
from scrap_book import *
import os

if __name__ == '__main__':
    #Recupération de toutes les catégories et leur URL respective
    nameUrl_category = scrap_name_and_url_category()

    # Création du dossier pour acceuillir toute la data
    if not os.path.exists("BookToScrap"):
        os.makedirs("BookToScrap")

    for nameCategory, urlCategory in nameUrl_category.items():
        if not os.path.exists("BookToScrap/" + nameCategory):
            os.makedirs("BookToScrap/" + nameCategory)
        allBook_in_category = scrap_all_urlBooks_in_categorie(urlCategory)

        # Création des différents CSV par catégories ainsi que la récupération des images de chaques livres
        header = ['Product page url', 'Universal product code (upc)', 'Title', 'Price including tax',
                   'Price excluding tax', 'Number available', 'Product description', 'Category', 'Review_rating',
                   'Image url']
        path_csv = os.path.join("BookToScrap/" + nameCategory, nameCategory + '.csv')
        with open(path_csv, 'w') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=';')
            writer.writerow(header)
            for book in allBook_in_category:
                bookTemp = scrap_book(book)
                writer.writerow(bookTemp)
                # Récupération de l'image du livre
                chemin_fichier = os.path.join("BookToScrap/" + nameCategory, bookTemp[2] + '.jpg')
                image = open(chemin_fichier, "wb")
                response = requests.get(bookTemp[9])
                image.write(response.content)
                image.close()