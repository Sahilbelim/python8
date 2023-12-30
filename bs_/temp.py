from bs4 import BeautifulSoup
import requests

url="https://vclock.com/time/"
html=requests.get(url).text

# print(html)

doc_html=BeautifulSoup(html,'html.parser')
print(doc_html)

name=BeautifulSoup(html,'')
# def Check_Prime_No(num):
#     for i in range(2,num+1):
#         if i % 2 == 0:
#             return False
#             # print("false")
#     return True
#             # print("true")

# def Twin_Prime_No(num):
#     for first_number in range(2,num+1):
#         secoend_num = first_number + 2

#         if( Check_Prime_No(first_number) and Check_Prime_No(secoend_num)):
#              print("{0} and {1}" .format(first_number,secoend_num))

# print("Twin Prime: ")
# Twin_Prime_No(100)