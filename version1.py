#!/usr/bin/env python
#!coding:utf-8

import getpass
import pexpect
import traceback
import os

def run(user, host, password, command):
    ssh_newkey = 'Are you sure you want to continue connecting' #alert when using private key to login 
    # Generate a spawn subprogram object for the ssh command
    child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey,'password: '], timeout=5)
    # if login timeout, print wrong information and quit
    # i=0 refer to the first element in list --pexpect.TIMEOUT
    if i == 0:
        print ('ERROR!')
        print ('SSH can\'t login, error:')
        print (child.before, child.after)
        return None
    if i == 1:
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT,'password: '])
        if i == 0:
            print ('ERROR!')
            print ('SSH can\'t login, error:')
            print (child.before, child.after)
            return None
    # enter password
    child.sendline(password)
    return child

def main():
    host = input('Hostname: ')
    user = input('User: ')
    password = getpass.getpass()
    command = input('Enter the command: ')
    child  = run(user, host, password, command)
    # matching pexpect,EOF
    child.expect(pexpect.EOF)
    # output command result
    print(child.before)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print (str(e))
        traceback.print_exc()
        os._exit(1)