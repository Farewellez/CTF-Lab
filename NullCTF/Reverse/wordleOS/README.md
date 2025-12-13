```
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ file wordle_os.bin
wordle_os.bin: DOS/MBR boot sector

```

MBR -> 512 Bytes, tapi disini
446 bytes = bootloader code yang bertugas memuat os ke dalam memory dan memulai eksekusi
64 bytes = partition table yang berisi informasi kecil di awal harddisk tentang bagaimana partisinya
2 bytes 0x55aa = boot signature

MBR sendiri itu ada di sektor pertama drive, baik HDD maupun SSD. MBR punya program khusus yang namanya bootloader. bootloader akan di transfer BIOS ke memory dan darisini kendali ada di bootloader. di sini bootloader
bakal cek MBR di bagian 64 bytes nya yang digunakan untuk partition table untuk mencari partisi yang aktif. di dalam partisi aktif, bootloader akan mencari boot record yang ada di sektor pertama partisi aktif. boot record disini
akan di cek boot signature yang valid sebelum dieksekusi sebagai program. boot record juga yang akan load file system

```
ls -l wordle_os.bin 
-rw-r--r-- 1 w4llnut_07 kali 94720 Dec  5 13:57 wordle_os.bin

```

ada lebih 94208 bytes -> ??? belum tau apa ini

coba cek magic bytes 55aa khas dari mbr di sektor 1 dari disk

```
xxd -l 512 wordle_os.bin      
00000000: 31c0 8ed8 8ec0 8ed0 8ee0 8ee8 fcbc 007c  1..............|
00000010: be12 7d66 e8a2 0000 00e4 92a8 0275 060c  ..}f.........u..
00000020: 0224 fee6 92fa 1e06 0f01 1676 7d0f 20c0  .$.........v}. .
00000030: 0c01 0f22 c0eb 00bb 1000 8edb 8ec3 24fe  ..."..........$.
00000040: 0f22 c007 1ffb bb01 0f66 b800 8f0b 003e  .".......f.....>
00000050: 6789 18b4 41bb aa55 cd13 0f82 aa00 66b8  g...A..U......f.
00000060: 007e 0000 6689 c366 c1eb 0489 1e98 7d66  .~..f..f......}f
00000070: c1e3 0466 29d8 a396 7d66 b800 7e00 0066  ...f)...}f..~..f
00000080: bb00 4a01 0066 29c3 66c1 eb09 891e 947d  ..J..f).f......}
00000090: 66bb 007c 0000 6629 d866 c1e8 0966 a39a  f..|..f).f...f..
000000a0: 7dbe 927d b442 cd13 7263 c706 987d 0000  }..}.B..rc...}..
000000b0: 66b8 457e 0000 66ff e0eb fe66 e80c 0000  f.E~..f....f....
000000c0: 00b0 0d66 e814 0000 00b0 0aeb 10fc ac84  ...f............
000000d0: c074 0866 e804 0000 00eb f366 c3b4 0ecd  .t.f.......f....
000000e0: 1066 c3b9 0400 88f8 c0e8 043c 0a72 0204  .f.........<.r..
000000f0: 0704 3066 e8e4 ffff ffc1 e304 e2e8 66c3  ..0f..........f.
00000100: 66e8 b5ff ffff ebb1 be33 7deb f3be 547d  f........3}...T}
00000110: ebee 426f 6f74 696e 6720 2866 6972 7374  ..Booting (first
00000120: 2073 7461 6765 292e 2e2e 0045 7272 6f72   stage)....Error
00000130: 3a20 004e 6f20 7375 7070 6f72 7420 666f  : .No support fo
00000140: 7220 696e 7431 3368 2065 7874 656e 7369  r int13h extensi
00000150: 6f6e 7300 4661 696c 6564 2074 6f20 6c6f  ons.Failed to lo
00000160: 6164 2072 6573 7420 6f66 2062 6f6f 746c  ad rest of bootl
00000170: 6f61 6465 7200 1700 7a7d 0000 0000 0000  oader...z}......
00000180: 0000 ffff 0000 009a cf00 ffff 0000 0092  ................
00000190: cf00 1000 0000 0000 0000 0000 0000 0000  ................
000001a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000001f0: 0000 0000 0000 0000 0000 0000 0000 55aa  ..............U.
```

terkonfirmasi di bagian akhir ada 55aa hexadecimal yang menandakan kalau 512 bytes pertama adalah sektor MBR yang berisi bootloader. dari situ kita bisa cek menggunakan binwalk, apakah ada embedded file didalamnya

Lalu aku cek pakai binwalk karena aku cari di google untuk key Linux Tool to extract embedded files itu menggunakan binwalk. dan benar ketika ku cek
```
└─$ binwalk wordle_os.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
52736         0xCE00          ELF, 64-bit LSB executable, AMD x86-64, version 1 (SYSV)
```

ada ELF file 64-bit yang berukuran 52736 ini artinya  dari offset ke 0xCE00 itu dimulai file nya ketika kucek

```
xxd -s 0x0000ce00 wordle_os.bin | head
0000ce00: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
0000ce10: 0200 3e00 0100 0000 303b 2000 0000 0000  ..>.....0; .....
0000ce20: 4000 0000 0000 0000 50a0 0000 0000 0000  @.......P.......
0000ce30: 0000 0000 4000 3800 0800 4000 0e00 0c00  ....@.8...@.....
0000ce40: 0600 0000 0400 0000 4000 0000 0000 0000  ........@.......
0000ce50: 4000 2000 0000 0000 4000 2000 0000 0000  @. .....@. .....
0000ce60: c001 0000 0000 0000 c001 0000 0000 0000  ................
0000ce70: 0800 0000 0000 0000 0100 0000 0400 0000  ................
0000ce80: 0000 0000 0000 0000 0000 2000 0000 0000  .......... .....
0000ce90: 0000 2000 0000 0000 cc0d 0000 0000 0000  .. .............
```

Artinya, harusnya kita bisa dump manual byte nya dari sini menggunakan dd command
```
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ dd if=./wordle_os.bin of=./wordle_os bs=1 skip=52736 count=41984 
41984+0 records in
41984+0 records out
41984 bytes (42 kB, 41 KiB) copied, 0.0973012 s, 431 kB/s
                                                                                                                  
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ ls
desc.md  wordle_os  wordle_os.bin  wordle_os.bin.bak  wordle_os.zip  wu.md
                                                                                                                     
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ file wordle_os    
wordle_os: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
                                                                                                                     
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ xxd -l 16 wordle_os | head            
00000000: 7f45 4c46 0201 0100 0000 0000 0000 0000  .ELF............
```

sekarang harusnya file ini yang benar. sekarang langsung buka ghidra dan buka symbol tree. karena kita ingin tahu cara membaca keyboard di rust maka filter keyboard dan interrupt.
kenapa bisa tahu kalau rust? karena recon dengan strings.

```
┌──(w4llnut_07㉿kali)-[~/…/Lomba/NullCTF/Rev/wordle_os]
└─$ strings wordle_os | head
Welcome to WordleOS!
Correct!
called `Result::unwrap()` on an `Err` value
src\vga_buffer.rs
C:\Users\toma\.cargo\registry\src\index.crates.io-1949cf8c6b5b557f\pc-keyboard-0.7.0\src\scancodes\set1.rs
C:\Users\toma\.cargo\registry\src\index.crates.io-1949cf8c6b5b557f\x86_64-0.14.13\src\addr.rs
src\interrupts.rs
C:\Users\toma\.cargo\registry\src\index.crates.io-1949cf8c6b5b557f\spin-0.9.8\src\once.rs
 index out of bounds: the len is 
 but the index is 
                    
```

.rs indikasi rust. setelah filter maka akan ada format label seperti ini

```
        _RNvNtCs9UuFNFXbVKO_9wordle_os10interrupts26keyboard_interrupt_handler
```

click dua kali dan kita akan ketemu logic kompleks namun mengarahkan kita ke flag di bagian

```
          if (((((*(long *)(DAT_0020a490 + 0xf00) == 0xf200f750f200f6e) &&
                (*(long *)(DAT_0020a490 + 0xf08) == 0xf200f6c0f200f6c)) &&
               ((*(long *)(DAT_0020a490 + 0xf10) == 0xf200f740f200f63 &&
                ((*(long *)(DAT_0020a490 + 0xf18) == 0xf200f7b0f200f66 &&
                 (*(long *)(DAT_0020a490 + 0xf20) == 0xf200f300f200f62)))))) &&
              (*(long *)(DAT_0020a490 + 0xf28) == 0xf200f740f200f30)) &&
             (((((*(long *)(DAT_0020a490 + 0xf30) == 0xf200f310f200f5f &&
                 (*(long *)(DAT_0020a490 + 0xf38) == 0xf200f740f200f6e)) &&
                (*(long *)(DAT_0020a490 + 0xf40) == 0xf200f5f0f200f30)) &&
               ((*(long *)(DAT_0020a490 + 0xf48) == 0xf200f300f200f77 &&
                (*(long *)(DAT_0020a490 + 0xf50) == 0xf200f640f200f72)))) &&
              ((*(long *)(DAT_0020a490 + 0xf58) == 0xf200f330f200f6c &&
               (*(long *)(DAT_0020a490 + 0xf60) == 0xf200f200f200f7d)))))) {
               
```

disini hapus f200f berulang yang mengganggu maka akan dapat list

```
756e
6c6c
7463
7b66
3062
7430
315f
746e
5f30
3077
6472
336c
207d
```

dalam format little endian, gunakan script python untuk ubah sesuai ascii.

```
f = open("./flag_enc.txt")
list_hex = []

for hex in f:
    list_hex.append(hex)

for char in list_hex:
    print(chr(int(char[2:4], 16)),end="")
    print(chr(int(char[:2], 16)),end="")
    
```

hasilnya **nullctf{b00t_1nt0_w0rdl3}**
