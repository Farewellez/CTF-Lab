#!/bin/bash

# variabel
harga_ayam=10
nama_ayam=Risky

# sapa dunia
dunia='Hello          world!'

echo "Harga dari seekor ayam adalah: $harga_ayam"
echo "Nama dari ayam ini adalah: $nama_ayam"
echo $dunia

FILELIST=`ls`
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%d).txt
echo "File disimpan di: $FileWithTimeStamp"