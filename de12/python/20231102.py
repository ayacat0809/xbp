from bs4 import BeautifulSoup
import requests

url = r"file:///C:/Users/takep/mygit/xbp/de12/index.html"
response = requests.get(url)

with open(url , mode="rt" , encoding="utf-8") as f:
    soup = BeautifulSoup(f.read() , "html.parser")

# どんな内容のタグを追加するのか
nt = soup.new_tag('a', href=r'https://amzn.asia/d/1hdxk8S')
nt.string = 'Python自動処理の教科書'

# 追加
soup.find(url).append(soup.new_tag)

# nt = soup.new_tag("li" , href='index.html')
# nt.string = 'aiueo'

# soup.find('ul').append(nt)

# print(soup)