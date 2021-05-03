#!/bin/bash
error() {
    printf '\E[31m'; echo "$@"; printf '\E[0m'
}

process() {
    chmod +x blyat.py
    cp blyat.py /usr/bin/blyat
    echo "Blyat Instalado Correctamente" > installed
    blyat installed
    rm installed    
}

if [[ $EUID -eq 0 ]]; then
    process
 else
     echo
     error "This script should not be run using sudo or as the root user"
     exit 1
fi
