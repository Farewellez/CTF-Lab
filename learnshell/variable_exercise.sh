#!/bin/bash

# string variable
BIRTHDATE="Jan 1, 2000"
Present=10
BIRTHDAY=$(date -d "$BIRTHDATE" +%A)

echo "$BIRTHDAY $BIRTHDATE"