from bs4 import BeautifulSoup

with open('index.html' , mode=nt , encoding='uft-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

nt = soup.new_tag("li" , href='index.html')
nt.string = 'aiueo'

soup.find('ul').append(nt)

print(soup)