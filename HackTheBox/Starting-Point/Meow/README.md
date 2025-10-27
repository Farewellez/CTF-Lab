## Machine Name: Meow
### Level: Very Easy

<img width="1913" height="937" alt="image" src="https://github.com/user-attachments/assets/c547a359-8e8d-4932-983c-654f74cad809" />

Jadi di awal, akan diminta untuk memilih menghidupkan Machine Lab menggunakan PWNbox atau OpenVPN. Disini aku mencoba menggunakan OpenVPN. Jika sudah selesai download file VPN nya bisa menggunakan perintah openvpn
```
root@LAPTOP-B49Q3K5D:/mnt/d/APALAH/CYSEC/VPN_HTB# ls
starting_point_w4llnut.ovpn
root@LAPTOP-B49Q3K5D:/mnt/d/APALAH/CYSEC/VPN_HTB# sudo openvpn starting_point_w4llnut.ovpn
```
Sesuaikan dengan nama file vpn yang didownload. Jika sudah terkoneksi, maka akan muncul IP Address dan bisa langsung coba spawn machine
<br>
<p align="center">
<img width="550" height="892" alt="image" src="https://github.com/user-attachments/assets/0ce1fd12-0d90-46d9-8ec9-925a0821e80f" />
</p>

### Task1: What does the acronym VM stand for?
Sepertinya ini mudah, jawabannya Virtual Box. Bagi yang belum tahu tentang VM bisa dicari di google tentang VM dan cara menggunakannya

### Task2: What tool do we use to interact with the operating system in order to issue commands via the command line, such as the one to start our VPN connection? It's also known as a console or shell.
Jawabannya terminal, atau tools yang sering dipakai untuk berinteraksi langsung dengan sistem via command line

### Task3: What service do we use to form our VPN connection into HTB labs?
Jawabannya, OpenVPN

### Task4: What tool do we use to test our connection to the target with an ICMP echo request?
Jawabannya, ping. Bisa dicoba untuk melakukan ping ke dns server milik google atau mungkin jika menggunakan wifi bisa coba ping ke gateway router masing-masing

### Task5: What is the name of the most common tool for finding open ports on a target?
Disini adalah tools yang akan kita coba di next task, yakni nmap

### Task6: What service do we identify on port 23/tcp during our scans?
Untuk ini kita perlu cek di port 23 ini service apa yang terlihat. Bisa langsung coba gunakan nmap di terminal
<img width="1045" height="264" alt="image" src="https://github.com/user-attachments/assets/ed9bb45f-29aa-4490-ba20-ded6bc43cdbb" />

Untuk melihat informasi option dari nmap, bisa langsung coba ketik nmap dan enter maka akan diperlihatkan beberapa opsi yang ada. -Sf disini untuk melihat port yang terbuka dan melihat service yang ada. Didapat port yang terbuka ada di port 23 dengan service telnet
<br> Jadi jawabannya adalah Telnet

### Task7: What username is able to log into the target over telnet with a blank password?
User dengan hak akses tertinggi yang bisa masuk tanpa password sendiri itu biasanya adalah root, jadi jawabannya root

### Task8: Submit root flag
Disini karena username yang bisa login ke telnet dengan blank password adalah root, jadi coba saja menggunakan opsi -l di telnet <br>
Dan nanti setelah command opsi -l dan username root, maka kita sudah berhasil masuk ke sistem tersebut 
<img width="753" height="677" alt="image" src="https://github.com/user-attachments/assets/c84c261d-317f-4908-8b2a-1a63cdd84edd" />

Dari situ kita coba cek ada apa saja di sistemnya
```
root@Meow:~# ls
flag.txt  snap
root@Meow:~# cat flag.txt
b40abdfe23665f766f9c61ecba8a4c19
root@Meow:~#
```
Dan berhasil dapat flagnya: **b40abdfe23665f766f9c61ecba8a4c19**
