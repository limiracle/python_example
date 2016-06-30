#!/usr/bin/python
#coding=utf-8

#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

#创建列表
L=[x*x for x in range(10)]
print L
#使用generator
g=(x*x for x in range(10))
print g

#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print g.next()
for i in g:
    print i

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
fib(10)

#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib1(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
print fib1(2)
for i in fib1(10):
    print i

def odd():
    r=''
    print 'step 1'
    yield 1
    print 'step 2'
    n=yield r
    print 'setp 3 %s' %n
    yield 5
o=odd()
o.send(None)
o.send(2)
o.send(3)


#了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。
# 其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。
#需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有Python yield语句来接收这个值。

