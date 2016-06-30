#coding=utf-8

#multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结

from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)' %(name,os.getpid())

if __name__=='__main__':
    print 'Parent process %s' %os.getpid()
    p=Process(target=run_proc,args=('test',))
    print 'Process will start'
    p.start()
    p.join()
    print 'Process end'

#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#join()阻塞当前进程，直到调用join方法的那个进程执行完了，再继续执行当前进程
#上边程序若不加p.join()则会先打印“Process end”再执行子进程