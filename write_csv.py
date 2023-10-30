import csv
import requests
def write_csv_img(nameCategory,infoBook):
    path_csv = "BookToScrap/" + nameCategory + "/"
    header = ['Product page url', 'Universal product code (upc)', 'Title', 'Price including tax',
              'Price excluding tax', 'Number available', 'Product description', 'Category', 'Review_rating',
              'Image url']
    with open(path_csv + nameCategory + ".csv", 'w') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=';')
            writer.writerow(header)
            for category, bookInfo in infoBook.items():
                writer.writerow(bookInfo)
                response = requests.get(bookInfo[9])
                image = open(path_csv + bookInfo[2] + '.jpg', "wb")
                image.write(response.content)
                image.close()