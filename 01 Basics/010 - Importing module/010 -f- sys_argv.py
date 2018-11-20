#-*- coding: utf-8 -*-

"""
Docs


Instruction!
RUN in cmd.exe

python "010 -f- sys_argv.py" hello 34

[output
-> ['010 -f- sys_argv.py', 'hello', '34']
-> hello

"""

import sys

print sys.argv


#first argument is FileName
if len(sys.argv) > 1:
    print sys.argv[1]
