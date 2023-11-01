import requests
from bs4 import BeautifulSoup

url = "https://ayacat0809.github.io/xbp/de12/index.html"
res = requests.get(url)

soup = BeautifulSoup(res.text , "html.parser")
elems = soup.select('body > ul ')

print(soup.ul.get_text)