import itertools
import time

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next( # next after nothing is the first, so go ahead and return that
        (WATER, ZEBRA)
        for (red, green, ivory, yellow, blue) in orderings
        if imright(green, ivory)
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
        if Englishman is red
        if Norwegian is first
        if nextto(Norwegian, blue)
        for (coffee, tea, milk, oj, WATER) in orderings
        if coffee is green
        if Ukranian is tea
        if milk is middle
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
        if Kools is yellow
        if LuckyStrike is oj
        if Japanese is Parliaments
        for (dog, snails, fox, horse, ZEBRA) in orderings
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

# def timedcall(fn):
#     "Call function and return elapsed time."
#     t0 = time.process_time()
#     fn()
#     t1 = time.process_time()
#     return t1 - t0

# *args means, it can take any number of arguments, and they should all be joined up into a tuple called args.
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.process_time()
    result = fn(*args)
    t1 = time.process_time()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)

print(timedcalls(0.5, zebra_puzzle))
print(timedcalls(300, zebra_puzzle))