<img width="932" height="416" alt="image" src="https://github.com/user-attachments/assets/d1efd9f2-d448-4388-b07d-84fe7f87d64c" />

Jadi di lab ini diajarkan sebuah kerentanan SSRF (Server Side Request Forgery) dengan akses ke local server. Untuk attack surface ada di bagian cek stok barang/produk yang menggunakan API Internal Service.

<img width="1622" height="847" alt="image" src="https://github.com/user-attachments/assets/66fc269d-33ab-48c4-83a5-c310822613e3" />

Semisal contoh di situ ada tombol cek stok. Pastika burpsuite menyala dan intercept on, baru klik tombol cek stoknya. Jika sudah maka akan ada informasi request seperti ini

<img width="1224" height="413" alt="image" src="https://github.com/user-attachments/assets/441ff348-7c40-4393-9b1b-b66ee0364948" />

Jika dilihat dibawah ada sebuah API yang mengarah atau fetch data dari local server. Karena kita diminta untuk request http://localhost/admin maka kita bisa inject payloads ke stockAPI ini. Namun dalam real life case ada beberapa kondisi dimana kita tidak bisa seenaknya inject localhost karena kerentanan berbeda-beda. Namun tidak ada salahnya untuk mencoba beberapa payloads. URL dari stockApi coba ganti menjadi localhost/admin maka alih-alih keluar data stok barang, yang keluar dibawah postingan tersebut adalah data html dari panel admin atau tampilan panel admin itu sendiri

<img width="1607" height="904" alt="image" src="https://github.com/user-attachments/assets/b0526096-45a2-4e3e-bd90-a5292797b06c" />

Seperti terlihat, namun kita tidak bisa langsung delete salah satu user karena interface dari admin panel ini hanya bisa diakses oleh admin atau localhost. Panel ini secara legalnya hanya bisa diakses oleh admin dengan login sebagai admin atau dengan localhost. Sedangkan di kondisi kita saat ini hanya bisa menyuruh server untuk fetch data atau mengirim request ke server internal. Disinilah kerentanan SSRF terlihat dengan request menggunakan localhost untuk akses panel admin. Jika penasaran ketika kita request dan klik delete salah satu secara langsung maka akan munculhalaman seperti ini

<img width="1882" height="714" alt="image" src="https://github.com/user-attachments/assets/8c0f8934-e5bd-4b7f-ad75-8cf3a5886844" />

Terlihat sebuah leak atau informasi bocor yang berharga **"Admin interface only available if logged in as an administrator, or if requested from loopback"** seperti yang kujelaskan sebelumnya, kita tidak bisa login sebagai admin namun bisa memanfaatkan request dari loopback atau localhost. Artinya kita bisa request untuk delete user menggunakan localhost itu sendiri via stockApi yang ada. seperti ini misal
```
stockApi=http://localhost/admin/delete?username=carlos
```
Hasilnya ketika dikirim maka seperti ini
<img width="1603" height="677" alt="image" src="https://github.com/user-attachments/assets/bcd902b9-11ee-49f5-97f7-d39f2734c5cf" />

Dan lab berhasil disolve. Jika tidak ada notif solve coba refresh halamannya.
<img width="1898" height="802" alt="image" src="https://github.com/user-attachments/assets/f48f73c8-1493-4214-8a20-5e7f004ec894" />

