import sys
import os
import time

X = 100
Y = dict(foo=123)

if os.fork() > 0:
    print('Inside parent')
    X = 200
    Y['foo'] = 456
    print('Inside parent, X:', X)
    print('Inside parent, Y:', Y)
    # wait for child to complete
    time.sleep(3)
else:
    print('Inside child')
    time.sleep(2)
    print('Inside child, X:', X)
    print('Inside child, Y:', Y)
