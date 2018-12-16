#!/usr/bin/python
a = 0
i = 0
b = 1
c = (a + b)

limit = input("Selectionner le nombre de ligne a afficher : ")
for i in range(limit):
    print (str(a) + " + " + str(b) + " = " + str(c))
    a = b
    b = c
    c = a + b
