#!/usr/bin/python
# coding:utf-8
import subprocess
import socket
from datetime import datetime
import emoji


t1 = datetime.now()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Banner():
    print "-" * 60
    print (bcolors.OKGREEN + '''
     ____  __ __  ___ ___   ____  ____         ___  _____ ___   
    |    \|  |  ||   |   | /    ||    \       /  _]/ ___/|   \  
    |  o  )  |  || _   _ ||  o  ||  o  )     /  [_(   \_ |    \ 
    |   _/|  ~  ||  \_/  ||     ||   _/     |    _]\__  ||  D  |
    |  |  |___, ||   |   ||  _  ||  |       |   [_ /  \ ||     |
    |  |  |     ||   |   ||  |  ||  |       |     |\    ||     |
    |__|  |____/ |___|___||__|__||__|       |_____| \___||_____|
                                                                
    ''' + bcolors.ENDC)
    print "-" * 60
subprocess.call('clear', shell=True)
Banner()

ipaddr = raw_input("Saisir l'adresse ip : ")
#ipaddr = "172.20.10.3"
portini = input("Saisir port initiale : ")
portdest = input("Saisir port destination : ")
nbport = 0

for port in range (portini,portdest):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ipaddr, port))
    if result == 0:
        nbport += 1
        print (emoji.emojize(bcolors.OKGREEN + "Port {}: Ouvert :thumbs_up:".format(port) + bcolors.ENDC))
    else:
        print (bcolors.FAIL + "Port {}: Ferme ".format(port) + bcolors.ENDC)
    s.close()
t2 = datetime.now()
total =  t2 - t1
print("\n" + "_" * 70)
print("\n Temps ecoule : {} Nombre de ports ouverts : {}".format(total,nbport))
print("\n" + "-" * 70)




