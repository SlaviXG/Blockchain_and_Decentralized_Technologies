def hex_to_big_endian(hex_value):
    return int(hex_value, 16)

def hex_to_little_endian(hex_value):
    hex_value = hex_value.lstrip("0x")
    return int(str(hex_value[::-1]), 16)

def big_endian_to_hex(big_endian):
    return hex(int(big_endian))

def little_endian_to_hex(little_endian, number_of_bytes):
    hex_str = hex(little_endian)
    for i in range(2 * number_of_bytes - len(hex_str) + 2):
        hex_str += '0'

    return hex_str
