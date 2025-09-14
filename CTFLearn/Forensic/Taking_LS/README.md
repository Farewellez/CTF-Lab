## Nama Chall: Taking LS 
## Level: Easy
## Author: alexkato29

Just take the Ls. Check out this zip file and I be the flag will remain hidden. https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## Write-Up
1. Disini jika mencoba langsung lihat pdf maka akan diminta passwordnya <br>
2. Jika melihat di folder sebelah ada sebuah folder yang menarik. Coba minta gemini untuk menjelaskan :3 <br>
<img width="937" height="377" alt="image" src="https://github.com/user-attachments/assets/d7c3b628-a6a2-42a9-aee6-8dcfb54dd515" /> 
3. Tidak terlalu berharga, jadi coba saja ketik ini untuk opsi tampilkan semua file/folder tersembunyi <br>

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/CTFLearn/Forensic/Taking_LS]
└─$ ls -la __MACOSX/The\ Flag
total 20
drwxrwxr-x 2 w4llnut_07 kali 4096 Sep 15 01:51  .
drwxrwxr-x 3 w4llnut_07 kali 4096 Oct 30  2016  ..
-rw-r--r-- 1 w4llnut_07 kali  120 Oct 30  2016  ._.DS_Store
-rw-r--r-- 1 w4llnut_07 kali  177 Oct 30  2016 '._The Flag.pdf'
-rw-r--r-- 1 w4llnut_07 kali  177 Sep 15 01:51  The_Flag.pdf
```

Ada sebuah folder tersembunyi yang bisa di cek, kemungkinan passwordnya juga disembunyikan <br>
4. Coba saja lakukan hal yang sama ke folder The Flag <br>

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/CTFLearn/Forensic/Taking_LS]
└─$ ls -la 'The Flag'
total 44
drwxr-xr-x 3 w4llnut_07 kali  4096 Sep 15 02:17  .
drwxr-xr-x 4 w4llnut_07 kali  4096 Sep 15 02:01  ..
-rw-r--r-- 1 w4llnut_07 kali  6148 Oct 30  2016  .DS_Store
-rw-r--r-- 1 w4llnut_07 kali 16647 Oct 30  2016 'The Flag.pdf'
drwxr-xr-x 2 w4llnut_07 kali  4096 Oct 30  2016  .ThePassword
```

Ada folder tersembunyi yang dinamakan .ThePassword, ini bisa dicek <br>
5. Langsung gunakan cd dan masuk ke folder itu <br>

```
┌──(w4llnut_07㉿kali)-[~/…/CTFLearn/Forensic/Taking_LS/The Flag]
└─$ cd .ThePassword         
┌──(w4llnut_07㉿kali)-[~/…/Forensic/Taking_LS/The Flag/.ThePassword]
└─$ ls    
ThePassword.txt                                                                                                                                                                                                   
┌──(w4llnut_07㉿kali)-[~/…/Forensic/Taking_LS/The Flag/.ThePassword]
└─$ cat ThePassword.txt                            
Nice Job!  The Password is "Im The Flag".
```

Ketemu passwordnya jadi tinggal input saja ke pdf <br>
6. Disini aku menggunakan libre office dari linux untuk membukanya <br>
<img width="1818" height="841" alt="image" src="https://github.com/user-attachments/assets/f86783da-1a2c-4c88-b080-960bd6e86b3d" />

## ABCTF{T3Rm1n4l_is_C00l}
