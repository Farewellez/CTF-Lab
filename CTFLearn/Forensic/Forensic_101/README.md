## Nama Chall: Forensics 101
## Level: Easy

Think the flag is somewhere in there. Would you help me find it? https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c

## Write-up
1. Simple aja, langsung cek raw data dari image nya pake xxd
```
xxd <namaimage>.jpg | less
```
Nanti bakal ketemu:
000023b0: d7c6 28c6 0e66 6c61 677b 776f 7721 5f64  ..(..flag{wow!_d
000023c0: 6174 615f 6973 5f63 6f6f 6c7d 8512 53be  ata_is_cool}..S.
