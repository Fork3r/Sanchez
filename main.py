#! /usr/bin/python
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue
import sys

cmd = '/home/rsalogub/QTProjects/build-Sanchez-Desktop-Debug/Sanchez'
proc = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
#while proc.poll() == None:
proc.stdin.write(b"foo\n")
#proc.stdin.flush()
res = proc.communicate()
if proc.returncode:
    print res[1]
print 'result:', res[0]
