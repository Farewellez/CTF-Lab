import re
import time


# Read in flag from file
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'


song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

MAX_LINES = 100

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
  
  # Find startLabel, refrain and refrain return
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:
      start = i + 1
    elif song_lines[i] == '[REFRAIN]':
      refrain = i + 1
    elif song_lines[i] == 'RETURN':
      refrain_return = i

  # Print lyrics
  line_count = 0
  lip = start
  
  print("lip: ", lip)
  print("start: ", start)
  print("refrain: ", refrain)
  print("reafrain_return: ", refrain_return)
  print("finished: ",finished)
  input()

  # print("\nmemulai lirik")
  while not finished and line_count < MAX_LINES:
    # print("line_count saat ini: ", line_count)
    print("lip: ", lip)
    print(f"line_count: {line_count}")
    print(f"song_lines[lip]: {song_lines[lip]}")
    line_count += 1
    for line in song_lines[lip].split(';'):
      # input()
      # print(f"apakah {line} == '' dan {song_lines[lip]} != ''")
      if line == '' and song_lines[lip] != '':
        # print("Ya itu sama, continue...")
        continue
      if line == 'REFRAIN':
        # print(f"ya, benar...\nrefrain_return saat ini: {refrain_return}\n{song_lines[refrain_return]} saat ini")
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        # print(f"{song_lines[refrain_return]} after")
        # print(f"{lip} before")
        lip = refrain
        # print(f"{lip} after")
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        # print(f"Hasil input: {crowd}\n{song_lines[lip]} before....")
        song_lines[lip] = 'Crowd: ' + crowd
        print("song_lines[lip] = ", song_lines[lip])
        # print(f"{song_lines[lip]} after....")
        # print(f"{lip} before...")
        lip += 1
        # print(f"{lip} after...")
      elif re.match(r"RETURN [0-9]+", line):
        print("BINGO...lip before: ", lip)
        print(line.split())
        print(line.split()[1])
        lip = int(line.split()[1])
        print("BINGO...lip after: ", lip)
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1



reader(song_flag_hunters, '[VERSE1]')
