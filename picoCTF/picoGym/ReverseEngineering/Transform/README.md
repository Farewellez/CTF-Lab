isi dari enc: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽

dan satu-satunya petunjuk yang ada yaitu code python yang digunakan untuk enkripsinya: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

langsung saja modif beberapa bagian kode untuk debug seperti ini

```
with open("./enc") as f:
    f_v = f.read()

flag = list(f_v)
print(flag, len(flag))


for i in range(len(flag)):
    print(flag[i], ord(flag[i]) , bin(ord(flag[i]))[2:])
    if len(bin(ord(flag[i]))[2:]) == 15:
        print("======= total 15 bit =======")
        print(flag[i], ord(flag[i]) , bin(ord(flag[i]))[2:9], int(bin(ord(flag[i]))[2:9],2), chr(int(bin(ord(flag[i]))[2:9],2)))
        print(flag[i], ord(flag[i]) , bin(ord(flag[i]))[10:], int(bin(ord(flag[i]))[10:], 2), chr(int(bin(ord(flag[i]))[10:], 2)),end="\n\n")
    else:
        print("======= total 14 bit =======")
        print(flag[i], ord(flag[i]) , bin(ord(flag[i]))[2:9], int(bin(ord(flag[i]))[2:9],2), chr(int(bin(ord(flag[i]))[2:9],2)))
        print(flag[i], ord(flag[i]) , bin(ord(flag[i]))[9:], (int(bin(ord(flag[i]))[9:], 2)), chr(int(bin(ord(flag[i]))[9:], 2) ),end="\n\n")

for i in range(len(flag)):
    if len(bin(ord(flag[i]))[2:]) == 15:
        print(chr(int(bin(ord(flag[i]))[2:9],2)),end="")
        print(chr(int(bin(ord(flag[i]))[10:], 2)),end="")
    else:
        print(chr(int(bin(ord(flag[i]))[2:9],2)),end="")
        print(chr(int(bin(ord(flag[i]))[9:], 2)),end="")
```

dari situ akan terlihat untuk char enkripsi yang berjumlah 15 bit maka 8 bit pertama + 8 bit kedua akan menghasilkan char ascii yang valid untuk flagnya. masalahnya terletak pada char yang berjumlah 14 bit. dampak dari operasi bitwise
shift leftnya terlihat di sini. semisal contoh lognya seperti ini

```
['灩', '捯', '䍔', '䙻', 'ㄶ', '形', '楴', '獟', '楮', '獴', '㌴', '摟', '潦', '弸', '弰', '㑣', '〷', '㘰', '摽'] 19
灩 28777 111000001101001
======= total 15 bit =======
灩 28777 1110000 112 p
灩 28777 1101001 105 i

捯 25455 110001101101111
======= total 15 bit =======
捯 25455 1100011 99 c
捯 25455 1101111 111 o

䍔 17236 100001101010100
======= total 15 bit =======
䍔 17236 1000011 67 C
䍔 17236 1010100 84 T

䙻 18043 100011001111011
======= total 15 bit =======
䙻 18043 1000110 70 F
䙻 18043 1111011 123 {

ㄶ 12598 11000100110110
======= total 14 bit =======
ㄶ 12598 1100010 98 b
ㄶ 12598 0110110 54 6

形 24418 101111101100010
======= total 15 bit =======
形 24418 1011111 95 _
形 24418 1100010 98 b

楴 26996 110100101110100
======= total 15 bit =======
楴 26996 1101001 105 i
楴 26996 1110100 116 t

獟 29535 111001101011111
======= total 15 bit =======
獟 29535 1110011 115 s
獟 29535 1011111 95 _

楮 26990 110100101101110
======= total 15 bit =======
楮 26990 1101001 105 i
楮 26990 1101110 110 n

獴 29556 111001101110100
======= total 15 bit =======
獴 29556 1110011 115 s
獴 29556 1110100 116 t

㌴ 13108 11001100110100
======= total 14 bit =======
㌴ 13108 1100110 102 f
㌴ 13108 0110100 52 4

摟 25695 110010001011111
======= total 15 bit =======
摟 25695 1100100 100 d
摟 25695 1011111 95 _

潦 28518 110111101100110
======= total 15 bit =======
潦 28518 1101111 111 o
潦 28518 1100110 102 f

弸 24376 101111100111000
======= total 15 bit =======
弸 24376 1011111 95 _
弸 24376 0111000 56 8

弰 24368 101111100110000
======= total 15 bit =======
弰 24368 1011111 95 _
弰 24368 0110000 48 0

㑣 13411 11010001100011
======= total 14 bit =======
㑣 13411 1101000 104 h
㑣 13411 1100011 99 c

〷 12343 11000000110111
======= total 14 bit =======
〷 12343 1100000 96 `
〷 12343 0110111 55 7

㘰 13872 11011000110000
======= total 14 bit =======
㘰 13872 1101100 108 l
㘰 13872 0110000 48 0

摽 25725 110010001111101
======= total 15 bit =======
摽 25725 1100100 100 d
摽 25725 1111101 125 }

picoCTF{b6_bits_instf4d_of_8_0hc`7l0d} 
```

terlihat masalahnya ada di total 14 bitnya. tapi salah satu char ada yang bisa terbaca yaitu di

```
㌴ 13108 11001100110100
======= total 14 bit =======
㌴ 13108 1100110 102 f
㌴ 13108 0110100 52 4
```

yang jika digabung dengan karakter sebelumnya membentuk kata "inst34d" itu dari perhitungan ini:

```
char 3
char 4

int 3 = 51
int 4 = 52

shift_3 = 51 << 8 = 13056
4 = 4 = 52

enc = 13056 + 52

enc = 13108

㌴ 13108 11001100110100
======= total 14 bit =======
㌴ 13108 1100110 102 f
㌴ 13108 110100 52 4

1100110   0110100
1100110	   110100

0110011 + 0110100

0110011 = 3 = 51
1100110 = f = 102

0110100 = 4 = 52
1101000 = h = 104

```

di sini aku mencoba menebak antara ascii: 3, e, a dan 4. dari situ ditemukan kalau 8 bit karakter pertama itu bergeser sebanyak 1 ke kanan dari hasil sekarang. jika dikelompokkan maka hasilnya seperti ini

```
ㄶ 12598 11000100110110
======= total 14 bit =======
ㄶ 12598 1100010 98 b -> 00110001 = 1
ㄶ 12598 0110110 54 6

㌴ 13108 11001100110100
======= total 14 bit =======
㌴ 13108 1100110 102 f -> 00110011 = 3
㌴ 13108 0110100 52 4

㑣 13411 1101000 1100011
======= total 14 bit =======
㑣 13411 1101000 104 h -> 00110100 = 4
㑣 13411 1100011 99 c

〷 12343 11000000110111
======= total 14 bit =======
〷 12343 1100000 96 ` -> 00110000 = 0
〷 12343 0110111 55 7

㘰 13872 11011000110000
======= total 14 bit =======
㘰 13872 1101100 108 l -> 00110110 = 6
㘰 13872 0110000 48 0

```
dan hasil flagnya: **picoCTF{16_bits_inst34d_of_8_04c0760d}**

sebenarnya ada satu cara lagi dengan memanfaatkan hint yang ada yaitu kamu perlu menggunakan tools online di: https://dencode.com

<img width="1222" height="582" alt="image" src="https://github.com/user-attachments/assets/fc03ccbe-5248-4e62-93e8-3d50458f0e71" />

copy hasil enkripsi dan ubah ke UTF-16 lalu cek bagian Quoted-printable: **picoCTF{16_bits_inst34d_of_8_04c0760d}**
