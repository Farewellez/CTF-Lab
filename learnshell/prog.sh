#!/bin/bash
function File {
    # think you are inside the file
    # Change here
    echo $* # untuk menampilkan seluruh argumen 
    TOTAL=$# # untuk menampilkan total argumen
    echo "Total argument: $TOTAL"
}

# Do not change anything
if [ ! $# -lt 1 ]; then
    File $*
    exit 0
fi

# change here
# here you can pass the arguments
bash test.sh arguments