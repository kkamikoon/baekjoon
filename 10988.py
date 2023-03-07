import sys
import math


def is_palindrome(S: list):
    for i in range(math.trunc(len(S)/2)):
        if S[i] != S[-(i+1)]:
            return False
    return True


S = list(sys.stdin.readline().strip())

print(1 if is_palindrome(S) else 0)
