#coding=utf-8
class Student(object):
    pass
#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
s=Student()
s.name='Michael'
print s.name

def set_age(self,age): #定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s,Student) #给实例锁定一个方法
s.set_age(25)#调用实例方法
print s.age
#给一个实例绑定的方法，对另一个实例是不起作用的
s2=Student();
#s2.set_age(30)

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score=score
Student.set_score=MethodType(set_age,None,Student)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现


#但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：

class Student1(object):
    __slots__=('name','age') #用tuple定义允许确定的属性名称
s1=Student1()
s1.name='Michael'
s1.age=19
s1.score=88
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
