#!/usr/bin/env python
#!coding:utf-8

import getpass
import pexpect
import traceback
import os

# the set of warning character when SSH successfully connect
PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(child,cmd):
	#send a command
	child.sendline(cmd)
	
	#expect prompt character on commandline
	child.expect(PROMPT)
	
	#print content 
	print(child.before)
	
def connect(user, host, password):
	#indicate host already use a new public key
	ssh_newkey = 'Are you sure you want to continue connecting' #alert when using private key to login 
	connStr = 'ssh ' + user + '@' + host
	
	# Generate a spawn subprogram object for the ssh command
    child = pexpect.spawn(connStr)
    	
    	# expect ssh_newkey character
    	# indicate the occurance of character of input password, otherwise timeout
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword: '])
    	
    	# timeout
    if ret == 0:
    	print ('[-] Error Connecting')
    	return
    	
    	# ssh_newkey
    if ret == 1:
            # send yes response to ssh newkey and expect the occurance of character of input password
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword: '])
        if ret == 0:
            print ('[-] Error Connecting')
            return
        
        # send password
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = input('Hostname: ')
    user = input('User: ')
    password = getpass.getpass()
    child  = connect(user, host, password)
    send_command(child,'uname -a')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print (str(e))
        traceback.print_exc()
        os._exit(1)
