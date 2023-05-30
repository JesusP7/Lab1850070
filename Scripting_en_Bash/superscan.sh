#!/bin/bash
#Script superscan.sh
#7/03/2023 - Jesús Ponce
date
    echo "|"
    echo "|---------------------|"
    echo "|    Menu Principal   |"
    echo "|---------------------|"
    echo "|1. Net Discover"
    echo "|2. Portscan1"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
read -p "Opcion [ 1 - 4 ] " c
case $c in
    1) $HOME/Documentos/Scripts/Netdiscover.sh;;
    2) $HOME/Documentos/Scripts/portscanv1.sh;;
    3) $HOME/Documentos/Scripts/welcome.sh;;
    4) echo "Bye!"; exit 0;;
esac