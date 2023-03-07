X = int(input())
N = int(input())
_X = 0

for __ in range(N):
    Price, Num = input().split(" ")
    _X += (int(Price) * int(Num))

if X == _X:
    print("Yes")
else:
    print("No")