import sys
Answer = [1,1,2,2,2,8]
Quest = [int(i) for i in sys.stdin.readline().split(" ")]

for a, q in zip(Answer, Quest):
    print(f"{a-q}", end=" ")
