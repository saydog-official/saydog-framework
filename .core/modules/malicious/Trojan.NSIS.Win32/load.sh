#! /system/bin/sh

R='\x1b[91m'
G='\x1b[32m'
B='\x1b[34m'
Y='\x1b[33m'
C='\x1b[36m'
D='\x1b[00m'

function Percent(){
    message="$1"
    max=$2
    #make loop
    while true; do
        i=0
        while [ $i -le $max ]; do
            echo -ne "\r${R}[+]${D} $message ${Y}$i${D} %"
            sleep 0.1
            if [ $i -eq 100 ]; then
                echo -ne "${R} [${D}success${R}]${D}\n"
                exit
            fi
            let i++
        done
    done
}
Percent "Loading..." 100
