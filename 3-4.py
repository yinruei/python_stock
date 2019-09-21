import pandas as pd
stock = '2002'

#要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
getdata = pd.read_html(url, encoding="big5", header=0)
print('getdata', getdata)