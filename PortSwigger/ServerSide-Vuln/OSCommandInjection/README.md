<img width="918" height="312" alt="image" src="https://github.com/user-attachments/assets/469773e1-dba9-49ab-8c6a-adf35e2d7a06" />

Jadi kerentanan ini sebenarnya lebih dasar tapi sulit ditebak ketimbang RCE via file uploads sebelumnya. Jika sebelumnya kita butuh inject payloads webshell ke server, sekarang kita hanya perlu inject command os/shell ke kolom input yang disediakan web untuk dikirim ke server.


<img width="1215" height="538" alt="image" src="https://github.com/user-attachments/assets/1958aa27-d2f9-4870-b674-fc3b6552232b" />

Seperti contoh itu, kita bisa tambah pemisah ";" untuk tanda agar menyelesaikan command yang pertama kemudia eksekusi command selanjutnya. dari situ kita bisa menggunakan beberapa command dasar linux seperti whoami untuk solve lab. 
