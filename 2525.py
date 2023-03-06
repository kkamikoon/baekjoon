H, M = input().split()
H = int(H)
M = int(M)
T = int(input()) + M

_H = H + int(T / 60)
_M = T - (int(T / 60) * 60)

print(f"{_H%24} {_M}")
