#!/bin/bash
if [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Das Argument ist eine Zahl"
    exit 0
fi

if [[ $1 =~ ^[a-zA-Z]+$ ]]; then
    echo "Das Argument ist ein Wort"
    else
    echo "Das Argument ist weder eine Zahl noch ein Wort"
fi
exit 0