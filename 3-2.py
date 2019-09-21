import requests
from bs4 import BeautifulSoup
import lxml

stock = '2002'
#要抓取的網址
# https://tw.stock.yahoo.com/q/q?s=2002
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "lxml")
#找到table這個標籤
# print(soup.find('table'))#只找到一個
# print(soup.find_all('table'))#找到網頁內的所有的table
print(soup.find_all('table', {'border':'2'}))#特別指定
