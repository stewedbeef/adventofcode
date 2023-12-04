cards = list()
with open("2023/4/input.txt", "r") as file:
    for line in file:
        # The cards are sequential
        printout = line.split(":")[1].split("|")
        draw = set(map(lambda x: int(x) - 1, printout[0].split()))
        correct = set(map(lambda x: int(x) - 1, printout[1].split()))
        cards.append(len(draw.intersection(correct)))

hand = [1] * len(cards)

# If we should have to process all original and copied scratchcards and we will
# never win beyond the end of the table, then surely we know we will iterate
# past all the cards exactly once.
for number in range(len(cards)):
    x = cards[number]
    # We win the next x cards
    for i in range(number + 1, number + x + 1):
        hand[i] += hand[number]

print(sum(hand))