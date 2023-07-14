from pwn import *

io = remote('127.0.0.1',4444)
io.sendline(b'11111')
io.interactive()
