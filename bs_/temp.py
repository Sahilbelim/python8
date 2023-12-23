from bs4 import BeautifulSoup
import requests

url="https://vclock.com/time/"
html=requests.get(url).text

# print(html)

doc_html=BeautifulSoup(html,'html.parser')
print(doc_html)

name=BeautifulSoup(html,'')