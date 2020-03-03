# Written by Nihad Bakirli
#
import pexpect

child = pexpect.spawn ('ssh root@192.168.100.5')
child.expect('root@192.168.100.5\'s password: ')
child.sendline ('powerpc')
child.expect ('#')
'''
child.sendline('mkdir newfile')
child.expect('#')
print(child.before)
child.expect('#')

child.sendline('free -m')
child.expect('#')
print(child.before, file=open("output.txt", "a"))
