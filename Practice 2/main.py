import hexIntConverter


val = input("\ni.\tValue: ")
print("ii.\tNumber of bytes: ", (len(val)-2)//2)
print("iii.Little-endian:	", hexIntConverter.hex_to_little_endian(val))
print("iv.\tBig-endian: ", hexIntConverter.hex_to_big_endian(val))



### Testing functions :

#print(hexIntConverter.hex_to_big_endian(n))
#print(hexIntConverter.hex_to_little_endian(n))
#print(len(hexIntConverter.big_endian_to_hex(n)))
#print(hexIntConverter.big_endian_to_hex(n))
#print(hexIntConverter.little_endian_to_hex(n, 32))
