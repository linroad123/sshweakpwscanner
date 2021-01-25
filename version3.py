#!/usr/bin/env python
#!coding:utf-8

from pexpect import pxssh
import traceback
import os
import getpass

def send_command(child,cmd):
	#send a command
	child.sendline(cmd)
	
	#expect prompt character on commandline
	child.prompt()
	
	#print content 
	print(child.before)
	
def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        # use pxssh class login method to ssh login
        s.login(host,user,password)
        return s
    except:
        print('[-] Error Connecting')
        exit(0)

def main():
    host = input('Hostname: ')
    user = input('User: ')
    password = getpass.getpass()
    child  = connect(host, user, password)
    send_command(child,'ls')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print (str(e))
        traceback.print_exc()
        os._exit(1)
