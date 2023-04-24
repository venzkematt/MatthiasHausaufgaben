#!/bin/bash
if [ -e /etc/resolv.conf ]; then
    echo "Die gibt es"
    else
    echo "Die gibt es nicht"
fi
exit 0