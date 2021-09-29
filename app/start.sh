#!/bin/bash

# alias python='python3'

export PYTHON_APP_HOME=`pwd`

cd src
python3 app.py
# 起動引数を渡したい場合は下記。
# python app.py $1 $2 ...
