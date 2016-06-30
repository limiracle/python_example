#!/usr/bin/python
#coding=utf-8

#slice 切片操作符
L=['a','b','c','d','e']
n=3
for i in range(n):
    print L[i]

#slice 切片操作符
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print L[0:3]
print L[2:3]
print L[:3]
print L[-2:-1]

L = range(100)
#取前10个元素
print L[:10]
#取后10个元素
print L[-10:]
#前11-20个数：
print L[10:20]
#前10个数，每两个取一个
print L[:10:2]
#所有的数，每5个取一个
print L[::5]

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
(0, 1, 2, 3, 4, 5)[:3]

#字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print 'ABCDEFG'[:3]

#［::-1] 是个list的切片方法，步移为-1，从list的开始到最后
print [0, 1, 2, 3, 4, 5][::-1]