class A(object):
    aa = 0
    def __init__(self):
        self.a = 1
        self.b = 0

class B(A):
    bb = 0
    def __init__(self):
        super().__init__()
        self.c = 0
    
print("获取类A的属性：{0}".format(A.__dict__))
print("获取类B的属性：{0}".format(B.__dict__))
b = B()
print("获取实例b的属性{0}：".format(b.__dict__))
b.__dict__['e'] = 1
print("获取实例b的属性{0}：".format(b.__dict__))
print(dir(b))
"""
    1.\__dict__查询实例b的属性，是不会显示类B的bb属性
    2.如果查询类B的属性也不会返回实例属性
    3.B继承A，\__dict__查询B的属性，并没法返回A的属性aa
    4.可以通过直接修改\__dict__的方式来更改对象的属性
    5.dir()能查看int，string类型的属性，但\__dick__不能
"""