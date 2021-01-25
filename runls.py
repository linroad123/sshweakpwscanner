#!/usr/bin/env python
#!coding:utf-8

from pexpect import *
result = run ('ls')
print(result)