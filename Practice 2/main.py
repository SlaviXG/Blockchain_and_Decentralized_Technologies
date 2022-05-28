import hexIntConverter

n = 255#input()

#print(hexIntConverter.hex_to_big_endian(n))

#print(hexIntConverter.hex_to_little_endian(n))

#print(len(hexIntConverter.big_endian_to_hex(n)))
#print(hexIntConverter.big_endian_to_hex(n))

print(hexIntConverter.little_endian_to_hex(n, 32))
