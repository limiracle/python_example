#!/usr/bin/python
#coding=utf-8

#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
def f(x):
    return x*x
print map(f,[1,2,3,4,5])

#把这个list所有数字转为字符串
print map(str,[1,2,3,4,5,6])

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算,其效果是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#对一个序列求和，就可以用reduce实现
def add(x,y):
    return x+y
print reduce(add,[1,2,3,4,5,6,7,8,9])

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])

def char2nums(s):
    return  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn,map(char2nums,'13245234567'))

#把str转换为int的函数

def str2int(x):
    def fn(x, y):
        return x * 10 + y

    def char2nums(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2nums,x))

print str2int('123124')

#还可以用lambda函数进一步简化成
def str2int(x):
    def char2nums(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x,y:x*10+y,map(char2nums,x))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
Updict={'A':'A','a':'A','B':'B','b':'B','C':'C','c':'C','D':'D','d':'D','E':'E','e':'E','F':'F','f':'F','G':'G','g':'G','H':'H','h':'H','I':'I','i':'I'}
downdict={'A':'a','a':'a','B':'b','b':'b','C':'c','c':'c','D':'d','d':'d','E':'e','e':'e','F':'f','f':'f','G':'g','g':'g','H':'h','h':'h','I':'i','i':'i'}

def su(x,y):
    return x+y
def low(x):
    return downdict[x]
def upLow(x):
    ll=map(low,x[1:])
    ll.insert(0,Updict[x[0]])
    return reduce(su,ll)


def su1(x):
    return x[0].upper()+x[1:].lower()
def upLow1(x):
    return map(su1,x)

print map(upLow,['adai', 'FGIA', 'HAig'])
print upLow1(['adai', 'FGIA', 'HAig'])


#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(ll):
    def mul(a,b):
        return a*b
    return reduce(mul,ll)
print prod([1,2,3])