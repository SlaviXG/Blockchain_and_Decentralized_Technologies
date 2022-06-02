import hexIntConverter

val = input("\ni.\tValue: ")
if(hexIntConverter.stringIsHexVal(val)):
    print("ii.\tNumber of bytes: ", hexIntConverter.countNumberOfBytes(val))
    print("iii.Little-endian:	", hexIntConverter.hex_to_little_endian(val))
    print("iv.\tBig-endian: ", hexIntConverter.hex_to_big_endian(val))
else:
    print("Incorrect hex value.")


### Testing functions :

#print(hexIntConverter.hex_to_big_endian(2))
#print(hexIntConverter.hex_to_little_endian(n))
#print(len(hexIntConverter.big_endian_to_hex(n)))
#print(hexIntConverter.big_endian_to_hex(255))
#print(hexIntConverter.little_endian_to_hex(255, 32))