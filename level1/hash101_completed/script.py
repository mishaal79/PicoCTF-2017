import sys

var = (sys.argv[1])
print "binary given -",var

str = (hex(int(var,2))[2:].decode('hex'))

print "string : ",str

hex = str.encode('hex')

print "hex : ",hex

dec = int(hex,16)

print "dec : ",dec
