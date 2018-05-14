#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import random
from math import sqrt

# 输出2-100之间的素数
num = []
for i in range(2, 100):
    for j in range(2, int(sqrt(i) + 1)):
        if (i % j == 0):
            break
    else:
        num.append(i)
print num


# 判断一个整数是不是素数
def is_primer(number):
    if number < 2:
        print '输入有误！'
    else:
        i = 2
        for i in range(2, int(sqrt(number) + 1)):
            # j = 2
            # for j in range(2, int(sqrt( number ) + 1 )):
            # for j in range(2,i):
            if number % i == 0:
                return False
        else:
            return True


print is_primer(16)

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# 打印*字塔
i = 1
# j=1
while i <= 9:
    if i <= 5:
        print ("*" * i)

    elif i <= 9:
        j = i - 2 * (i - 5)
        print("*" * j)
    i += 1
else:
    print("")



# 冒泡排序算法
# arr = random.sample(range(1,100),20)
arr =[1,9,3,5,4,8,0]
