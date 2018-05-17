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
for i in range(1,len(arr)+1):
    for j in range(1,len(arr)-i+1):
        if arr[j-1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
print '排序之后的顺序：',arr

#插入排序算法
arr = random.sample(range(1,100),10)
print arr
for i in range(1,len(arr)):
    temp = arr[i]
    j=i
    while (j>0 and arr[j-1]>temp):
        arr[j]=arr[j-1]
        j-=1
    arr[j]=temp
print arr


def InsertSort(myList):
    # 获取列表长度
    length = len(myList)

    for i in range(1, length):
        j = i - 1  # 设置当前值前一个元素的标识
        if (myList[i] < myList[j]):# 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
            temp = myList[i]
            myList[i] = myList[j]
            j = j - 1 # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            while j >= 0 and myList[j] > temp:
                myList[j + 1] = myList[j]
                j = j - 1

            # 将临时变量赋值给合适位置
            myList[j + 1] = temp


myList = [49, 38, 65, 97, 76, 13, 27, 49]
InsertSort(myList)
print(myList)



