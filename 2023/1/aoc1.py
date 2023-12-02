i = 0
with open("aoc1_1.txt", "r") as f:
    for line in f:
        digits = [int(c) for c in line if c.isdigit()]
        i += digits[0] * 10 + digits[-1]

print(i)