'''单例模式'''
class A(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
        return cls.__instance[cls]

class B(metaclass=A):
    '''类B'''

class C(metaclass=A):
    '''类A'''


b_1 = B()
b_2 = B()
c_1 = C()
c_2 = C()

# b_1和b_2是同一个实例， c_1和c_2是同一个实例
print(b_1, b_2)  #<__main__.B object at 0x0357F350> <__main__.B object at 0x0357F350>
print(c_1, c_2)  #<__main__.C object at 0x0357F390> <__main__.C object at 0x0357F390>

print(A.__dict__) 
# A的__dict__属性
#{'__module__': '__main__', '__call__': <function A.__call__ at 0x035A3270>, '__doc__': None}
# '_A__instance': {<class '__main__.B'>: <__main__.B object at 0x035E7270>, 
                 # <class '__main__.C'>: <__main__.C object at 0x035E72B0>}

print(A.__dict__['_A__instance'])
# __instance不知道为什么，在__dict__中的键叫_A__instance

A.__dict__['_A__instance'].pop(B)  #这样可以删除原来创建的B的单例
d_1 = B()
d_2 = B()
print(d_1, d_2)
print(b_1, b_2)

