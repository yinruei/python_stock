import requests
from bs4 import BeautifulSoup
import lxml
import json
import datetime

stock='2002'
#今天的時間
today = datetime.date.today()
#請求的網站
url = 'http://invest.wessiorfinance.com/Stock_api/Notation_cal?Stock='+ stock + '&Odate=' + str(today) + '&Period=3.5&is_log=0&is_adjclose=0'

#開始請求
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, 'lxml')
#將爬下來的文字轉成json
getJson = json.loads(soup.text)
print('getJson', getJson)