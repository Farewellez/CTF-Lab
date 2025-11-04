<img width="1140" height="589" alt="step-1 (3)" src="https://github.com/user-attachments/assets/cd3fbc58-41b6-416b-84f7-a6e037f80615" />

Disini kita diberitahu kalau lab ini memiliki kerentanan username enumeration dengan respons yang berbeda. Artinya tiap kali kita memberikan post username dan password maka akan ada perbedaan respons yang bisa dilihat oleh client.

<img width="1918" height="938" alt="step-2 (3)" src="https://github.com/user-attachments/assets/0e7d7301-8ff0-4ac9-9c14-7aa1d5ce719e" />

Semisal contoh disini ketika kita input sembarangan maka akan ada tulisan Invalid username. Artinya web ini secara explisit menunjukkan kalau username kita tidak valid, namun disisi lain itu berarti kita bisa mengenumerasi username lain karena kita tahu hanya username yang invalid.

<img width="1918" height="938" alt="step-3 (3)" src="https://github.com/user-attachments/assets/67793362-17db-4ab0-9bc0-8be0fe477a44" />

Dengan script yang sudah kubuat disini, ini akan mengenumerasi list usernmae yang sudah diberikan di awal. Kenapa tidak langsung menggunakan intruder di burp? karena penasaran aja pakai python hehe. Contoh hasil script ini dapat username yang valid yaitu **Root**
Ketika kita coba input username root maka sekarang ada warning kalau password kita salah atau **Incorrect password**. Dari sini kita tahu kalau root user itu ada dan sekarang hanya perlu  bruteforcing passwordnya.

<img width="1918" height="938" alt="step-5 (3)" src="https://github.com/user-attachments/assets/13594d59-1da4-4c82-9178-70b2933c1687" />

Dengan script python lainnya aku melakukan bruteforcing dengan mengirim request ke server untuk username root dan wordlist password yang sudah diberikan dan berhasil ditemukan yaitu **asdfgh** ketika coba kita submit maka lab berhasil terselesaikan.

<img width="1918" height="938" alt="step-6 (2)" src="https://github.com/user-attachments/assets/da811918-87dd-4212-bd8a-ec96e1f666a3" />

