#!/usr/bin/python
#coding=utf-8

#print('nihao,世界','世界');
#print '你好，世界';


#name=raw_input("请输入姓名");
#print '输入的姓名是'+name;

#list是一个可变的有序集合
classmates=['Michael','bob','tracy'];
print classmates;
a=len(classmates);
print a;
print classmates[2];
print classmates[-1]; #使用-1做索引，直接获取最后一个元素
print classmates[-2]; #使用-2做索引，获取倒数第二个元素
classmates.append('lll');
classmates.insert(1,'jack');#在固定位置添加元素
classmates.pop(3);#删除固定位置元素
classmates[1]='sarch';#将某个固定位置元素替换成别的元素

L = ['Apple', 123, True];#list中的元素数据类型可以不同

s = ['python', 'java', ['asp', 'php'], 'scheme'];

p = ['asp', 'php'];
s = ['python', 'java', p, 'scheme'];

#元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates = ('Michael', 'Bob', 'Tracy');

#定义只有一个元素的元组时要在后边添加‘，’，因为不添加，表示数字公式的小括号
t=(1,);

m=('aaa',);
print m;
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
t = ('a', 'b', ['A', 'B']);
t[2][0] = 'X';
t[2][1] = 'Y';
print t;