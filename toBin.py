import binascii

n = "Mark Thompson"
n=n.encode()
buffString = ''
for i in range(100):
	buffString += 'a'
by = binascii.a2b_hex(''.join(buffString))
by = n + by
f = open('testFile','wb')
f.write(by)
