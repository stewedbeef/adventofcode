schematic = list()
with open("2023/3/input.txt", "r") as file:
    for line in file:
        schematic.append(list(line))
searched = [[False for _ in r] for r in schematic]

def checksymb(schematic, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r + i < 0 or r + i >= len(schematic):
                continue
            if c + j < 0 or c + j >= len(schematic[r+i]):
                continue
            if not (schematic[r+i][c+j].isdigit()
                    or '.' in schematic[r+i][c+j]
                    or schematic[r+i][c+j].isspace()):
                return True
    return False

total = 0
for r in range(len(schematic)):
    for c in range(len(schematic[r])):
        if searched[r][c]:
            continue
        searched[r][c] = True
        symb = False
        i = 0
        x = 0
        while c + i < len(schematic[r]) and schematic[r][c+i].isdigit():
            symb = symb or checksymb(schematic, r, c+i)
            x = x * 10 + int(schematic[r][c+i])
            searched[r][c+i] = True
            i += 1
        if symb:
            # print(x)
            total += x

print(total)