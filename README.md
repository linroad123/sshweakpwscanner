# SSH Weak Password Scanner


## Background

Pexpect is a Python implementation of Don Libes' Expect language. It is a Python module that is used to start subprogram and use regular expressions to make specific responses to the output of the program to achieve automatic interaction with it.

Pexpect can be used to realize automatic interaction with ssh, ftp, telnet and other programs. It can be used to automatically copy software installation packages and install them on different machines. It can also be used to automate the interaction with command lines in software testing.


## Usage

### Pexpect's run() function

The Run() function can be used to run commands, similar to the system() function of the Python os module, run() is implemented by the Pexpect class.

If the path of the command is not completely given, *run* will use the *which* command to try to search for the path of the command.

Different from os.system(), run() can easily obtain the output result of the command and the exit status of the command at the same time.

The return result needs us to actively obtain and output

### spawn() usage example

Pexpect provides a spawn() class

  Spawn is the main class of the Pexpect module, used to start subprograms. It has a wealth of ways to interact with subprograms to realize user control of subprograms. It mainly uses *pty.fork()* to generate child processes, and calls the *exec()* series of functions to execute the command parameter.

The method of use is as follows:
```sh
child = pexpect.spawn ('whoami') #Execute whoami command

child = pexpect.spawn ('touch test.txt') #New test.txt file

child = pexpect.spawn ('ls /tmp') #Display the contents of the /tmp directory spec
```
### Definition of expect()
In order to control the subrprogram, wait for the subrprogram to produce a specific output and make a specific response, you can use the expect method.

```sh
expect(self, pattern, timeout=-1, searchwindowsize=None)
```
In the parameters: pattern can be a regular expression, pexpect.EOF, pexpect.TIMEOUT, or a list of these elements. It should be noted that when the type of pattern is a list, and more than one of the output results of the subprogram is matched successfully, the result returned is the element that appears first in the buffer, or the leftmost element in the list. Use timeout to specify the timeout period for waiting for the result, in seconds. When the reservation time is exceeded, expect matches pexpect.TIMEOUT.

Expect() may throw two types of exceptions during execution, namely EOF and TIMEOUF, where EOF usually represents the exit of the subroutine, and TIMEOUT represents a timeout while waiting for the target regular expression.

### send functions
```sh
send(self, s)

sendline(self, s='')

sendcontrol(self, char)
```
These methods are used to send commands to subprogram to simulate the behavior of input commands. The difference with send() is that sendline() will input an extra carriage return, which is more suitable for simulating the operation of inputting commands to the subprogram. When you need to simulate the behavior of sending "Ctrl+c", you can also use sendcontrol() to send control characters.
