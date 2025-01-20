import math
while True:                                       #让这个程序一直运行下去
    a=int(input("请输入一个正整数："))
    if a<=0:
        continue
    else:
        b=int(math.sqrt(a))                     #使用开方，这样就不用一直迭代计算到输入的这个整数，可以减少计算量
        if a==1:
            print(a,"既不是素数，也不是因数。")
        elif a==2:
            print(a,"是一个素数。")
        elif a==3:
            print(a,"是一个素数。")               #先把1，2，3这三个特殊的数字讨论掉
        else:
            for i in range(2,b+1,1):
                if i==1:
                    continue
                elif a%i==0:
                    print(a,"是一个因数。")
                    break                       #找到一个因子停止for循环，避免重复计算
                elif i==b:                      #避免每次找不到因子就打印一次“是一个素数”，哪怕输入的数其实是因数
                    print(a,"是一个素数。")
