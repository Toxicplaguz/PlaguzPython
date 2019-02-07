#!/bin/bash

mkdir /root/Collect
chmod 775 -R /root/Collect

mount /dev/sdb2 /media/root
read -p "Nom d'utilisateur de la windows :" user
echo " -- Copie de : NTUSER.DAT"
cp /media/root/Users/$user/NTUSER.DAT /root/Collect
echo " -- Copie des Prefetch ..."
cp -R /media/root/Windows/Prefetch /root/Collect
echo " -- Copie des Logs ..."
cp -R /media/root/Windows/System32/winevt/Logs /root/Collect
echo " -- Copie de la ruche SYSTEM ..."
cp /media/root/Windows/System32/config/SYSTEM /root/Collect
echo " -- Copie de la ruche SAM ..."
cp /media/root/Windows/System32/config/SAM /root/Collect
echo " -- Copie de la ruche DEFAULT ..."
cp /media/root/Windows/System32/config/DEFAULT /root/Collect
echo " -- Copie de la ruche SECURITY ..."
cp /media/root/Windows/System32/config/SECURITY /root/Collect
echo " -- Copie de la ruche SOFTWARE ..."
cp /media/root/Windows/System32/config/SOFTWARE /root/Collect
echo " -- Création d'une timeline ... "
fls -o 718848 -z GMT -s 0 -m '/' -f ntfs -r /dev/sdb >> timeline.txt
mactime -b timeline.txt -z GMT >> /root/Collect/timeline.csv
echo " -- Timeline générée : /root/Collect/timeline.csv "
echo " -- Copie du Bureau .. "
cp -R /media/root/Users/$user/Desktop /root/Collect
echo " -- Copie des Downloads .."
cp -R /media/root/Users/$user/Downloads/ /root/Collect
echo " -- Copie de la Corbeille .."
cp -R /media/root/'$Recycle.Bin'/ /root/Collect
echo "-- Copie des strings Cookie Chrome .."
strings /media/root/Users/$user/AppData/Local/Google/Chrome/User\ Data/Default/Cookies >> /root/Collect/Chrome-Cookies-strings.txt
echo "-- Copie des strings History Chrome .."
strings /media/root/Users/$user/AppData/Local/Google/Chrome/User\ Data/Default/History >> /root/Collect/Chrome-History-strings.txt
echo " -- Extraction du userassist dans la ruche NTUSER.DAT .."
/usr/local/bin/rip.pl -p userassist -r /root/Collect/NTUSER.DAT >> /root/Collect/userassist.txt
echo " -- Extraction du shimcache dans la ruche SYSTEM .."
/usr/local/bin/rip.pl -p shimcache -r /root/Collect/SYSTEM >> /root/Collect/shimcache.txt
echo " -- Extraction du runmru dans la ruche NTUSER.DAT .."
/usr/local/bin/rip.pl -p runmru -r /root/Collect/NTUSER.DAT >> /root/Collect/runmru.txt
echo -e "\n[+] Collecte Terminée : /root/Collect --"
