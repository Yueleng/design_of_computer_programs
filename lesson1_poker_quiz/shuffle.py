import random

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n-card hands"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

print(deal(2, 7))

def shuffle1(deck):
    "My teacher's algorithm: not efficient, it might never terminate"
    "Hard Part: This algorithm is not even fair"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)

def shuffle(deck):
    """Knuth's Algorithm P."""
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i,N))

def swap(deck, i, j):
    """swap element i and j of a collection"""
    deck[i],  deck[j] = deck[j], deck[i]

from collections import defaultdict

def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)  # set the value of any key to int 0 by default.
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1. / factorial(len(deck)) ## expected count
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__ # function name
    print('%s(%s) %s  ' % (name, deck, ('ok' if ok else "*** BAD ***")))
    for item, count in sorted(counts.items()): # make the dictionary a list
        print("%s:%4.1f  " % (item, count*100./n), end='')
    print()

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc', 'ab']):
    for deck in decks:
        print()
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n * factorial(n-1)

def shuffle2(deck):
    """A modification of my teacher's algorithm; correct"""
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)

def shuffle3(deck):
    "An easier modification of my teacher's algorithm. Biased, not correct"
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))

# Testing
test_shufflers([shuffle, shuffle1]) # shuffle1 is not correct

test_shufflers([shuffle, shuffle2]) # shuffle2 is correct

test_shufflers([shuffle, shuffle3]) # shuffle3 may looks correct, actually it's not