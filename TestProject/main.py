import cv2
import pytesseract
from bs4 import BeautifulSoup
import requests as rq
import urllib.request


#image scraping
url = "https://narutoshippuden-manga.com/manga/naruto-chapter-670/"
source_code = rq.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text, 'html.parser')
print(soup.title)

images = soup.find_all("img")
print(images)

number = 0

#downloads the images
for image in images:
    image_src = image["src"]
    print(image_src)

    urllib.request.urlretrieve(image_src, str(number))
    number += 1

#prints the words from the pictures

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for num in range(len(image_src)-1):
    print("Page " + str(num))
    img = cv2.imread(str(num))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    print(text)
    cv2.imshow('Result',img)
    cv2.waitKey(1)

