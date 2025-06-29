# JinjaCare [Web]
Jinjacare is a web application designed to help citizens manage and access their COVID-19 vaccination records. The platform allows users to store their vaccination history and generate digital certificates. They've asked you to hunt for any potential security issues in their application and retrieve the flag stored in their site.

### 📝 Related Bug Bounty Reports
- Bug Report #1 - <a href="https://hackerone.com/reports/125980">RCE via SSTI</a>
- Bug Report #2 - <a href="https://hackerone.com/reports/1104349">SSTI</a>

## Write-up step-by step
### Step 1
Pertama aku mencoba untuk masuk ke web yang akan muncul ip-address dan port nya ketika spawn docker

### Step 2
Ketika sudah masuk, maka akan diminta untuk melakukan login apabila sudah memiliki akun. Dari sini, karena nama challengenya adalah Jinja, aku mencoba mencari tahu bahasa apa yang digunakan untuk membuat web ini. Jinja berhubungan dengan python, dari situ aku mencoba memperkuat
 dengan melihat contoh bug report yang diberikan. Di kedua report itu ada dari orange untuk uber dan battle_angle untuk glovo. Dari kedua report diberikan contoh percobaan exploitasi yang mungkin, yaitu SSTI dan RCE. 
 Dari keduanya bisa dipastikan challenge ini kemungkinan menggunakan cara itu. 

### Step 3
Aku mencoba menuliskan {{"7"*7}} ke input nama di log-in dan pembuatan akun baru, tapi keduanya gagal. Untuk password masih diperbolehkan

### Step 4
Karena gagal, akhirnya aku mencoba membuat akun biasa dan login tanpa ada karakter aneh di input. Ketika sudah masuk, di fitur profil kita bisa mengedit nama kita dan ketika di save ternyata lulus autentikasi.

### Step 5
Aku mencoba menuliskan hal yang sama namun kali ini {{"7"*7}} ku tulis di edit profil dan benar ternyata lulus. Namun masalahnya aku tidak tahu apakah ini benar-benar berhasil untuk mencetak string "7" sebanyak 7 kali.

### Step 6
Akhirnya aku mencoba explore lagi dan ternyata ada fitur untuk cetak sertifikat semacam penghargaan karena sudah vaksin mungkin. Ketika dicetak dalam bentuk pdf ternyata namaku berubah menjadi string "7" sebanyak 7  kali seperti ini:
![Screenshot 2025-06-29 180347](https://github.com/user-attachments/assets/bad2a1e3-32ef-4e56-aa97-724f9310db2e)

Itu artinya SSTI berhasil, kemungkinan serangan selanjutnya merujuk ke RCE.

### Step 7
Akhirnya aku mencoba menggali lebih dalam dengan mencoba inject command: {{ ''.__class__.mro()[1].__subclasses__() }}
Untuk mengeksplorasi lebih banyak objek python.

### Step 8
Dari command yang diinject itu akan muncul banyak seperti ini:
![image](https://github.com/user-attachments/assets/ce2fcf14-c8e5-43c8-8e87-0b6ca8c798ec)

Tujuan utama adalah mencari subprocess.Popen itu ada di index ke berapa agar nanti bisa meng-execute command shell

### Step 9
Disini aku menggunakan pencarian pdf biasa untuk menemukan subprocess.Popen dan aku menemukan di index ke-159
![image](https://github.com/user-attachments/assets/7769f939-e332-4788-b849-72dba143a32c)

### Step 10
Dari situ langsung saja jalankan command via RCE:
{{ ''.__class__.mro()[1].__subclasses__()[159].__init__.__globals__['os'].popen('ls /').read() }} 

dari sini akan terlihat isi dari directory root "/"

### Step 11
Dari situ muncul beberapa directory sekaligus flag yang ada
![image](https://github.com/user-attachments/assets/b3d4b279-e436-4eb7-bc8e-4af33e6a40ce)

### Step 12
Gunakan command "cat" untuk membaca flag nya:
{{ ''.__class__.mro()[1].__subclasses__()[159].__init__.__globals__['os'].popen('cat /flag.txt').read() }}
![WhatsApp Image 2025-06-29 at 17 11 45_1011c421](https://github.com/user-attachments/assets/2c45ae29-268f-4918-bc8c-bf3dcf695b33)



