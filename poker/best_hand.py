import itertools


def best_hand(hand):
    """From a 7 hand, return the best hand """
    # best_hand = None
    # best_rank = None
    # for hand_five in itertools.combinations(hand, 5):
    #     if best_rank is not None or best_rank < hand_rank(hand_five):
    #         best_hand = hand_five
    #         best_rank = hand_rank(hand_five)

    # return best_hand
    return max(itertools.combinations(hand, 5), key=hand_rank)


allranks = "23456789TJQKA"
redcards = [r + s for r in allranks for s in "HD"]
blackcards = [r + s for r in allranks for s in "SC"]


def best_wild_hand(hand):
    """Try all values for jokers in all 5-card """
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands)


def replacements(card):
    """Return a list of possible replacements for a card
    There will be more than 1 only for wild cards."""
    if card == "?B":
        return blackcards
    elif card == "?R":
        return redcards
    else:
        return [card]
