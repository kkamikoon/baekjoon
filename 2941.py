import sys

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

S = sys.stdin.readline().strip()
temp = S
cnts = 0

while temp:
    checked = False

    for c in croatia:
        if c in temp[:len(c)]:
            checked = True
            cnts += 1

            if temp == temp[:len(c)]:
                temp = ""
            else:
                temp = temp[len(c):]
        
    if not checked:
        temp = temp[1:]
        cnts += 1

print(cnts)
