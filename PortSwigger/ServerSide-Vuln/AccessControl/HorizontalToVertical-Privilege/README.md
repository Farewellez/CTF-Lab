<img width="1918" height="938" alt="step-1 (2)" src="https://github.com/user-attachments/assets/6dd9e58a-d4b7-4834-9aea-fd41453ab2c4" />

Celah yang ada di lab ini terletak pada fitur **prefilled password** yang ada pada akun pengguna ditambah **kerentanan IDOR pada query parameter id pengguna di URL**. 

<img width="1918" height="938" alt="step-2 (2)" src="https://github.com/user-attachments/assets/e5e9717e-cd5b-49ee-909c-45cd0d99b927" />

Alurnya, ketika pengguna berhasil login maka halaman akan di direct ke panel akun atau MyAccount dengan password yang langsung terisi meskipun di masked. Terlihat normal, namun ada id pada query parameter yang awalnya username pengguna, bisa kita ganti ke **administrator**.

<img width="1918" height="938" alt="step-3 (2)" src="https://github.com/user-attachments/assets/e2e2b1eb-f45d-4679-8cbd-111e95657c37" />

 Akhirnya halaman dengan prefilled password kita sekarang berubah ke password admin yang bisa kita ambil. Kita bisa log-in ulang menggunakan username administrator dengan password yang sudah kita dapatkan.

 <img width="1918" height="938" alt="step-4 (2)" src="https://github.com/user-attachments/assets/af8861ef-805f-4064-9a92-702dc3b0cc4c" />

Coba log-in dengan akun admin yang credentialnya sudah kita dapatkan. Untuk mendapatkan hak akses ke panel admin

<img width="1918" height="938" alt="step-5 (2)" src="https://github.com/user-attachments/assets/32f54a3b-28a4-4fe4-b8e9-dc668f0dcc5f" />

Dari ini kita bisa hapus user yang sesuai, misal **Carlos** untuk menyelesaikan Labnya.

<img width="1918" height="938" alt="step-6" src="https://github.com/user-attachments/assets/d09c7f03-32c6-47c1-b4ab-c8da48356b43" />

