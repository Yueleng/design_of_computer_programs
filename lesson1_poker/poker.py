print(max([3, 4, 5, 0]))
print(max([3, 4, -5, 0], key = abs))


# -----------
# User Instructions
# 
# Modify the poker() function to return the best hand 
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
#

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax_peter(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    key = key or (lambda x: x)
    maxValue = max(iterable, key=key)
    return [hand for hand in iterable if key(hand) == key(maxValue)]

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    "8: straight flush; 7: full of a kind; 6:full house: 3 of a kind + 2 of a kind"
    "5: 3 of a kind; 4:flush;  3: straight; 2: 2 pairs; 1: 2 of a kind; 0: nothing(High Card)"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


    return None # we will be changing this later.

def card_ranks(hand):
    "hand: ['6C', '7C', '8C', '9C', 'TC']"
    "Return a list of the ranks, sorted with higher first. For example: [10, 9, 8, 7, 6]"
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def straight(ranks):
    ranks.sort()
    return ranks[-1] - ranks[0] == 4 and len(set(ranks)) == 5
    # Peter's solution
    # return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    return len(set([s for r,s in hand])) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    two_pair = set()
    for r in ranks:
        if ranks.count(r) == 2: two_pair.add(r)
    two_pair_lst = list(two_pair)
    two_pair_lst.sort(reverse = True)
    return tuple(two_pair_lst) if len(two_pair) == 2 else None

def two_pair_peter(ranks):
    pair = kind(2, ranks);
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# Test

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    assert poker([sf, fk, fh]) == [sf]
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    assert poker([sf]) == [sf]
    assert poker([sf] +  99*[fk]) == [sf]

    # add 3 new assert statements here
    # what is the desired return for the following three hands
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    # test card_rank
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    

    # test straight and flush
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    # test kind(, ranks)
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    assert two_pair_peter(fkranks) == None
    assert two_pair_peter(tpranks) == (9, 5)

    # more testing cases
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert straight(card_ranks(al)) == True 

    # ties
    al_copy = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert poker([al, al_copy]) == [al, al_copy]

    return "tests pass"
print(test())



import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

# S: Spade, H: Hearts, D: Diamond, C: Club
mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    deal_of_hands = []
    chosen_deck = deck[0: numhands * n]
    for i in range(numhands):
        deal_of_hands.append(chosen_deck[i*n: i*n+n])
    return deal_of_hands

hand_names = ['High Card', 'Pair', '2 Pair', '3 Kind', 'Straight', 'Flush', 'Full House', '4 Kind', 'Straight Flush']

def hand_percentages(n=700 * 1000):
    "Sample n random hands and print a table of percentages for each type of hand."
    counts = [0] * 9
    for i in range(int(n/10)):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names[i], 100. * counts[i]/n))


hand_percentages()