#!/usr/bin/env python
from sys import argv

if len(argv) >= 2:
    name = argv[1]    
else:
    name = 'stranger'
print 'Hello ' + name  