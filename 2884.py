H, M = input().split(" ")
H = int(H)
M = int(M)

if (M-45) < 0:
    if (H-1) < 0:
        H += (24-1)
    else:
        H -= 1
    M += (15)
else:
    M -= 45

print(f"{H} {M}")

