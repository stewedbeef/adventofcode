def process(s: str) -> int:
    game = s.split(":")
    id = int(game[0][len("Game "):])

    for roll in game[1].split(";"):
        result = {"red": 0, "green": 0, "blue": 0}

        for res in roll.split(","):
            res1 = res.split()
            result[res1[1]] += int(res1[0])

        if (result["red"] > 12
            or result["green"] > 13
            or result["blue"] > 14):
            return 0
    return id

i = 0
with open("2023/2/input.txt", "r") as file:
    for line in file:
        i += process(line)

print(i)