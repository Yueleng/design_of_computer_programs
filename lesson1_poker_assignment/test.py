import itertools

allranks = "23456789TJQKA"
redcards = [r + s for r in allranks for s in "HD"]
blackcards = [r + s for r in allranks for s in "SC"]

# for lst in itertools.product([1, 2, 3], [100, 200]):
#     print(lst)


def replacements(card):
    """Return a list of possible replacements for a card
    There will be more than 1 only for wild cards."""
    if card == "?B":
        return blackcards
    elif card == "?R":
        return redcards
    else:
        return [card]


for card in map(replacements, ["2C", "?B", "?R"]):
    print(card)

for h in itertools.product(*map(replacements, ["2C", "?B", "?R"])):
    print(h)

