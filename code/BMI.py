#用于计算用户的BMI指数    BMI=体重/（身高**2）
user_weight=float(input("请输入您的体重   （kg）"))
user_height=float(input("请输入您的身高   （m）"))
BMI=user_weight/(user_height**2)
print("您的BMI指数为：",BMI)
#正常：18.5<BMI<=25
#偏瘦：BMI<=18.5
#偏胖：25<BMI<=30
#肥胖：BMI>30
if BMI<=18.5:
    print("您的身材偏瘦")
elif 18.5<BMI<=25:
    print("您的身材正常")
elif 25<BMI<=30:
    print("您的身材偏胖")
else:
    print("您的身材肥胖")