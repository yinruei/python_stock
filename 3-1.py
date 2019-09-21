import requests
from bs4 import BeautifulSoup
import lxml

stock = '2002'
#要抓取的網址
# https://tw.stock.yahoo.com/q/q?s=2002
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
#請求網站
list_req = requests.get(url)
print('list_req', list_req)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "lxml")
print('soup', soup)
#找到b這個標籤
get_stock = soup.find('b').text#只抓到第一個<b>
print('get_stock', get_stock)

get_stock = soup.findAll('b')[1].text#抓到收盤價格
print('get_stock', get_stock)