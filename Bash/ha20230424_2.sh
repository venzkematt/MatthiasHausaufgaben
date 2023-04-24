#!/bin/bash
if [ -d /etc/default ]; then
    echo "Den Ordner gibt es"
    else
    echo "Den Order gibt es nicht"
fi

if [ -e /etc/default/pam.conf ]; then
    echo "Die Datei gibt es in diesem Ordner"
    else
    echo "Die Datei gibt es in diesem Ordner nicht, sondern in: "
    find / -name pam.conf 2>/dev/null
fi
exit 0
