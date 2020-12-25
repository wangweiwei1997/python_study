# -*-coding:UTF-8 -*-
#文件名以：test开头
#函数以：test开头
#一、
def func(x):
    return x 
def test_one():
    assert func(3)==3
    
    
#二、
class testgoods():
    def func(self,x):
        return x 
    
    def test_one(self):
        assert self.func(3)== 3

g = testgoods()
g.test_one()

        








    
