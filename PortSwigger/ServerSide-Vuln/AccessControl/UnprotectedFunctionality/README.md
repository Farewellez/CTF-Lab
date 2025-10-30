<img width="1020" height="411" alt="UnprotectedFunc1" src="https://github.com/user-attachments/assets/d9d2e87f-7e95-402e-920b-c8d5b38870a0" />

Nama lab ini adalah unprotected functionality. Jika diartikan mungkin artinya adalah sebuah fungsionalitas yang tidak ter-proteksi. Masih dengan tipe pentesting **_grey box_**, disini diberitahu kalau lab ini mempunyai admin panel yang tidak terproteksi. Artinya apa, kita hanya perlu mencari dimana rute url untuk admin panel tersebut.

<img width="1918" height="938" alt="UnprotectedFunc2" src="https://github.com/user-attachments/assets/0269e83b-af98-4be4-ac0e-2df44cdc006f" />

Disini menggunakan robots.txt sangat membantu. Terdapat tulisan

```
User-agent: *
Disallow: /administrator-panel
```

_User-agent: *_ ditujukan untuk robot mesin pencari seperti google-bot atau bingbot <br>
_Disallow: /administrator-panel_ artinya menyuruh robot pencari ini untuk tidak melakukan indexing ke halaman ini. Namun tentu untuk kita manusia atau _hacker_ ini informasi berharga dalam tahap _recon_. Artinya ada sebuah halaman dengan nama **administrator-panel yang seharusnya dijaga atau terdapat proteksi didalamnya**.

<img width="1918" height="938" alt="UnprotectedFunc3" src="https://github.com/user-attachments/assets/00e0ab4f-3cf8-4f29-8af9-b0865e66beb3" />

Dan benar saja ketika di akses, tidak ada autentikasi siapa saja yang sedang melakukan akses ke panel admin. Dari sini kita juga bisa melakukan delete terhadap beberapa akun yang juga merupakan kerentanan _privilege escalation_ yang mana kita bisa melakukan aksi yang hanya bisa dilakukan oleh admin.

<img width="1918" height="938" alt="UnprotectedFunc4" src="https://github.com/user-attachments/assets/4836a768-1273-427d-a406-dde62792cd71" />

Sebenarnya untuk solving lab ini hanya perlu menghapus user carlos, namun karena penasaran apa jadinya jika menghapus semua user, ternyata tetap dan sama saja lab akan ter-solved.
