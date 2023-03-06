import sys

S = sys.stdin.readline().strip().split(" ")
while ("" in S):
    S.remove("")

print(len(S))