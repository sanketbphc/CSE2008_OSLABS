import sys
import os
import time

sys.stdout.write('Ready to fork? (Press enter to continue) ')
sys.stdout.flush()

sys.stdin.readline()

PID_AFTER_FORK = os.fork()

if PID_AFTER_FORK > 0:
    print('Inside parent')
else:
    print('Inside child')
