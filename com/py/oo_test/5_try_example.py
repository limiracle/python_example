#coding=utf=8
import logging
logging.basicConfig(level=logging.INFO)
try:
    print 'try,,,'
    r=10/0
    print 'result:',r
except BaseException,e:
    print 'except:',e
    logging.exception(e)
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n