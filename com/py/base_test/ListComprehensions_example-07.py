#!/usr/bin/python
#coding=utf-8
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#生成[1x1, 2x2, 3x3, ..., 10x10]
print [x*x for x in range(1,11)]
print [x * x for x in range(1, 11)]
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

# for循环后面还可以加上if判断
print [x*x for x in range(1,11) if x%2==0]

#还可以使用两层循环，可以生成全排列
sss=[m+n for m in 'abcd' for n in 'ABCD']
print sss

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print d

m={'a':'1','b':'2','c':'3'}
ii=[k+'='+v for k,v in m.iteritems()]
print ii

