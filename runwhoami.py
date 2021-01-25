#!/usr/bin/env python
#!coding:utf-8

from pexpect import *
result = pexpect.spawn('whoami')
result.expect(pexpect.EOF)
print(result.before)