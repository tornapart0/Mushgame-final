#!/bin/zsh
cd -- "${0:A:h}"
if [[ ! -x .venv/bin/python ]]; then
    print 'Create the Python environment first. See README.md for the three setup commands.'
    read '?Press Enter to close.'
    exit 1
fi
.venv/bin/python interpreter.py main.mylang
