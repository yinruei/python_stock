'''
Louis今天要去香港旅遊，港幣匯率為exchange = 3.7，旅遊基金有5萬新台幣，
換成港幣，預計機票來回為2000港幣，飯店為4000港幣，吃喝玩樂為5000港幣，
回國後，louis換回台幣的錢還剩多少
'''
#1港幣 = 3.7台幣

travel_fund = 50000
exchange = 3.7883
airplane = 2000
hotel = 4000
eat_play = 5000

HKD = int(travel_fund / exchange)
print('台幣換港幣為 '+ str(HKD) + '元')
totalcost = airplane + hotel + eat_play
print('總花費 ' + str(totalcost) + '元')
residual_ntd = int((HKD - totalcost) * exchange)

print('台幣剩: ', residual_ntd, ' 元')