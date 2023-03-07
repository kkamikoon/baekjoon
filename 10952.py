import sys
done = False

while not done:
    A, B = sys.stdin.readline().split(" ")
    if not int(A) and not int(B):
        done = True
        continue
    print(int(A) + int(B))
