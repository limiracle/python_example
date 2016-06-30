#!/usr/bin/python
#coding=utf-8


#Python内置的sorted()函数就可以对list进行排序
print sorted([2,34,41,23,46,9])

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数
#通常是函数参数在前，但是sorted的函数参数是可选的，放在第二个调用比较方便，否则你必须传入：
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted([2,34,41,23,46,9],reversed_cmp)

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以：
def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)