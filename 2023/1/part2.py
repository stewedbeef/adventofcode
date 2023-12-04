import re

digitNames = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9}
forwardRegex = re.compile(r"\d|" + "|".join(digitNames.keys()))
backwardRegex = re.compile(r"\d|" + "|".join([s[::-1] for s in digitNames.keys()]))

def parseInt(s: str) -> int:
    n = digitNames.get(s, None)
    if n == None:
        return int(s)
    else:
        return n

def process(s: str) -> int:
    forwardmatch = re.search(forwardRegex, s)
    backwardmatch = re.search(backwardRegex, s[::-1])
    return parseInt(forwardmatch.group(0)) * 10 + parseInt(backwardmatch.group(0)[::-1])

i = 0
with open("2023/1/input.txt", "r") as f:
    for line in f:
        i += process(line)
print(i)