# Practical Example of Digital Forensics
### [description]
Everything we do on our digital devices, from smartphones to computers, leaves traces. Let’s see how we can use this in the subsequent investigation.

Our cat, Gado, has been kidnapped. The kidnapper has sent us a document with their requests in MS Word Document format. We have converted the document to PDF format and extracted the image from the MS Word file for your convenience.

You can download the attached file to your local machine for inspection; however, for your convenience we have added the files to the AttackBox. To follow along, open the terminal on the AttackBox, then go to the directory /root/Rooms/introdigitalforensics as shown below. In the following terminal output, we changed to the directory containing the case files.

![image](https://github.com/user-attachments/assets/472103fc-4248-40bb-9c68-99896ea0df1f)

## [Document Metadata]
When you create a text file, TXT, some metadata gets saved by the Operating System, such as file creation date and last modification date. However, much information gets kept within the file’s metadata when you use a more advanced editor, such as MS Word. There are various ways to read the file metadata; you might open them within their official viewer/editor or use a suitable forensic tool. Note that exporting the file to other formats, such as PDF, would maintain most of the metadata of the original document, depending on the PDF writer used.

Let’s see what we can learn from the PDF file. We can try to read the metadata using the program pdfinfo. Pdfinfo displays various metadata related to a PDF file, such as title, subject, author, creator, and creation date. (The AttackBox already has pdfinfo installed; however, if you are using Kali Linux and don’t have pdfinfo installed, you can install it using sudo apt install poppler-utils.) Consider the following example of using pdfinfo DOCUMENT.pdf.
The PDF metadata clearly shows that it was created using MS Word for Office 365 on October 10, 2018.

### [Soal 1]
Using pdfinfo, find out the author of the attached PDF file, ransom-letter.pdf.

1. Gunakan pdfinfo yang merupakan tools untuk melihat metadata dari sebuah file pdf dengan lengkap
2. Jika belum memiliki pdfinfo ketik command:
```
sudo apt install poppler-utils
```
3. Cari tag-name author atau bisa ketik command:
```
┌──(w4llnut_07㉿kali)-[~/Downloads/_tryhackme/_forensic/intro_digital_forensic]
└─$ pdfinfo ransom-letter.pdf| grep -i "author"
```
![image](https://github.com/user-attachments/assets/3d0f3c9f-ebb5-4aa3-b725-8ceddf900851)

4. Submit jawaban: Ann Gree Shepherd

## [Photo EXIF Data]
EXIF stands for Exchangeable Image File Format; it is a standard for saving metadata to image files. Whenever you take a photo with your smartphone or with your digital camera, plenty of information gets embedded in the image. The following are examples of metadata that can be found in the original digital images:

Camera model / Smartphone model
Date and time of image capture
Photo settings such as focal length, aperture, shutter speed, and ISO settings
Because smartphones are equipped with a GPS sensor, finding GPS coordinates embedded in the image is highly probable. The GPS coordinates, i.e., latitude and longitude, would generally show the place where the photo was taken.

There are many online and offline tools to read the EXIF data from images. One command-line tool is exiftool. ExifTool is used to read and write metadata in various file types, such as JPEG images. (The AttackBox already has exiftool installed; however, if you are using Kali Linux and don’t have exiftool installed, you can install it using sudo apt install libimage-exiftool-perl.) In the following terminal window, we executed exiftool IMAGE.jpg to read all the EXIF data embedded in this image.
If you take the above coordinates and search one of the online maps, you will learn more about this location. Searching Microsoft Bing Maps or Google Maps for 51 deg 30' 51.90" N, 0 deg 5' 38.73" W reveals the street where the photo was taken. Note that for the search to work, we had to replace deg with ° and remove the extra white space. In other words, we typed 51°30'51.9"N 0°05'38.7"W in the map search bar.

### [Soal 2]
Using exiftool or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street?

1. Gunakan exiftool untuk melihat EXIF data file gambar
2. Jika belum memiliki exiftool bisa ketik command:
```
sudo apt install libimage-exiftool-perl
```
3. Jika sudah, di terminal ketik command:
```
┌──(w4llnut_07㉿kali)-[~/Downloads/_tryhackme/_forensic/intro_digital_forensic]
└─$ exiftool letter-image.jpg 
```
maka akan muncul banyak EXIF data yang banyak dan tidak worth it membaca tag-name satu persatu
4. Gunakan command linux seperti piping dan grep -iname:
![image](https://github.com/user-attachments/assets/9a5aa723-9478-4462-8a9f-3e3f1e9896a9)

Tempat foto diambil kemungkinan besar kordinat jadi cari dengan key-word "gps"
5. Masuk ke https://www.gps-coordinates.net/ dan masukkan kordinat yang ada

![image](https://github.com/user-attachments/assets/52b3c8f4-4928-4fcb-b663-b5c407627912)

Akan muncul kordinat yang merujuk ke suatu jalan
6. Submit jawaban: Milk Street

### [Soal 3]
What is the model name of the camera used to take this photo?

1. Sama seperti sebelumnya, gunakan exiftool yang digabung dengan piping dan grep:
![image](https://github.com/user-attachments/assets/58325044-34f1-4c78-b0fb-f4af4004a557)
3. Submit jawaban: Canon EOS R6

## [Congrats!]
![image](https://github.com/user-attachments/assets/6acf3b7a-061f-40f8-9494-7feeec1a7a6f)


