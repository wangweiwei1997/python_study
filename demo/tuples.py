# -*-coding:UTF-8 -*-

#元祖
tuple_1=()
userinfo=()
#1、一维            有几个括号就有几维
userinfo=(1,'王苇',12,None)
#二维
userinfo=((1,'王苇',12,None),(2,'蔡蔡',123,None),(3,'王大',1234,None))

#2、切片        0      1    2  3    4
userinfo=('张飞','涿郡',20,1000,None)
#          -5     -4   -3  -2  -1
# print(userinfo[2])
#正切                   0取值不到（0：第一个）
# print(userinfo[0:3])
#反切:              -1取值不到（-1：最后一个）
# print(userinfo[-4:-1])

#0可不写
# print(userinfo[:3])
#-1可不写
# print(userinfo[-5:])

#遍历
userinfo=(1,'张飞','涿郡',20,1000,None)
# print(userinfo[0])
# print(userinfo[1])
# print(userinfo[2])
# print(userinfo[3])
# print(userinfo[4])
# print(userinfo[5])

# for i in range(6):
#     print(i)
# 
# for i in range(6):
#     print(userinfo[i])

#len(代表长度，可不用数长度）
for i in range(len(userinfo)):
    print(userinfo[i])






