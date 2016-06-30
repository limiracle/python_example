#coding=utf-8
try:
    f=open('/local/test/test','r') #标示符'r'表示读，这样，我们就成功地打开了一个文件。

    print f.read()
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法
with open('/local/test/test','r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
    # print f.read()

#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。

import codecs
with codecs.open('/local/test/test', 'r', 'gbk') as f:
    print f.read() # u'\u6d4b\u8bd5'

with open('/local/test/test', 'w') as f:
    f.write('Hello, world!')
