# import turtle    #导入海龟绘图模块
# turtle.showturtle()    #显示箭头
# turtle.write("the first try")    #写下文字
# turtle.forward(100)         #前进100个像素
# turtle.left(90)     #向左转90度
# turtle.color("red")       #把画笔颜色改为红色，注意颜色需要写成字符串的形式
# turtle.goto(0,0)        #把箭头移动到指定坐标位置
# turtle.penup()          #把笔抬起来，这样移动时就不会留下路径
# turtle.goto(0,100)
# turtle.pendown()            #把笔放下，不然画不了线
# turtle.pensize(6)           #调整画笔粗细，和turtle.width()效果一样
# turtle.goto(-100,10)
# turtle.circle(100)         #画圆（半径，
# turtle.done()      #程序结束后保留绘图结果窗口，应置于最后
import turtle
# #画个五环
# turtle.showturtle()
# turtle.width(10)
# turtle.penup()
# turtle.goto(-125,50)
# turtle.pendown()
# turtle.color('blue')
# turtle.circle(70)
#
# turtle.penup()
# turtle.goto(0,50)
# turtle.pendown()
# turtle.color('black')
# turtle.circle(70)
#
# turtle.penup()
# turtle.goto(125,50)
# turtle.pendown()
# turtle.color('red')
# turtle.circle(70)
#
# turtle.penup()
# turtle.goto(-60,-50)
# turtle.pendown()
# turtle.color('yellow')
# turtle.circle(70)
#
# turtle.penup()
# turtle.goto(60,-50)
# turtle.pendown()
# turtle.color('green')
# turtle.circle(70)
#
# turtle.done()

turtle.speed(20)
j=50
turtle.showturtle()
for i in range(1,1000,1):
    if i%2==0:
        turtle.color('blue')
    elif i%3==0:
        turtle.color('red')
    elif i%5==0:
        turtle.color('black')
    elif i%7==0:
        turtle.color('dark green')
    else:
        turtle.color('purple')
    turtle.forward(i)
    turtle.left(j)
turtle.done()
