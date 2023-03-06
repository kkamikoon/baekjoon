import sys

A, B = sys.stdin.readline().strip().split(" ")

LA = list(A)
LB = list(B)
LA.reverse()
LB.reverse()

LA = "".join(LA)
LB = "".join(LB)

if int(LB) > int(LA):
    print(LB)
else:
    print(LA)