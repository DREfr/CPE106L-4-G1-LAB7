import requests
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page1.html'

response = requests.get(url)

if response.status_code == 200:
    print("Page fetched")
else:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

# Find the first <h1> tag (Title)
title = soup.find('h1')
if title:
    print(f"Title: {title.text}")
else:
    print("Title not found.")

# Find all <div> tags (texts)
texts = soup.find_all('div')
if texts:
    for texts in texts:
        print(f"Texts: {texts.text}")
else:
    print("No texts found!")

#Using find_all() for all links <a>
links = soup.find_all('a')
if links:
    print("Links on the page:")
    for link in links:
        href = link.get('href')  # Get the href attribute (URL of the link)
        print(href)
else:
    print("No links found")
