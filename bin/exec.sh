#!/usr/bin/env zsh

DIR=$(dirname "$0")
BASEDIR=$(dirname "$DIR")
eval "python -u $BASEDIR/src/main.py"
