## Nama Chall: Easy Crack
### Point: 100

## Write-up
1. Disini tidak diberikan clue apapun terkait soal jadi perlu check jenis soal dengan file command. Untuk OS aku menggunakan linux disini
```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Crack]
└─$ file Easy_CrackMe.exe
Easy_CrackMe.exe: PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections
```
Dari situ terlihat kalau ini adalah file PE 32 bit. Untuk informasi apa itu file PE bisa cek disini <a href="https://en.wikipedia.org/wiki/Portable_Executable">File PE</a> 32 bit yang dimana ini adalah file dari operating system Windows


2. Karena ini file untuk Windows dan aku menggunakan linux, maka tidak bisa dijalankan di lingkungan saat ini
```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Crack]
└─$ ./Easy_CrackMe_cp.exe 
run-detectors: unable to find an interpreter for ./Easy_CrackMe_cp.exe
```


3. Jadi sebelum tes ke lingkungan windows, coba baca dulu isi code file dengan metode static analyst menggunakan strings
```
KERNEL32.dll
Incorrect Password
Congratulation !!
EasyCrackMe
AGR3versing
```
Di bagian bawah ternyata ada text string yang menunjukkan kondisi "Incorrect" dan "Congratulation" artinya bisa diasumsikan ini adalah aplikasi yang meminta input password yang benar

4. Langsung saja lakukan static analyst menggunakan IDA dan cari text dengan isi string "Incorrect" atau "Congratulation"
<img width="726" height="371" alt="image" src="https://github.com/user-attachments/assets/d26ca751-4c16-4e2c-80cc-fc8b7c79a754" />


5. Terlihat ada dua kondisi true dan false, coba siapa yang memanggil kondisi true. Bisa terlihat yang di mark orange
<img width="725" height="208" alt="image" src="https://github.com/user-attachments/assets/8988ec8b-1687-4ac2-88aa-38eaa8ed693f" />

6. Dari situ coba decompile dengan F5 dan masuk ke tab pseudocode
<img width="942" height="200" alt="image" src="https://github.com/user-attachments/assets/56f8dced-e501-4e9b-864e-def6bb015a3d" />


7. Dari situ terlihat bahwa function ini melakukan validasi tiap input pengguna pada index ke 0, 1, 2 dan 4 <br>
Untuk index string ke-0: 69 -> E jika di tabel ASCII <br>
Untuk index string ke-1: 97 -> a jika di tabel ASCII <br>
Untuk index string ke-2: IDA menerjemahkan ke Str2, 2u, bisa klik 2 kali pada Str2 <br>
Hasilnya adalah 5y. Ini bisa dilakukan juga pada string index ke-4 yaitu R3versing

#### Keseluruhan jika digabung maka flagnya adalah: Ea5yR3versing
