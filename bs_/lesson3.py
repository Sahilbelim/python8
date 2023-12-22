from bs4 import BeautifulSoup
import requests

url="https://vclock.com/time/"
html=requests.get(url).text

# print(html)

doc_html=BeautifulSoup(html,'html.parser')
time=doc_html.find_all('span',{'id':'lbl-time'})
print(time[0].string)

# exercise :# https://www.ndtv.com/fuel-prices
# [{'city':'Adilabad','petrol_price':'111.83 ₹/L','diseal':"99.84 ₹/L"}]