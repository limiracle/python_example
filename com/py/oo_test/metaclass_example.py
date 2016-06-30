#coding=utf-8
from hello import Hello
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self,name='world'): #先定义函数
    print('Hello, %s' %name)

Hello1=type('Hello1',(object,),dict(hello=fn)) #创建Hello class
m=Hello1()
m.hello()
print(type(Hello1))
print(type(m))

#要创建一个class对象，type()函数依次传入3个参数：

#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。



#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
#__new__()方法接收到的参数依次是：
#当前准备创建的类的对象；
#类的名字；
#类继承的父类集合；
#类的方法集合。

class MyList(list):
    __metaclass__=ListMetaclass