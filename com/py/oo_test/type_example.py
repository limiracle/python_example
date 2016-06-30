#coding=utf-8

#我们来判断对象类型，使用type()函数
print type(123)
print type('abc')
print type(abs)

import types
type('abc')==types.StringType
type(str)==types.TypeType
#有一种类型就叫TypeType，所有类型本身的类型就是TypeType


#使用isinstance()函数
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score
bart = Student('bart', 200)
print isinstance(bart,Student)

#使用dir()
print dir('abc')