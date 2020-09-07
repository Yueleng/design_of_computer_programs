import re
import string
import itertools
import time

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next(
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


def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timedcalls(n, fn, *args):
    "Call function n times with args; "
    "n times if n is an int, or up to n seconds if n is a float; "
    "return the min, avg, and max time."
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers"
    return sum(numbers) / float(len)


def ints(start, end=None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1


def all_ints():
    yield 0
    for i in ints(1):
        yield i
        yield -i


def c(sequence):
    """
    c.starts is the number of sequence started.
    c.items is number of items generated.
    """
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


def valid(f):
    "Formula f is valid iff it has no numbers with leading zero, and evals true."
    try:
        return not re.search(r"\b0[0-9]", f) and eval(f) is True
    except ArithmeticError:
        return False


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    """
    Generate all possible fillings-in of letters in formula with digits.
    """
    letters = "".join(set(re.findall("[A-Z]", formula)))
    for digits in itertools.permutations("1234567890", len(letters)):
        table = string.maketrans(letters, "".join(digits))
        yield formula.translate(table)


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [
            ("%s*%s" % (10 ** i, d)) for (i, d) in enumerate(word[::-1])
        ]  # reverse it.
        return "(" + "+".join(terms) + ")"
    else:
        return word


def fast_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, "".join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """
    Compile formula into a function. Also return letters found, as a str,
    in some order as params of function. For example, 'YOU == ME ** 2' returns
    (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'
    """
    letters = "".join(set(re.findall("[A-Z]", formula)))
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z])", formula))
    body = "".join(tokens)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


def compile_formula_improved(formula, verbose=False):
    """For example, 'YOU == ME ** 2' => 
    lambda Y, M, E, U, O: Y != 0 and M != 0 and ((1*U+10*O+100*Y) == (1*E+10*M)**2) 
    """
    letters = "".join(set(re.findall("[A-Z]", formula)))
    firstLetters = set(re.findall("\b([A-Z])[A-Z]", formula))
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z])", formula))
    body = "".join(tokens)
    if firstLetters:
        test = " and ".join(L + "!=0" for L in firstLetters)
        body = "%s and (%s)" % (test, body)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters

# ------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.


def floor_puzzle():
    # Your code here
    floors = first, _, _, _, fifth = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))

    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if Hopper is not fifth
                if Kay is not first
                if Liskov is not first and Liskov is not fifth
                if Perlis - Kay > 0
                if abs(Ritchie - Liskov) > 1
                if abs(Liskov - Kay) > 1
                )


