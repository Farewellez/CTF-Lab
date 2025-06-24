# 🧠 What Does a Security Analyst Do? – Hacker’s Summary

## 🔍 Peran Utama

Security Analyst adalah **garda depan pertahanan siber** organisasi. Tugas mereka adalah **mendeteksi, menganalisis, merespon, dan mencegah serangan** yang dapat mengganggu sistem dan data organisasi.

Alih-alih hanya duduk menatap dashboard, Security Analyst berperan aktif dalam memahami logika serangan, membedakan false positive, dan memerangi ancaman real-time.


## ⚔️ Tanggung Jawab Inti

1. **Monitoring & Detection**

   * Memantau alert keamanan dari tools seperti SIEM dan EDR.
   * Menelusuri aktivitas mencurigakan dalam log, network, endpoint, email, dsb.

2. **Incident Response**

   * Menentukan apakah alert merupakan false/true positive.
   * Menjalankan proses triage dan investigasi awal.
   * Jika serius → *escalate* ke Level 2 Analyst.

3. **Reporting & Documentation**

   * Membuat laporan insiden, rekomendasi teknis, dan memperbaiki SOP.
   * Berkomunikasi lintas tim (IT, DevOps, Management).

4. **Threat Research & Correlation**

   * Menggabungkan informasi dari berbagai sumber (web proxy, firewall, EDR, logs).
   * Membangun *timeline* serangan → pahami pola serangan.

5. **Security Planning**

   * Berkontribusi dalam pengembangan kebijakan keamanan.
   * Mengkaji tren ancaman dan teknik eksploitasi terbaru.


## 🧱 Level dan Jalur Karier

Security Analyst biasanya dibagi menjadi 3 level:

* **Level 1 (Triage/Entry-Level)**
  Deteksi awal, penyaringan alert, penanganan insiden ringan.

* **Level 2 (Incident Responder)**
  Penanganan insiden kompleks, malware analysis, forensik.

* **Level 3 (Threat Hunter)**
  Deteksi proaktif, *advanced adversary emulation*, mengembangkan signature/rule baru.

Jalur karier:
→ SOC Engineer → Threat Intel Analyst → SOC Manager → CISO (Chief Information Security Officer)


## 🛠️ Tools & Frameworks yang Digunakan

* **SIEM**: Splunk, QRadar, ELK Stack
* **EDR**: CrowdStrike, SentinelOne, Microsoft Defender
* **SOAR**: Cortex XSOAR, Splunk SOAR
* **Frameworks**: MITRE ATT\&CK, Cyber Kill Chain


## 🧠 Skill yang Diperlukan

### 🧬 Teknis

* TCP/IP, DNS, HTTP
* Linux & Windows basics
* Log analysis & network packet inspection
* Familiar dengan tools: Wireshark, sysmon, osquery, PowerShell/Bash scripting

### 🧠 Non-Teknis (Soft Skills)

* Critical thinking
* Curiosity (hacker mindset)
* Detail-oriented
* Mental tahan stres (alert fatigue is real)

## 📚 Learning Path di TryHackMe

### Untuk Pemula:

1. **Pre-Security** – Pengenalan IT dan cybersecurity.
2. **Cyber Security 101** – Dasar networking, OS, web, dan serangan.

### Untuk Calon Analyst:

3. **SOC Level 1** – Simulasi dunia nyata sebagai Level 1 Analyst.
4. **SOC Level 2** (opsional lanjutan) – Threat hunting, malware analysis.


## 🧪 Pengalaman Praktikal

* Bikin home lab (VM, SIEM, firewall rules).
* CTF (Capture The Flag) – defensive/offensive.
* Praktik analisa phishing, brute force, malware log, dll.
* Setup dan tuning detection rule → kurangi false positive.


## 📈 Salary & Perjalanan

* Gaji bervariasi tergantung wilayah dan level.
* Di UK:

  * L1 Analyst: £31,000 - £37,000 (\~\$40k - \$69k)
  * L2+: £40,000+
* Banyak peluang promosi & kerja remote.


## 🧭 Tips dari Dunia Nyata

Dari Isaiah (mantan SOC Analyst, sekarang Offensive Engineer di US):

> “Mulailah dengan rasa ingin tahu. Latih diri untuk membaca banyak hal, dan validasi dengan praktik. Jangan takut salah — yang penting terus belajar dan terbuka.”


## 📌 Kesimpulan

Security Analyst adalah role penting bagi siapa pun yang ingin **memahami cara kerja sistem, logika serangan, dan pertahanan digital secara mendalam**. Ini adalah **fondasi yang kuat untuk menjadi hacker, threat hunter, atau offensive engineer** di masa depan.
