just a fucking nested list

use this fucking script:

```
import ast

flag = ""
with open('./scram_flag.txt') as f:
    r_f_string = f.read()         # Ini masih string
    r_f_list = ast.literal_eval(r_f_string) # Ini mengubahnya menjadi list

for i, hexa in enumerate(r_f_list):
    if i == 15 or i == 16:
        # print("\n\n================== ANOMALI ==================")
        # print(f"index-{i} {hexa}")
        # print("dapat: ",hexa[0], hexa[-1],end="\n\n")
        child_hexa = hexa[-1]
        flag += chr(int(hexa[0],16))
        # print("\n\n================== CHILD ==================")
        # for j, c_hexa in enumerate(child_hexa):
        #     print(f"index-{i}.{j} {c_hexa}")
        #     print("dapat: ",c_hexa[0], c_hexa[-1],end="\n\n")
        #     flag += chr(int(c_hexa[0],16)) + chr(int(c_hexa[-1],16))
        # print("=============================================\n\n")
    else:
        # print(f"index-{i} {hexa}")
        # print("dapat: ",hexa[0], hexa[-1],end="\n\n")
        flag += chr(int(hexa[0],16)) + chr(int(hexa[-1],16))

print("FLAG:", flag)
```
