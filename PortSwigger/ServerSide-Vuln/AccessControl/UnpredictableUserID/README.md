<img width="1168" height="593" alt="image" src="https://github.com/user-attachments/assets/d0cd0221-0797-4999-97bb-fab61fb58c01" />

Jadi pada lab kali ini, disebutkan kalau dia memiliki sebuah kerentanan IDOR (Insecure Direct Object Reference). Kerentanan ini memiliki dampak **Horizontal Privilege Escalation**. Tujuan dari kita sebagai pentester adalah mencoba memanfaatkan dampak dari celah ini untuk mencuri API Key dari user lain bernama **Carlos**.

<img width="1918" height="938" alt="step-3" src="https://github.com/user-attachments/assets/628be687-6b95-480d-a108-81a0bb463bb3" />

Setelah selesai login dengan akun yang diberikkan oleh lab, kita bisa cek url yang merupakan Guid milik kita. Jika kita bisa menemukan Guid milik carlos, maka kita bisa masuk ke dalam akunnya dengan memanfaatkan celah IDOR. Cara menemukan Guid dari user Carlos sendiri adalah dengan cek postingan dari user-user yang upload beberapa artikel di blog mereka. Kita cukup cari nama pengguna dengan nama carlos dan kunjungi blognya maka Guid dari Carlos akan muncul di Query Parameter di Url browser. Copy Guidnya lalu pindahkan ke panel akun kita, maka kita bisa bypass login untuk akun Carlos

<img width="1918" height="938" alt="step-4" src="https://github.com/user-attachments/assets/4312f2db-0ae9-42c5-a2c2-ed5850620a17" />

Seperti terlihat dampak dari kerentanan IDOR dengan manipulasi query parameter yang berisi user yang tidak terprediksi. Tinggal submit API-Key dair Carlos dan Lab akhirnya terselesaikan.

<img width="1918" height="938" alt="step-5" src="https://github.com/user-attachments/assets/2f88233b-7fd6-4c19-b83d-43d0f0e46d20" />
