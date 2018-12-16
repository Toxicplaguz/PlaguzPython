#!/usr/bin/env python
from cryptography.fernet import Fernet
from sys import stdout, exit
from time import time

k = Fernet.generate_key()
f = open("key/" + str(time()) + ".php","w")
f.write(k)
f.close()

stdout.write(k)
exit(0)
