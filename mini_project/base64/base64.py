#!/usr/bin/python3
import sys
special64_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

# BUAT LOGIC NYA
def ubah_utf(input_string):
    utf_result = []
    for char in input_string:
        utf_result.append(ord(char))
    
    return utf_result

def ubah_biner(input_utf, enc=True):
    biner_result = ""
    if (enc):
        for dec in input_utf:
            biner_padd = str(bin(dec))[2:]
            biner_result += biner_padd.zfill(8)
    else:
        for dec in input_utf:   
            biner_padd = str(bin(dec))[2:]
            biner_result += biner_padd.zfill(6)
    return biner_result

def bit6(input_biner):
    bit6_result = []
    for i in range(0, len(input_biner), 6):
        bit6_result.append(input_biner[i:i+6])
    return bit6_result

def searching_index(base64_string_encode):
    index64 = []
    for char in base64_string_encode:
        index_value = special64_char.index(char)
        index64.append(index_value)
    return index64

def utf64(biner64):
    utf_value = []
    for biner in range(0, len(biner64), 8):
        value = biner64[biner:biner+8]
        utf_value.append(int(value, 2))
    return utf_value

# Buat OPTIONNYA
def Base64_encode(input):
    base64_encode = ""
    utf_list = ubah_utf(input)
    biner_list = ubah_biner(utf_list, True)
    bit6_list = bit6(biner_list)
    last_bit = bit6_list[-1]

    while len(last_bit) % 6 != 0:
        last_bit += '0'
    bit6_list[-1] = last_bit
    
    for char in bit6_list:
        value = int(char, 2)
        base64_encode += special64_char[value]
    
    if len(input) % 3 == 2:
        base64_encode += ('='*1)
    elif len(input) % 3 == 1:
        base64_encode += ('='*2)
    
    print(base64_encode)

def Base64_decode(input: str):
    base64_decode = ""
    clean_input = input.rstrip('=')
    base64_index = searching_index(clean_input)
    base64_biner = ubah_biner(base64_index, False)
    base64_utf = utf64(base64_biner)
    for char in range(0, len(base64_utf)):
        base64_decode += chr(base64_utf[char])

    print(base64_decode)

# BUAT MAIN SCRIPT
def main():
    try:
        if len(sys.argv) < 3:
            print(f"Penggunaan: {sys.argv[0]} <string> -d (untuk decode) | -e (untuk encode)")
            return 0
        if sys.argv[1] == "":
            print('""')
            return 0
        else:
            if sys.argv[2] == '-e':
                string_input = f"{sys.argv[1]}" 
                Base64_encode(string_input)
            elif sys.argv[2] == '-d':
                string_input = f"{sys.argv[1]}" 
                Base64_decode(string_input)
            else:
                print(f"Penggunaan: {sys.argv[0]} <string> -d (untuk decode) | -e (untuk encode)")
    except ValueError:
        print(f"Penggunaan: {sys.argv[0]} <string> -d (untuk decode) | -e (untuk encode)")
main() 
