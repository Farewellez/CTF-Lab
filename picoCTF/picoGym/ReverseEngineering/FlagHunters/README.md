yang perlu di garis bawahi itu bagian ini


**There's a hidden refrain this program doesn't print by default.**

Program ini akan mencetak lirik yang melompat dari verse ke refrain. tapi ada refrain yang ga di print secara
default by program. misinya mencari refrain ini.

karena ini adalah whitebox kita bisa debug program menggunakan source code yang ada

```
def reader(song, startLabel):
  lip = 0
  start = 0
  refrain = 0
  refrain_return = 0
  finished = False

  # Get list of lyric lines
  song_lines = song.splitlines()
  print("song_line = ", song_lines)
  for index, char in enumerate(song_lines):
    print(index, char)
```

di bagian ini, agar songlines terlihat maka aku tambahkan iterasi for loop untuk cek per index dalam element list liriknya dan hasilnya seperti ini

```
0 Pico warriors rising, puzzles laid bare,
1 Solving each challenge with precision and flair.
2 With unity and skill, flags we deliver,
3 The ether’s ours to conquer, picoCTF{flag}
4 
5 
6 
7 [REFRAIN]
8 We’re flag hunters in the ether, lighting up the grid,
9 No puzzle too dark, no challenge too hid.
10 With every exploit we trigger, every byte we decrypt,
11 We’re chasing that victory, and we’ll never quit.
12 CROWD (Singalong here!);
13 RETURN
14 
15 [VERSE1]
16 Command line wizards, we’re starting it right,
17 Spawning shells in the terminal, hacking all night.
18 Scripts and searches, grep through the void,
19 Every keystroke, we're a cypher's envoy.
20 Brute force the lock or craft that regex,
21 Flag on the horizon, what challenge is next?
22 
23 REFRAIN;
24 
25 Echoes in memory, packets in trace,
26 Digging through the remnants to uncover with haste.
27 Hex and headers, carving out clues,
28 Resurrect the hidden, it's forensics we choose.
29 Disk dumps and packet dumps, follow the trail,
30 Buried deep in the noise, but we will prevail.
31 
32 REFRAIN;
33 
34 Binary sorcerers, let’s tear it apart,
35 Disassemble the code to reveal the dark heart.
36 From opcode to logic, tracing each line,
37 Emulate and break it, this key will be mine.
38 Debugging the maze, and I see through the deceit,
39 Patch it up right, and watch the lock release.
40 
41 REFRAIN;
42 
43 Ciphertext tumbling, breaking the spin,
44 Feistel or AES, we’re destined to win.
45 Frequency, padding, primes on the run,
46 Vigenère, RSA, cracking them for fun.
47 Shift the letters, matrices fall,
48 Decrypt that flag and hear the ether call.
49 
50 REFRAIN;
51 
52 SQL injection, XSS flow,
53 Map the backend out, let the database show.
54 Inspecting each cookie, fiddler in the fight,
55 Capturing requests, push the payload just right.
56 HTML's secrets, backdoors unlocked,
57 In the world wide labyrinth, we’re never lost.
58 
59 REFRAIN;
60 
61 Stack's overflowing, breaking the chain,
62 ROP gadget wizardry, ride it to fame.
63 Heap spray in silence, memory's plight,
64 Race the condition, crash it just right.
65 Shellcode ready, smashing the frame,
66 Control the instruction, flags call my name.
67 
68 REFRAIN;
69 
70 END;
```

disini karena aku jalankan di local, jadi aku coba buat dummy flag dulu

```
┌──(w4llnut_07㉿kali)-[~/…/Platform/picoCTF/Rev/FlagHunters]
└─$ echo "picoCTF{flag}" > flag.txt

```

dan terlihat dummy flagnya ada di index ke-tiga yang harusnya juga sama dengan yang ada di server. dari sini bisa disimpulkan kalau "**hidden refrain**" yang disebutkan di deskripsi adalah lirik lagu pada baris ke 0 - 3. 
kita perlu mentrigger algoritma dari program yang ada untuk menampilkan refrain ini. kuncinya ada di logic split method di bagian ini

```
for line in song_lines[lip].split(';'):
...
elif re.match(r"RETURN [0-9]+", line):
        print("BINGO...lip before: ", lip)
        print(line.split())
        print(line.split()[1])
        lip = int(line.split()[1])
        print("BINGO...lip after: ", lip)
```
regex ini digunakan untuk catch string yang mengandung "RETURN" dan angka dari 0-9.
aku tambahkan debug untuk cek. dibawa kemana payload yang kita inject di input method program. ketika dijalankan, hasil lognya seperti ini

```
We’re chasing that victory, and we’ll never quit.
lip:  12
line_count: 27
song_lines[lip]: Crowd: ;RETURN 1
Crowd: 
BINGO...lip before:  13
['RETURN', '1']
1
BINGO...lip after:  1
lip:  1
line_count: 28
song_lines[lip]: Solving each challenge with precision and flair.
Solving each challenge with precision and flair.
lip:  2
line_count: 29
song_lines[lip]: With unity and skill, flags we deliver,
With unity and skill, flags we deliver,
lip:  3
line_count: 30
song_lines[lip]: The ether’s ours to conquer, picoCTF{flag}
The ether’s ours to conquer, picoCTF{flag}
```

terlihat kalau ternyata input kita bisa digunakan untuk mentrigger refrain 0-3 dengan tambahan ";" di awal. dari situ karena input mengandung kata "RETURN" dan angka "1" maka lip yang sebelumnya 12 menjadi lip = 1 yang mentrigger "**hidden refrain**" yang disebut dan secara otomatis akan mengeluarkan flag yang ada. dengan ini kita bisa trigger juga ke server picoCTF dengan nc yang yang diberikan.

```
┌──(w4llnut_07㉿kali)-[~/…/Platform/picoCTF/Rev/FlagHunters]
└─$ nc verbal-sleep.picoctf.net 55575
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: ;RETURN 3

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: 
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0099cf61}
```

FLAG: **picoCTF{70637h3r_f0r3v3r_0099cf61}**
