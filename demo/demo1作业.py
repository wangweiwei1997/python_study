# -*-coding:UTF-8 -*-


#变量
name=10
cate_name=20

#赋值(赋什么打什么，以最后一次为准）
chang=15
kuan=5
gao=3
tiji=chang*kuan*gao
print(tiji)
tiji='wangwei'
print(tiji)

#运算符和表达式
month_sal=1000+200
print(month_sal)

#   /小数点
print(9/3)#结果3.0
#   //整数
print(9//3)#结果3
print(10//3)#结果3
#   %除数的余数
print(10/3)#结果1；读法：10模3
#   **（幂）
print(5**3)#结果：125


#if
sal=4000
if sal>2000:
    print('超高')
#and or    
sal=4000
comm=300
if sal>2000 and comm>200:
    print('很高')
    
sal=4000
comm=300
if sal>2000 or comm>200:
    print('很高')
    
#整形
chang=30
#浮点
comm=100.5
#布尔
True
False

sal=3000
if sal>2000:
    print('好')


#字符串：所有的字符串用单引号和双引号
name='王苇'
name="王苇"
name=''




#字典和元祖(无序）（一堆行为）
userinfo = ()
#一维
# userinfo = ('王苇',123,'耗子',123,'兔子')
#二维
#           0                         1                        2
userinfo = ('王苇',123,'好好',123,'兔子'),('王苇',123,'完美',123,'兔子'),('王苇',123,'耗子',123,'兔子')
#           -3                        -2                       -1
name = ['王苇 ',12,'耗子',123,'兔子']


print(userinfo[0])
print(userinfo[1])
print(userinfo[2])

print(userinfo[0:2])

userinfo2=('王苇',123,'好好',123,'兔子')

# for i in range(5):
#     print(i)
# 
# for i in range(4):
#     print(userinfo2[i])
for i in range(4):
    print(userinfo2[i])


#增加 appdne 
userinfo2=['王苇',123,'好好',123,'兔子']
userinfo2.append('兔兔')
print(userinfo2)

userinfo2.insert(1,'张珊')
print(userinfo2)



    




















    


















