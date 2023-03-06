import sys

N = int(sys.stdin.readline().strip())
result = 0

for __ in range(N):
    groups = {}
    is_group = True

    for index, c in enumerate(list(sys.stdin.readline().strip())):
        if groups.get(c) == None or groups.get(c)+1 == index:
            groups[c] = index
        else:
            is_group = False
            break
    
    if is_group:
        result += 1


print(result)