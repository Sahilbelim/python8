
# exercise :# https://www.ndtv.com/fuel-prices
# [{'city':'Adilabad','petrol_price':'111.83 ₹/L','diseal':"99.84 ₹/L"}]

from bs4 import BeautifulSoup
import requests

price=[]

data=requests.get("https://www.ndtv.com/fuel-prices").text
# print(data) # data is string 
#  to convert in to html doc 
doc_html=BeautifulSoup(data,'html.parser')

table=doc_html.find_all('table')[1]

# print(table.find_all('td')[0].string)
td=table.find_all('td')
city=td[0].string
# print(city)
# print(table.find_all('td')[1].span.string)
# print(td[1].span.string)
p_price=td[1].span.string
# print(table.find_all('td')[2].span.string)
# print(td[2].span.string)
d_price=td[2].span.string

for i in range(0,len(td),3):
    # print(i)
    city=td[i].string
    p_price=td[i+1].span.string
    d_price=td[i+2].span.string
    # {'city':city,'petrol_price':p_price,'diseal':p_price}
    # print(f" {city} = > | {p_price}  | {d_price} " )

# print(price)    
