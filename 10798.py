import sys

S = []
R = ""

for i in range(5):
    S.append(list(sys.stdin.readline().strip()))

for i in range(15):
    for j in range(5):
        try:
            print(f"{S[j][i]}", end="")
        except:
            pass
