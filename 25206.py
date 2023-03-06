import sys

scores = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_units = []
total_scores = []

for __ in range(20):
    subject, unit, score = [a for a in sys.stdin.readline().strip().split(" ")]
    unit = float(unit)
    score = scores.get(score)

    if score == None:
        continue

    total_units.append(unit)
    total_scores.append(unit * score)

if sum(total_units):
    print(f"{sum(total_scores) / sum(total_units):.6f}")
else:
    print("0.000000")

