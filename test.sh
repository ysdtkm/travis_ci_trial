#!/bin/bash

res=`python3 main.py 2 3`
if [ ${res} != "5" ]; then
  echo "Fail: 2 + 3 is not ${res}"
  exit 1
fi
