from bs4 import BeautifulSoup
import requests

qrl='https://www.cricbuzz.com/'
html=requests.get(qrl).text
# print(html)
html_doc=BeautifulSoup(html,'html.parser')
run=html_doc.find_all('div',{'class':'cb-col-50 cb-ovr-flo'})
print(run[0].string)
# <div class="cb-col-50 cb-ovr-flo" style="display:inline-block; width:100%">270-6 (48)</div>