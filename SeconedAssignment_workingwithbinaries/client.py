import struct
import sys


if len(sys.argv) <5:
	print("Usage example: python",sys.argv[0],"db1.bin","db2.bin","db3.bin","db4.bin","db5.bin")
	exit(1)
	

format_strings = ['9sif','f?c','ci9s','f9s?']
for i in range(1,5):
      with open(sys.argv[i], "rb") as f:
        binary_data = f.read()
        unpacker = struct.Struct(format_strings[i-1])
        unpacked_data = unpacker.unpack(binary_data)
        print(unpacked_data)



values = [(b'elso', 73, True), (76.5, False, b'X'), (64, b'masodik', 83.9), (b'Z', 95, b'harmadik')]
formats = ['15si?', 'f?c', 'i13sf', 'ci16s']

for i in range(4):
    s = struct.Struct(formats[i])
    packed_data = s.pack(*values[i])
    print(packed_data)

# values = [(b'elso', 73, True), (76.5, False, b'X'), (64, b'masodik', 83.9), (b'Z', 95, b'harmadik')]
# formats = ['<4si?', '<f?c', '<i7sf', '<ci8s']


# for i in range(4):
#     s = struct.Struct(formats[i])
#     packed_data = s.pack(*values[i])
#     print(packed_data)


# values = [(b'elso', 73, True), (76.5, False, b'X'), (64, b'masodik', 83.9), (b'Z', 95, b'harmadik')]
# formats = ['4si?', 'f?c', 'i7sf', 'ci8s']

# packed_data_list = []

# for i in range(4):
#     s = struct.Struct(formats[i])
#     packed_data = s.pack(*values[i])
#     packed_data_list.append(packed_data)

# for data in packed_data_list:
#     print(data)


# values = [
#     (b'elso', 73, True),
#     (76.5, False, b'X'),
#     (64, b"masodik", 83.9),
#     (b'Z', 95, b"harmadik")
# ]

# formats = ['4sxI?', 'f?c', 'I7sxf', 'ci8sx']

# for value, format_str in zip(values, formats):
#     s = struct.Struct(format_str)
#     packed_data = s.pack(*value)
#     print(packed_data)



# packed_data = [
#     b'elso\x00\x00\x00\x00S\x00\x00\x00\x01',
#     b'\x00\x00\xadB\x00X',
#     b'J\x00\x00\x00masodik\xcd\xcc\xbbB',
#     b'Z\x00\x00\x00i\x00\x00\x00harmadik\x00'
# ]

# # Define the format strings for unpacking
# formats = ['4sxi?', 'fc', '11s4sf', 'ci8s']

# for packed, format_str in zip(packed_data, formats):
#     s = struct.Struct(format_str)
#     unpacked_data = s.unpack(packed)
#     print(unpacked_data)




# s1 = "test".encode()
# packer=struct.Struct('4s')
# packed = packer.pack(s1)
# print(packed)

