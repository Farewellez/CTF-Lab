## Nama Chall: I'm a dump
## Level: Easy
## Author: lancillotto

The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{*}

## Write-Up
1. Untuk pertama, cek dulu ini file apa bisa gunakan exiftool atau cukup dengan *file*

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/CTFLearn/Forensic/Iam_aDump]
└─$ file file
file: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=672d1ab79b5c1f063344be7b8edbda2219d8991d, for GNU/Linux 3.2.0, not stripped
```
Karena ini adalah shared library maka ini bukanlah file yang bisa dijalanlan seperti biasa (tau darimana kalau so? pake exiftool dan cek extensionnya). Untuk penjelasan lengkapnya aku tanya gemini :3<br>
<img width="905" height="670" alt="image" src="https://github.com/user-attachments/assets/a6441640-ba14-47d5-93c1-b6a5aa16b47f" />
2. Coba gunakan strings dan less untuk cek barangkali flagnya berupa strings

```
u3UH
CTFlearnH
{fl4ggyfH
l4g}H
[]A\A]A^A_
;*3$"
```

Ada dibagian awal, jika dibersihkan bentukannya seperti ini: <br>

CTFlearnH{fl4ggyfHl4g}H <br>

Tapi kita akan salah jika langsung submit, jika perhatikan deskripsi soal menyebutkan jika kita harus membuang beberapa karakter "removing an useless H.E.H.U.H.E. from the flag" <br>

Jika huruf itu di remove maka akan kita dapatkan flag asli:

## CTFlearn{fl4ggyfl4g}
