# CodeWithHarry

# Info you want to scrape a website:
# 1. Use the API
# 2. HTML WEB Scraping using tools like bs4

# Step Zero : all requirements
# pip install requests 
# pip install bs4
# pip install html5lib

# Installing Libraries
import requests
from bs4 import BeautifulSoup
import html5lib

# URL To Be Scraped
# url = "https://gogo-stream.com/videos/boruto-naruto-next-generations-episode-113"
url = "https://codewithharry.com/"

# Step 1: Get HTML
rContent = requests.get(url)
htmlContent = rContent.content
# print(htmlContent)

# Step 2: Parse HTML
soup = BeautifulSoup(htmlContent, "html.parser")
# print(soup.prettify)

# Get the title of the HTML Page
title = soup.title

# Get all paragraphs from the HTML Page
print("All Paragraph Tags")
paras = soup.find_all('p')
print(paras, "\n")

# Get all anchor tags from the HTML Page
print('All Anchor Tags')
ancr = soup.find_all('a')
print(ancr, "\n")

all_links = set()

# Finding Classes of any elements in the HTML Page
# print(soup.find('p')['class'])

# Getting First Element
print(soup.find('p'))

# Getting elements of Specific Class
print(soup.find_all("p", class_="brandLogo"))

# Getting the text using Tags/Soup
print(soup.find('p').get_text())

# Getting all TEXT using Tags/Soup
print(soup.get_text())

# Getting all the links on Page
for link in ancr:
    if(link.get('href') != '#'):
        link1 = "https://codewithharry.com" + link.get('href')
        all_links.add(link1)
        print(link1)

navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent.content)
# exit()

# 4. Comment

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
exit()

###
# Step 3: HTML Tree Traversal
#
# Commonly used types of objects:
# # 1. Tag - print(title)
# # 2. NavigableString - print(type(title))
# # 3. BeautifulSoup - print(type(title.string)) 
#
###