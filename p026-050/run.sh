#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 problem_number"
  exit 1
fi

file="p$1"
src="$file.c"

gcc -Wall -o $file $src && ./$file && rm $file
