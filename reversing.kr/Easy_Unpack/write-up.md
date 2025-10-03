### Point: 100
## Write-up
1. Jadi ketika mendownload file nya maka di awal kita akan mendapat file zip. Coba unzip filenya dan akan terlihat ada dua file
```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Unpack]
└─$ ls
Easy_UnpackMe.exe  Easy_UnpackMe.zip  ReadMe.txt
```
Dari sini terlihat ada sebuah file txt yang bisa kita cek
```
cat ReadMe.txt
ReversingKr UnpackMe


Find the OEP

ex) 00401000
```
Isinya adalah permintaan soal untuk mencari OEP yang merupakan Original Entry Point dari program tersebut

2. Coba cek detail file ini lebih lanjut dengan file command (konteks saat ini aku menggunakan OS linux)
```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Unpack]
└─$ file Easy_UnpackMe.exe
Easy_UnpackMe.exe: PE32 executable for MS Windows 4.00 (GUI), Intel i386, 5 sections
```
Terlihat kalau ini adalah file PE32, artinya ini adalah sebuah Portable Executable untuk Windows. Dari sini maka kemungkinan perlu dilanjutkan analisis ke OS Windows

3. Aku berpindah ke OS Windows 10 di VM. Dengan menggunakan tools DetectItEasy maka akan terlihat lebih detail lagi informasi tentang file PE ini
<img width="722" height="531" alt="image" src="https://github.com/user-attachments/assets/58465687-e6b3-4f02-be56-ae6d515a723c" />

Dari gambar terlihat kalau file tersebut adalah file adalah sebuah PE32 dengan proteksi packer yaitu UPX. Artinya OEP yang diminta soal nanti itu bukan OEP program asli. Olehkarena itu kita harus mencari kode mana yang merupakan program asli <br>
Untuk proses manual unpack sebuah packer bisa di cek disini: <br>
https://yoshlsec.github.io/manuallyupx/

4. Jika dicek, EIP berada seperti pada gambar dibawah
<img width="1007" height="347" alt="image" src="https://github.com/user-attachments/assets/f204a2ab-84de-429f-826b-69abe23c454b" />

Ini bukanlah entry point program asli, melainkan sebuah packed program atau program yang dipack oleh UPX. Setelah membaca cara kerja packer di link yang tadi disebut, kita tau tugas selanjutnya adalah mencari program asli yang telah didekripsi dan diunpack oleh stub

5. Gunakan F8 untuk terus untuk melakukan step-over
<img width="1027" height="592" alt="image" src="https://github.com/user-attachments/assets/209aa4b6-0a04-403f-ae31-a7b5e2928e26" />

Teruskan hingga menemukan pola looping dan sebuah code seperti
```
0040A09B | 74 26                    | je easy_unpackme.40A0C3                 |
```

Arti dari looping tersebut, stub dalam packer masih mendekripsi dan melakukan dekompresi dari file yang sudah di enkripsi dan dikompres oleh ppacker. Dalam hal ini set breakpoint tepat setelah looping berakhir dengan F2 seperti titik merah pada gambar diatas

6. Di beberapa jalan lain pasti akan beberapa looping lagi dan hanya perlu set breakpoint ke luar loop, tapi ingat setelah keluar loop tersebut gunakan F8 untuk step over dan F9 ketika di daerah looping untuk step into
<img width="1032" height="582" alt="image" src="https://github.com/user-attachments/assets/85733bb2-5a47-4044-965c-af98d4143d59" />


7. Titik krusial berada di 3 alamat ini
<img width="1031" height="362" alt="image" src="https://github.com/user-attachments/assets/2a56d32a-470c-4d67-b44b-3cf323bcd242" />

Di alamat ini hingga beberapa looping lagi perlu beberapa kali F8 dan F9 hingga ke loop terakhir

8. Setelah loop terakhir dan dirasa sudah tidak akan jump ke looping lagi maka gunakan F8, jangan F9
<img width="1012" height="340" alt="image" src="https://github.com/user-attachments/assets/bb069d65-fb01-4474-af94-f5a1db53a546" />

Maka akan terlempar ke kode dan alamat seperti di gambar itu. Dengan ciri khas entry point di assembly bisa disimpulkan ini adalah OEP program dan bisa langsung disubmit

#### 00401150
