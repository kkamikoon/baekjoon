import sys
done = False

while not done:
    try:
        A, B = sys.stdin.readline().split(" ")
        print(int(A) + int(B))
    except ValueError:
        done = True

