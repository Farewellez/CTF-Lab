<img width="912" height="441" alt="step-1 (4)" src="https://github.com/user-attachments/assets/4e20ac3a-3a3f-49d8-a819-fae5f66b12c0" />

Jadi disini kita dijelaskan kerentanan yang ada di web ini yakni **Broken Access Control** yang terletak di autentikasi 2FA. Coba buka halaman akun dan masukkan kredensial user wiener (kita) seperti biasa.

<img width="1918" height="938" alt="step-3 (4)" src="https://github.com/user-attachments/assets/e99b3d38-23b2-481b-b958-3ff4cfaa2373" />

Setelah login dan berhasil maka akan diminta kode 2FA yang dikirim VIA email. Tentu kita disini bisa lihat email kita dan kita masuk ke panel akun kita.

<img width="1918" height="938" alt="step-4 (4)" src="https://github.com/user-attachments/assets/3a8adba5-c9d5-4349-80ed-dd0fead0d0eb" />

Coba lihat query parameternya. Ini adalah paremeter id dari akun kita wiener. Jika kita ganti carlos dengan harapan ada kerentanan **IDOR** lewat request parameter via user id maka tidak akan berhasil. Disini kerentanan simple IDOR nya mungkin sudah di patch.

<img width="1918" height="938" alt="step-5 (4)" src="https://github.com/user-attachments/assets/636b799d-fc33-4053-90cf-a57cd0ac6af4" />

Sekarang coba login dengan username carlos dan password yang sudah diberikan, ketika minta 2FA kita tidak punya hak akses ke email carlos. Lalu coba alih-alih berpikir mendapatkan email carlos, kita coba ubah url yang awalnya /ogin2 menjadi query parameter yang sebelumnya

<img width="1918" height="938" alt="step-6 (3)" src="https://github.com/user-attachments/assets/b0d487a0-103d-40bd-aecf-e904e4df7873" />

Contoh seperti query parameter id user milik wiener tadi, namun kita ubah ke carlos lalu cek apakah berhasil

<img width="1918" height="938" alt="step-7" src="https://github.com/user-attachments/assets/b9ef778d-26a0-4503-a6bd-cae9fdb42dea" />

Seperti yang terlihat kita berhasil masuk ke panel akun dari carloss. Dari sini ketika kita cek email, kita sudah selesai solve lab ini. Serangan lebih jauh mungkin bisa mengganti kredensial email carlos menjadi email kita sendiri untuk mengubah autentikasi akunnya.
