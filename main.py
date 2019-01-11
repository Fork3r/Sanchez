#! /usr/bin/python
from subprocess import Popen, PIPE
import os
cmd = os.path.join(os.getcwd()) + '/' + 'Sanchez'
proc = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
proc.stdin.write(b"test\n")



