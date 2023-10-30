from scrap_category import *
import os
from write_csv import *

if __name__ == '__main__':
    #allBook = {Catégorie : {Book1 : [infobook], Book2 : []}, Catégorie2 : {Book1 : [], Book2 : []} }
    allBooksInBookToScrap = all_book_sort_category()

    if not os.path.exists("BookToScrap"):
        os.makedirs("BookToScrap")
    for nameCategory, sousCategory in allBooksInBookToScrap.items():
        if not os.path.exists("BookToScrap/" + nameCategory):
            os.makedirs("BookToScrap/" + nameCategory)
            write_csv_img(nameCategory,sousCategory)