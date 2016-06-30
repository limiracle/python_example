#!/usr/bin/python
#coding=utf-8

#高阶函数英文叫Higher-order function
print abs(-10)
print abs
#可见，abs(-10)是函数调用，而abs是函数本身。

#把函数本身赋值给变量 函数本身也可以赋值给变量，即：变量可以指向函数
f=abs
print f

#函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数
#abs=10
#print abs(-10)

#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数了
#注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x)+f(y)
print add(10,2,abs)