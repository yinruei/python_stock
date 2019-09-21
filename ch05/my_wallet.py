'''
sean每個月月薪3萬元，每個月必須支付勞健保加上稅金共11%，房租水電為1萬5，吃喝玩樂開銷為5000，
其餘薪水定存銀行，請問sean一年可存多少錢
'''

salary = int(input('薪水: '))
tax = float(input('勞保和稅金: '))
rent_water_ele = int(input('房出水電: '))
eat_play = int(input('吃喝玩樂: '))


real_salary = salary - (salary * tax) 
save_per_month = real_salary - rent_water_ele - eat_play

save_per_year = save_per_month * 12

print('每個月可以存 ' + str(save_per_month) +'元')
print('每年可以存 ' + str(save_per_year) +'元')