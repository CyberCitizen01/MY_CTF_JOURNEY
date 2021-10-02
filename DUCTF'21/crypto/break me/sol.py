from base64 import b64encode, b64decode
from pwn import *
from string import printable

from Crypto.Cipher import AES

key = '!_SECRETSOURCE_!'

p = remote('pwn-2021.duc.tf', 31914)

# for n in range(len(key) + 1, 17):
#     p.sendlineafter(b"Enter plaintext:\n", b"A"*n)
#     chunk4 = b64decode(p.recvline(keepends=False))[48:]
#     for char in printable:
#         p.sendlineafter(b"Enter plaintext:\n", char.encode()+ key.encode() + b"0"*(16 - n))
#         chunk3 = b64decode(p.recvline(keepends=False))[32:48]
#         print(f'{chunk4.hex() = }\n{chunk3.hex() = }\n{char = }')
#         if chunk3 == chunk4:
#             print(f'{key = }, {char = }')
#             key = char + key
#             break
# print(key)

p.sendlineafter(b"Enter plaintext:\n", b"")
c_flag = b64decode(p.recvline(keepends=False))[:32]

decipher = AES.new(key.encode(), AES.MODE_ECB)

print(decipher.decrypt(c_flag))
