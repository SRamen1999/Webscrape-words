import cv2
import pytesseract
from bs4 import BeautifulSoup
import requests as rq
import urllib.request


#image scraping

response = input("Enter url: ")
source_code = rq.get(response)
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
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_src, str(number))
    number += 1

#prints the words from the pictures

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for num in range(len(images)):
    print("Page " + str(num))
    img = cv2.imread(str(num))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    print(text)
    cv2.imshow('Result',img)
    cv2.waitKey(0)

