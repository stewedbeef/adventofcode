accumulator = 0
c = 0
with open("2023/4/input.txt", "r") as file:
    for line in file:
        printout = line.split(":")[1].split("|")
        draw = set(map(int, printout[0].split()))
        correct = set(map(int, printout[1].split()))
        matches = len(draw.intersection(correct))
        if matches == 0:
            continue
        score = 2 ** (matches - 1)
        accumulator += score

print(accumulator)