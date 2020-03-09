"""金字塔是世界七大奇景之一，請利用for迴圈寫出如下圖所示的4層金字塔圖形。
>>>
       *
    *     *
  *    *    *
*    *    *    *
>>>
"""
for i in range(4):# 總共有4層
    for j in range(4 - i - 1):#在印第一個＊之前先印空白
        # print(j)
        print("", end=" ")
    for k in range(i+1):# 印出每一行＊的數量
        print("* ", end="")
    print("\t")# 換行