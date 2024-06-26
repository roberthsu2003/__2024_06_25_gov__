import math
import pyinputplus as pyip

side = pyip.inputNum('請輸入對邊',min=0,max=100)
another_side = pyip.inputNum('請輸入斜邊')
radian = math.asin(side / another_side)
degree = math.degrees(radian)
print(f"對邊:{side},斜邊:{another_side},角度:{round(degree,ndigits=2)}")