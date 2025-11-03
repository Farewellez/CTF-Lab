<img width="1020" height="438" alt="Unpredict1" src="https://github.com/user-attachments/assets/6c9b8914-c2ab-4656-b383-0cccc9e6fd28" />

Nama lab ini adalah Unprotected admin functionality with unpredictable URL. Dari nama lab, sudah diberi clue kalau web fungsionalitas admin di dalam web ini memiliki sebuah kerentanan. Artinya admin panel ada, namun kemungkinan disembunyikan oleh script tertentu. Karena itu kita bisa cek **_DOM Html_** dengan inspect halaman, atau kita lihat raw code nya dengan ctrl+u (_di firefox, mungkin bisa berbeda di browser lain_).

<img width="628" height="311" alt="Unpredict4" src="https://github.com/user-attachments/assets/aec8aea2-6ecd-42f5-aadb-d94b91d5b21f" />

Dan benar, di dalam DOM html nya terdapat script js yang menyimpan logic tampilan. Seharusnya script js seperti ini tidak boleh terlihat oleh user biasa **atau** tidak boleh sembarangan menaruh logic access ke admin didalam script js seperti ini. Setelah tau celahnya sebenarnya aku menemukan baru dua cara untuk melakukan eksekusi lab ini.

<img width="1918" height="938" alt="Unpredict5" src="https://github.com/user-attachments/assets/8928417f-b593-43e2-8f51-a8386845744b" />

Pertama dengan _mengcopy-paste_ script js yang ditemukan tadi ke console di developer setting di browser lalu mengubah variable **_isAdmin_** menjadi true. Ini akan membuat sebuah link baru dengan text **_Admin Panel_** muncul. Dari situ coba akses link nya.

<img width="1918" height="298" alt="Unpredict7" src="https://github.com/user-attachments/assets/26fdb022-a9ae-44a0-976e-8d57585c1064" />

Atau cara kedua dengan langsung akses request URL ke halaman tersebut. Disini nama admin panelnya disembunyikan dengan nama **_admin-haq2ze_**.

<img width="1918" height="938" alt="Unpredict6" src="https://github.com/user-attachments/assets/71978fdc-85f1-46e0-a79a-454f26b0106c" />

Dari kedua cara tersebut, keduanya akan langsung mengakses halaman admin panel dan darisitu untuk solve lab bisa coba hapus user bernama carlos. 

<img width="1918" height="938" alt="Unpredict8" src="https://github.com/user-attachments/assets/5d130d75-3e73-4e3e-ae68-e6728662bdea" />

