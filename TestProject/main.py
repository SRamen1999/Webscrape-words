import re
import requests
from bs4 import BeautifulSoup
import pytesseract
import os
import cv2

#https://kissmanga.org/
#https://www.comicextra.com/
#'https://www.kissmanga.org/chapter/manga-ng952689/chapter-700.5'

site = input("Enter url: ")

# check if the folder is created already
if not (os.path.isdir('web_photos')):
    os.mkdir('web_photos')

response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')

#find all the img urls
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]
page_num = 0

#filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
for url in urls:
    '''filename = re.search(r'/([\w_-]+[.](jpg|gif|png| ))$', urls[i])
    if not filename:
         print("Regex didn't match with the url: {}".format(urls[i]))
         continue'''

    if 'http' in url:
        page_num += 1
        with open("web_photos//" + str(page_num) + '.png', 'wb+')as f:
            response = requests.get(url)
            f.write(response.content)


#prints the words from the pictures
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.chdir('web_photos')
for num in range(2,page_num):
    print("Page " + str(num))
    img = cv2.imread(str(num)+'.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(img)
    print(text)
    imS = cv2.resize(img, (700, 700))
    cv2.imshow('Result', imS)
    cv2.waitKey(0)

