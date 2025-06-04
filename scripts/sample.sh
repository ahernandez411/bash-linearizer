#!/bin/bash

ME=$(whoami)

mkdir temp
echo "Hi $ME" > temp/hi-there.txt

MULTILINE="This is a 
multiline string
that will see if we can 
have this go into a single line"

echo $MULTILINE > temp/multiline.txt

ls -l temp
cat temp/hi-there.txt
cat temp/multiline.txt
