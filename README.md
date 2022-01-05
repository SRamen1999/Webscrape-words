# Webscrape words
 This program webscraps pictures off a website and prints out the words from the picture

# Websides you can use the program on 
https://kissmanga.org/ \
https://www.comicextra.com/

# libraies needed
import requests\
from bs4 import BeautifulSoup\
import pytesseract\
import os\
import cv2

#How the program works
The program will first ask you to enter the url of of a manga or comic book from one of these websites.
Then it will then create a folder called web_photos and download all the photos from the url you put in.
Lastly it will display all the photos it downloaded and will print out the words from the pictures using pytesseract.
