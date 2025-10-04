```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Keygen]
└─$ ls
'Easy Keygen.exe'   Easy_KeygenMe.zip   ReadMe.txt
```

2. Coba cek isi dari ReadMe.txt untuk melihat deskripsi challenge
```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/Reversing.kr/Easy_Keygen]
└─$ cat ReadMe.txt      
ReversingKr KeygenMe


Find the Name when the Serial is 5B134977135E7D13
```

Dari situ terlihat kalau kita diminta untuk mencari nama dari pemilik serial **5B134977135E7D13**

3. Karena kita tidak bisa tahu bagaimana algoritma autentikasi bekerja, maka perlu melakukan sebuah analisis baik statis maupun dinamis
<img width="728" height="530" alt="image" src="https://github.com/user-attachments/assets/edd41c7c-50f5-44f7-9a3a-b3747e443577" />

Sebenarnya ini opsional, namun mengingat ini adalah PE jadi aku gunakan DiE untuk cek apakah ada sebuah protector di dalamnya dan ternyata tidak ada

4. Langsung saja buka x32dbg karena ini adalah file PE32 atau 32-bit dan lakukan dynamic analyst karena akan terlalu lama untuk melakukan static analyst di program ini
<img width="1023" height="452" alt="image" src="https://github.com/user-attachments/assets/1e685af0-eb6d-4783-a61c-ae009cb4aeec" />

Gunakan F9 untuk step over hingga ke OEP program

5. Jika terus di F9 Maka program akan meminta sebuah input 
<img width="972" height="505" alt="image" src="https://github.com/user-attachments/assets/a9f2e9bf-97e6-42e8-9421-ded85082dc8e" />

Dari sini kita tahu bahwa ada string "Input Name: " yang bisa dicari di x32dbg dengan seach all module

6. Set breakpoint sebelum dan saat program menerima input
<img width="1008" height="347" alt="image" src="https://github.com/user-attachments/assets/cc715447-57e9-4c77-975f-094168e626e3" />

7. Geser ke bawah lagi dan akan ketemu sebuah perkondisian true and false
<img width="985" height="187" alt="image" src="https://github.com/user-attachments/assets/99fb675f-95a3-4d19-a6eb-16bdc2005cab" />

Yakni ketika correct dan ketika wrong. Dari situ bisa beri breakpoint

8. Running program atau gunakan F9 hingga menyentuh breakpoint input dan sebelum mencapai kondisi correct and wrong yakni ketika di breakpoint setelah input diterima gunakan F8 untuk step into satu persatu 
<img width="1005" height="133" alt="image" src="https://github.com/user-attachments/assets/ca6e81d5-d110-4c97-8c32-0eb11a14e66c" />

Seperti contoh gambar, kita bisa bebas input name untuk melihat logika autentikasinya bagaimana dan lanjut F8

9. Setelah diminta sebuah input nama, selanjutnya akan diminta input serial. Beri breakpoint disitu
<img width="1035" height="287" alt="image" src="https://github.com/user-attachments/assets/a4fc12ec-a4ee-4f4f-92a0-47c9955a4637" />

Input nomor serial dengan nomor serial yang sebelumnya

10. Setelah input gunakan F8 untuk step into dan coba cek bagaimana program berjalan
<img width="1020" height="368" alt="image" src="https://github.com/user-attachments/assets/69f90f8b-1899-4ca0-a156-417d9218baeb" />

Nah dari sini terlihat sebuah loop yang digunakan untuk validasi serial dengan nama yang valid. Terlihat kalau input AAA yang kita masukkan tadi berubah menjadi **516171**

11. Di chall ini ada beberapa opsi untuk memecahkan chall nya
- Menganalisis algoritma yang ada dan menulis script untuk me reverse dan mendapatkan nama yang ditarget
- Melakukan percobaan input char satu persatu dan cek validasinya

Untuk percobaan pertama, aku mencoba cara kedua karena serial key "5B134977135E7D13" itu tidak terlalu banyak. Sudah terlihat juga kalau ini adalah hexadecimal

0x5B\0x13\0x49\0x77\0x13\0x5E\0x7D\0x13 -> kurang lebih seperti itu dan kita masih belum tahu sebenarnya apa arti serial ini karena ini bukan hash artinya bisa kita decode

12. Coba input satu persatu char. Semisal ketika mencapai breakpoint pertama dan diminta input name input char ascii satu persatu dan perkirakan. Dari situ aku berhasil mendapatkan pola char 'K' itu cocok dengan 0x5B artinya kemungkinan besar 2 digit hexadecimal di serial itu merepresentasikkan 1 char nama target

13. Seperti contoh ini aku berhasil mencocokkan char 'K', '3' dan 'y' sebagai representasi 3 digit hexadecimal pada nomor serial
<img width="505" height="129" alt="image" src="https://github.com/user-attachments/assets/67c36d75-b85f-4e75-b7d5-9a52fa8b5cba" />

Jika diulang terus langkahnya hingga ke char terakhir didapat kalau name target adalah: **K3yg3nm3** 

## Opsional
Karena kita sudah tahu jawaban dari chall ini adalah **K3yg3nm3** kita bisa coba menduplikasi keygen yang dibuat program ini <br>
<img width="1212" height="518" alt="image" src="https://github.com/user-attachments/assets/84900e9b-703f-4313-a0d0-0463fc7c980e" />

Itu adalah hasil decompile file yang dibuat di IDA. Dari sini aku coba minta bantuan AI untuk cek algortimanya dan membuat sebuah script python untuk check saja
```
# Kunci 3-byte yang kita temukan dari assembly
KEY = [0x10, 0x20, 0x30]

def generate_serial(name: str) -> str:
    """
    Fungsi ini mereplikasi algoritma keygen untuk menghasilkan serial dari nama.
    """
    serial = ""
    for i, char in enumerate(name):
        # Operasi XOR dengan kunci yang berulang
        key_byte = KEY[i % len(KEY)]
        encrypted_char = ord(char) ^ key_byte
        
        # Format menjadi 2 digit Heksadesimal dan gabungkan
        serial += f"{encrypted_char:02X}"
        
    return serial

def find_name_from_serial(serial: str) -> str:
    """
    Fungsi ini membalikkan algoritma untuk menemukan nama dari serial.
    Ini adalah solusi untuk challenge ini.
    """
    name = ""
    # Proses serial 2 karakter sekaligus (karena format %02X)
    for i in range(0, len(serial), 2):
        # Ambil 2 karakter hex (e.g., "5B")
        hex_char = serial[i:i+2]
        
        # Konversi ke integer
        encrypted_val = int(hex_char, 16)
        
        # Dapatkan byte kunci yang sesuai
        key_byte = KEY[(i // 2) % len(KEY)]
        
        # Balikkan operasi XOR
        original_val = encrypted_val ^ key_byte
        
        # Konversi kembali ke karakter
        name += chr(original_val)
        
    return name

# --- PENGUJIAN ---

# 1. Uji coba dengan nama yang kita temukan untuk memastikan logikanya benar
test_name = "K3yg3nm3"
generated_serial = generate_serial(test_name)
print(f"Nama: {test_name}")
print(f"Serial yang dihasilkan: {generated_serial}")
print(f"Apakah serial cocok? {generated_serial == '5B134977135E7D13'}")

print("-" * 30)

# 2. Balikkan prosesnya untuk menemukan nama dari serial yang diberikan di soal
target_serial = "5B134977135E7D13"
found_name = find_name_from_serial(target_serial)
print(f"Serial target: {target_serial}")
print(f"Nama yang ditemukan: {found_name}")
```

Dari sini terbukti kalau keygennya menggunakan operasi XOR:
- Karakter pertama nama XOR 0x10
- Karakter kedua nama XOR 0x20
- Karakter ketiga nama XOR 0x30
- Karakter keempat nama XOR 0x10 (kembali ke awal)

Contoh: Jika input adalah "ABC":
- 'A' (0x41) ^ 0x10 = 0x51 -> diformat menjadi "51"
- 'B' (0x42) ^ 0x20 = 0x62 -> diformat menjadi "62"
- 'C' (0x43) ^ 0x30 = 0x73 -> diformat menjadi "73"
- Hasil akhir Buffer: "516273"
