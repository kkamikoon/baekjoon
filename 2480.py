from collections import Counter

dice = [int(i) for i in input().split(" ")]
cnt = Counter(dice)

answer = 0

if len(cnt) == 1:
    answer = 10000 + (dice[0] * 1000)

elif len(cnt) == 2:
    index = list(cnt.values()).index(2)
    num = list(cnt.keys())[index]
    answer = 1000 + (num*100)

else:
    answer = max(*dice) * 100

print(answer)