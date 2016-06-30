#!/usr/bin/python
#coding=utf-8

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

#在一个list中，删掉偶数，只保留奇数
def is_odd(s):
    return s%2>0
print filter(is_odd,[1,2,3,4,5,6,7,8,8,9,])