### THIS PROGRAM IS NOT CORRECT

schematic = list()
with open("2023/3/input.txt", "r") as file:
    for line in file:
        schematic.append(list(line))

searched = [[False for c in r] for r in schematic]

def searchForAsterisk(schematic, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            try:
                if schematic[r+i][c+j] == '*':
                    return r+i, c+j
            except IndexError:
                pass
    return None

accumulator = 0
for r in range(len(schematic)):
    for c in range(len(schematic[r])):
        if searched[r][c]:
            continue
        if not schematic[r][c].isdigit():
            searched[r][c] = True
            continue
        # Consume the digits and find the asterisk
        ratios = [0, 0]
        asterisk = None
        i = 0
        while schematic[r][c+i].isdigit():
            searched[r][c+i] = True
            asterisk = asterisk or searchForAsterisk(schematic, r, c+i)
            ratios[0] = ratios[0] * 10 + int(schematic[r][c+i])
            i += 1
        if not asterisk:
            continue
        # Look for the integer
        r, c = asterisk
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if (not searched[asterisk[0]+i][asterisk[1]+j]
                        and schematic[asterisk[0]+i][asterisk[1]+j].isdigit()):
                        r, c = asterisk[0] + i, asterisk[1] + j
                except IndexError:
                    pass
        if not schematic[r][c].isdigit():
            continue
        i = 0
        # Find the leftmost digit of the number
        while schematic[r][c+i].isdigit():
            i -= 1
        i += 1
        while schematic[r][c+i].isdigit():
            searched[r][c+i] = True
            ratios[1] = ratios[1] * 10 + int(schematic[r][c+i])
            i += 1
        print(f"{ratios[0]},\t{ratios[1]},\t{ratios[0] * ratios[1]}")
        accumulator += ratios[0] * ratios[1]

print(accumulator)