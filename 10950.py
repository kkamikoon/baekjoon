T = int(input())
Q = []

for __ in range(T):
    A, B = input().split(" ")
    Q.append([int(A), int(B)])

for _q in Q:
    print(sum(_q))