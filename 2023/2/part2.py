def process(s: str) -> int:
    rolls = s.split(":")[1].split(";")
    result = {"red": 0, "green": 0, "blue": 0}
    
    for roll in rolls:
        for res in roll.split(","):
            res1 = res.split()

            if (result[res1[1]] < int(res1[0])):
                result[res1[1]] = int(res1[0])
    return tuple(result.values())

i = 0
with open("2023/2/input.txt", "r") as file:
    for line in file:
        r, g, b = process(line)
        print(r, g, b)
        i += r * g * b

print(i)