#!/usr/bin/python
#coding=utf-8

#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print '2016-06-24'
f=now
print f
f()

#函数对象有一个__name__属性，可以拿到函数的名字：
print now.__name__
print f.__name__

#现在，假设我们要增强now()函数的功能，比如，
# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    def wrapper(*args,**kwargs):
        print 'call func %s():' %func.__name__
        return func(*args,**kwargs)
    return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now1(x,y):
    print x+y+'2016-06-24'
#把@log放到now1()函数的定义处，相当于执行了语句：now1 = log(now)

now1('a','b')
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


def log2(text):
    def decorate(func):
        def wrapper(*args,**kwargs):
            print 'call func'+text+' %s():' %func.__name__
            return func(*args,**kwargs)
        return wrapper
    return decorate

@log2('execute')
def now2(x,y):
    print x+y+'2016-06-24'
#@log2('execute')相当于now2=log2('abcd')(now2 )
now2('a','b')
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
print now2.__name__
#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#Python内置的functools.wraps可以实现类似wrapper.__name__ = func.__name__代码

import functools

def log3(*text):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print 'call func'+text+' %s():' %func.__name__
            return func(*args,**kwargs)
        return wrapper
    return decorate

@log3('execute')
def now3(x,y):
    print x+y+'2016-06-24'

print now3.__name__



###############################
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

import functools
def loge(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print 'begin call'
        r=func(*args,**kwargs)
        print 'end call'
        #wrapper不返回最终结果调用者如何获得原函数的结果？他永远只能得到None
        return r
    return wrapper

@loge
def test1():
    print 'abcd'

test1()