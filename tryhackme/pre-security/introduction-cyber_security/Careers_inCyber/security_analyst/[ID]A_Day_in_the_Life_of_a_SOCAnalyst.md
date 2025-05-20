# A Day in the Life of a SOC Analyst (Bahasa Indonesia)

Karier sebagai Analis Pusat Operasi Keamanan (SOC Analyst) menawarkan banyak keuntungan dan pengalaman yang dinamis, di mana hampir tidak ada dua hari yang sama. SOC Analyst berada di garis depan dalam mempertahankan organisasi dari serangan siber dan memiliki peran signifikan dalam menjalankan operasi keamanan. Artikel ini menggambarkan rutinitas harian dan tanggung jawab dari seorang SOC Analyst, berdasarkan wawancara dengan Isaiah, seorang mantan SOC Analyst yang kini bekerja sebagai Senior Offensive Security Engineer sekaligus Content Engineer paruh waktu di TryHackMe.


## Seperti Apa Hari-Hari Seorang SOC Analyst?

Hari kerja seorang SOC Analyst biasanya dimulai dengan meninjau dashboard dari berbagai alat monitoring keamanan. Tujuan awal ini adalah untuk mencari aktivitas mencurigakan atau anomali dalam log yang dikumpulkan dari sistem-sistem yang diamankan.

### Tanggung Jawab Harian:

* Meninjau dan menyelidiki peringatan (alerts) yang dihasilkan oleh aturan deteksi
* Mengidentifikasi false positives dan melakukan penyempurnaan terhadap aturan
* Membuat laporan keamanan
* Menjaga agar dashboard tetap bersih sebelum shift berakhir, atau menyerahkan investigasi yang belum selesai ke tim berikutnya

## Apa yang Terjadi Saat Sebuah Alert Dikenali?

Tujuan utama dari seorang SOC Analyst adalah memastikan operasional bisnis tetap berjalan tanpa gangguan. Ketika sebuah alert ditemukan, langkah yang dilakukan adalah:

1. **Identifikasi pemicu**: Cari tahu apa yang menyebabkan alert muncul
2. **Tentukan asal dan alasan**: Lihat dari mana alert itu berasal dan mengapa
3. **Tindakan sesuai playbook**: Mengikuti prosedur yang sudah ditetapkan dalam playbook SOC
4. **Korelasikan data** dari sumber-sumber seperti web proxy, EDR (Endpoint Detection & Response), SIEM, dan endpoint
5. **Analisis log dan susun timeline**: Ini penting untuk menentukan apakah alert benar (true positive) atau hanya aktivitas biasa (false positive)

Jika ternyata alert adalah false positive, maka dilakukan tuning ulang terhadap aturan agar mengurangi "noise". Jika ternyata benar-benar serangan, seperti phishing, maka SOC Analyst akan bekerja sama dengan stakeholder dan melakukan respon sesuai SOP.

## Pengalaman Nyata Seorang SOC Analyst

Isaiah membagikan bahwa selama bekerja sebagai SOC Analyst baik di MSSP (Managed Security Services Provider) maupun in-house, dia memiliki beberapa tanggung jawab utama, antara lain:

* Memantau sistem keamanan harian untuk mendeteksi aktivitas mencurigakan seperti malware dan hacking
* Investigasi tiket pengguna terkait phishing, spam, atau aktivitas mencurigakan lainnya
* Melakukan riset harian mengenai tren dan ancaman terbaru di dunia cybersecurity
* Menyesuaikan dan menyempurnakan skrip monitoring untuk mengurangi kebisingan
* Triase alert dan korelasi log perangkat
* Menjalankan prosedur Incident Response saat terjadi pelanggaran
* Melakukan threat hunting untuk mendeteksi anomali yang tidak biasa
* Menyusun laporan intelijen ancaman (threat intelligence) terkait malware dan metode penyebarannya

## Penerapan Pengalaman Nyata dalam Pelatihan

Pengalaman nyata Isaiah sebagai SOC Analyst sangat berpengaruh dalam pembuatan training room di TryHackMe. Ia menyusun materi pelatihan berdasarkan skenario nyata yang terjadi di lapangan, agar para peserta dapat memperoleh keterampilan yang relevan dan praktis.

## Saran Bagi Calon SOC Analyst

Isaiah juga memberikan beberapa saran penting:

* **Kembangkan rasa ingin tahu**: Punya sikap "Saya belum tahu sekarang, tapi akan tahu nanti"
* **Praktek langsung**: Jangan hanya membaca teori, lakukan eksperimen melalui hands-on lab
* **Rendah hati secara intelektual**: Bersedia mengakui kesalahan dan membuka diri untuk belajar dari kesalahan
* **Kuasai dasar-dasar cybersecurity**: Mulai dari jalur pembelajaran Cyber Security 101
* **Ikuti perkembangan terbaru**: Baca blog, forum, laporan bug bounty, malware analysis, dan threat intelligence
* **Bangun lab sendiri**: Instal Active Directory, jalankan website pribadi, setup SIEM, konfigurasi firewall, dan lainnya
* **Latih cara berpikir dari dua sisi**: Baik sebagai defender maupun attacker

## Jalur Pembelajaran yang Disarankan

TryHackMe menyediakan jalur pembelajaran lengkap:

1. **Cyber Security 101**: Untuk pemula yang ingin memahami dasar-dasar
2. **SOC Level 1 Pathway**: Latihan berbasis skenario nyata untuk level entry
3. **SOC Level 2 Pathway**: Untuk topik lanjutan seperti threat hunting dan malware analysis

Bagi yang ingin tantangan lebih dalam, jalur SOC Level 2 memberikan fondasi yang lebih kuat untuk menjadi analis tingkat menengah.

## Penutup

Karier sebagai SOC Analyst memberikan fondasi kuat untuk berkarier di dunia keamanan siber. Dengan kombinasi antara keterampilan teknis, pengalaman langsung, dan sikap yang terus ingin belajar, siapa pun bisa meniti jalan sukses sebagai profesional di bidang ini.

Mulailah dengan jalur pelatihan dari TryHackMe, kuasai dasar-dasar, dan terus kembangkan keterampilanmu untuk mencapai level berikutnya!

Terima kasih untuk Isaiah atas wawasan dan pengalaman berharganya!
