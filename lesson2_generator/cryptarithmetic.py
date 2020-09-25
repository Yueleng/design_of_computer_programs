import string, re, itertools, time
from funWrapper import timedcall
def solve(formula):
    """
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    """
    for f in fill_in(formula):
        if valid(f):
            return f

def fill_in(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    "Formula f is valid iff it has no numbers with leading zero, and evals true."
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X/X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])
""".splitlines()

def test():
    t0 = time.process_time()
    for example in examples:
        print()
        print(11*' ', example)
        print('%6.4f sec: %s ' % timedcall(solve, example))
    print('%6.4f tot. ' % (time.process_time() - t0))

def main():
    test()


if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')