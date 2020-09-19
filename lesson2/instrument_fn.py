import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next( # next after nothing is the first, so go ahead and return that
        (WATER, ZEBRA)
        for (red, green, ivory, yellow, blue) in c(orderings)
        if imright(green, ivory)
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
        if Englishman is red
        if Norwegian is first
        if nextto(Norwegian, blue)
        for (coffee, tea, milk, oj, WATER) in c(orderings)
        if coffee is green
        if Ukranian is tea
        if milk is middle
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
        if Kools is yellow
        if LuckyStrike is oj
        if Japanese is Parliaments
        for (dog, snails, fox, horse, ZEBRA) in c(orderings)
        if Spaniard is dog
        if OldGold is snails
        if nextto(Chesterfields, fox)
        if nextto(Kools, horse)
    )


def imright(h1, h2):
    "house h1 is immediately right of h2 if h1 - h2 == 1"
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differe by 1"
    return abs(h1 - h2) == 1


def instrument_fn(fn, *args):
    c.start, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items' % (fn.__name__, result, c.start, c.items)) 

def c(sequence):
    """
    Generate items in sequence; keeping counts as we go;
    c.starts is the number of sequences started;
    c.items is number of items generated.
    """
    c.start += 1
    for item in sequence:
        c.items += 1
        yield item

instrument_fn(zebra_puzzle)
# zebra_puzzle got (1, 5) with 25 iters over 2775 items

# Quiz
def ints(start, end=None):
    i = start
    while i <= end or end is None:
        yield i 
        i = i + 1

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    yield 0
    for i in ints(1):
        yield i
        yield -i