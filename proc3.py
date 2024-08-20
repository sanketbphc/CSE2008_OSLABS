import sys
import os
import time

sys.stdout.write('Ready to fork? (Press enter to continue) ')
sys.stdout.flush()

sys.stdin.readline()

os.fork()

print('I will print twice')

time.sleep(10)

print('I will also print twice')
