#!/u#!/usr/bin/python
#coding=utf-8

#collections是Python内建的一个集合模块，提供了许多有用的集合类。

#namedtuple

from collections import namedtuple
Point1=namedtuple('Point',['x','y'])#point 是此namedtuple的名称
print Point1._fields
p=Point1(1,2)
print p.x
print p.y
# namedtuple('名称', [属性list]):
#坐标/半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])


#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素



#orderedDict  key有序的dict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print d
od=OrderedDict([('a',1),('b',2),('c',3)])
print od
#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedDict,self).__init__()
        self._capacity=capacity

    def __setitem__(self,key,value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last=self.popitem(last=False)
            print('remove',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)

lastDict=LastUpdatedDict(3)
lastDict.update([('a',1),('b',2),('c',3)])
print lastDict.items()
lastDict.__setitem__('d',6)
print lastDict.items()



#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c=Counter()
for ch in 'programing':
    c[ch]=c[ch]+1

print c



