#coding=utf-8
#Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

import time,threading

#新线程执行代码
def loop():
    print 'thread %s is running...' % threading.currentThread().name
    n=0
    while n<5:
        n=n+1
        print 'thread %s>>%s' %(threading.currentThread().name,n)
        time.sleep(1)
    print  'thread %s ended...' %threading.currentThread().name
print    'thread %s is running...' %threading.currentThread().name

t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' %threading.currentThread().name

#由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……