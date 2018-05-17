#!/usr/bin/env python
# -*- coding:utf-8 -*-



"""
解决中文在dos命令行下显示问题，dos中文默认编码为GBK，python使用中文时通常是UTF-8
需要做一下字符编码转换，utf-8通过解码转化为unicode,然后通过unicode编码转化为gbk；
其实只需要把utf-8转化为unicode编码就可以，因为当windows的CMD遇到unicode编码时，
会自动给你转化为gbk编码。
另外python3x中没有unicode类型，但可以支持从utf-8直接解码转换为gbk。
"""

content = "你好，世界！"
#将字符串由utf-8解码为unicode
c_unicode = content.decode("utf-8")
#将字符串编码为gbk
c_gbk = c_unicode.encode("GBK")
print (c_gbk)

content = "你好，世界！"
#将字符串由utf-8解码为unicode
c_unicode = content.decode("utf-8")
print (c_gbk)


#python3x
concent = "请输入内容："
#将字符串由utf-8解码为gbk
c_gbk = concent.decode("gbk")
print (c_gbk)








