from string import hexdigits

def hex_to_big_endian(hex_value):
    return int(hex_value, 16)

def hex_to_little_endian(hex_value):
    hex_value = hex_value.lstrip("0x")
    if(len(hex_value)%2):
        hex_value = '0' + hex_value
    byte_array = bytearray.fromhex(hex_value)
    byte_array.reverse()
    hex_value = ''.join(format(i, '02x') for i in byte_array)
    return int(hex_value, 16)

def big_endian_to_hex(big_endian):
    return hex(int(big_endian))

def little_endian_to_hex(little_endian, number_of_bytes):
    hex_str = hex(int(little_endian))
    hex_str = hex_str.lstrip("0x")

    byte_array = bytearray.fromhex(hex_str)
    byte_array.reverse()
    hex_str = ''.join(format(i, '02x') for i in byte_array)

    hex_str = '0x' + hex_str

    for i in range(2 * number_of_bytes - len(hex_str) + 2):
        hex_str += '0'

    return hex_str

def countNumberOfBytes(val):
    val = val.lstrip("0x")
    if (len(val) % 2):
        val = '0' + val
    return len(val)//2

def stringIsHexVal(str):
    if(len(str) > 2) :
        if(str[0] == '0' and str[1] == 'x'):
            str = str[2:]
    return all(ch in hexdigits for ch in str)