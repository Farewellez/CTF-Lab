#!/usr/bin/python3
hexa_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
biner_string = ""
special64_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

for hex in hexa_string:
    hex_value = int(hex, 16)
    bin_string = bin(hex_value)[2:]
    bin_padded = bin_string.zfill(len(hex) * 4)
    biner_string += bin_padded

bin6_list = []

for index_biner in range(0, len(biner_string), 6):
    potongan_asli = biner_string[index_biner: index_biner+6]
    bin6_list.append(potongan_asli)

my_result = ""
cryptopals_result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

for bin6 in bin6_list:  
    bin_value = int(bin6, 2)
    if (bin_value > 63):
        my_result += "="
    else:
        my_result += special64_char[bin_value]

print(my_result)

if len(my_result) == len(cryptopals_result):
    print("kedua hasil sama, decode berhasil!!!")
else:
    print("skill issue lu bang owkoakowakoawk")
