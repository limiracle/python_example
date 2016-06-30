#!/usr/bin/python
#coding=utf-8

#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#dict的key必须是不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']


#set
s = set([1, 2, 3])
#注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。

#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
s.add(8)
s.remove(1);


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2