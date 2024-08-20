#Two things that might be important for a parent process - it might want to wait till a child process completes, and it might want to know whether a child process run successfully or not.

#Success or failure of a process is usually indicated by a number which is called its exit status. You can set the exit status of a Python process by calling sys.exit(). Calling this function gracefully terminates your Python process (by ensuring that the finally clauses of the try statement are run), and sets the exit status to the value passed to it.

#An exit status can be between 0 and 127. 0 means success, everything else indicates failure.

#A parent process can wait for a child process by using the os.waitpid() call. waitpid() takes a child pid as argument alongwith an integer specifying options (usually set to 0). It returns a tuple containing the child pid and exit status indication. The exit status indication is a 16-bit number whose low byte is the signal number that killed the process, and whose high byte is the exit status (if the signal number is zero). For now we will only worry about the exit status.

import sys
import os
import time

sys.stdout.write('Ready to fork? (Press enter to continue) ')
sys.stdout.flush()

sys.stdin.readline()

PID_AFTER_FORK = os.fork()

if PID_AFTER_FORK > 0:
    print('Inside parent')
    status_encoded = os.waitpid(PID_AFTER_FORK, 0)[1]
    print('Inside parent, child exited with code', status_encoded >> 8)
else:
    print('Inside child')
    time.sleep(2)
    sys.exit(127)
