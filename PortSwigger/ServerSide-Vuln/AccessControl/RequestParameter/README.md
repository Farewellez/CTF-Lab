<img width="1020" height="445" alt="ParamRequest" src="https://github.com/user-attachments/assets/ee9cb225-8174-465c-bb20-edd183a9e157" />

Di lab ini, kita diberi clue bahwa ada sebuah kerentanan yang dari informasinya terletak di bagian **cookies**. Kita diberitahu juga kalau admin panel ada di rute /admin. Namun sepertinya tidak bisa langsung masuk jika bukan admin. Karena itu kita **diberi user bernama wiener dengan password peter**.

<img width="1918" height="938" alt="ParamRequest1" src="https://github.com/user-attachments/assets/02589697-c5bf-4b51-ad26-72238a5e5395" />

Setelah masuk kita terlihat mengirim data login dengan method POST ke server dengan user wiener. Disini kita juga mendapat sesi kita di cookies **"r6eJuJkoRJQ2JMo9bEh9DepIreGioxsJ"**

<img width="1918" height="938" alt="ParamRequest3" src="https://github.com/user-attachments/assets/d1a8482c-42b4-469d-a757-bf221dacfd6b" />

Tapi, kerentanan disini adalah, Request dengan method GET yang kita dapat (_halaman wiener disini_) dalam headernya terdapat informasi tambahan. Bukan hanya sesi cookies namun juga **admin=false**. Alhasil kita bisa mengubah request GET ini menjadi **admin=true**.

<img width="1918" height="938" alt="ParamRequest7" src="https://github.com/user-attachments/assets/d8aaf484-3111-44e6-9197-e98d050a97e0" />

Di tab storage di browser developer tools, cari bagian cookies. Disitu hanya perlu ubah value yang awalnya **false** menjadi **true**. Setelah itu refresh halaman dan link baru ke **Admin Panel** akan muncul.

<img width="1918" height="938" alt="ParamRequest8" src="https://github.com/user-attachments/assets/ec5abb23-584e-4a66-9390-ca1a41fc61cd" />

Dari situ kita bisa hapus beberapa user, untuk disini carlos. Setelah itu lab berhasil di solve. Selain menggunakan developer tools, disini aku bisa menggunakan **curl** di terminal linux.

```
Command untuk akses ke admin panel
┌──(w4llnut_07㉿kali)-[~]
└─$ curl "https://0a4500210335084280488030004f0058.web-security-academy.net/my-account" -b "session=r6eJuJkoRJQ2JMo9bEh9DepIreGioxsJ; Admin=true"

Command untuk akses admin panel sekaligus hapus user (karena carlos sudah terhapus, disini coba hapus wiener)
┌──(w4llnut_07㉿kali)-[~]
└─$ curl "https://0a4500210335084280488030004f0058.web-security-academy.net/admin/delete?username=wiener" -b "session=r6eJuJkoRJQ2JMo9bEh9DepIreGioxsJ; Admin=true" 
```

Refresh Halaman dan akun wiener akan hilang
<img width="1918" height="938" alt="ParamRequest9" src="https://github.com/user-attachments/assets/474686e7-6f2e-4159-bed5-48ac55cf970c" />


