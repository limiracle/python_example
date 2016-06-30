#!/usr/bin/python
#coding=utf-8

#协程，又称微线程，纤程。英文名Coroutine。
#协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。
#子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
#所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
#子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

#使用协程 开发 生产者-消费者模型

import time
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' %n)
        time.sleep(1)
        r='200 OK'

def produce(c):
    c.next()
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...' %n)
        r=c.send(n)
        print('[PRODUCER] Consumer return:%s' %r)
    c.close()

if __name__=='__main__':
    c=consumer()
    produce(c)

#下面来着重说明下send执行的顺序。当第一次next()（对应25行）时，启动生成器，从生成器函数的第一行代码开始执行，直到第一次执行完yield（对应第17行）后，跳出生成器函数。这个过程中，n一直没有定义。
#下面运行到send（1）时，进入生成器函数，注意这里与调用next的不同。这里是从第17行开始执行，把1赋值给n，但是并不执行yield部分。下面继续从yield的下一语句继续执行，然后重新运行到yield语句，执行后，跳出生成器函数。
#即send和next相比，只是开始多了一次赋值的动作，其他运行流程是相同的。

#注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：

#首先调用c.next()启动生成器；

#然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

#consumer通过yield拿到消息，处理，又通过yield把结果传回；

#produce拿到consumer处理的结果，继续生产下一条消息；

#produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

#最后套用Donald Knuth的一句话总结协程的特点：

#子程序就是协程的一种特例。