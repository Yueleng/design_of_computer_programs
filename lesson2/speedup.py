import re, itertools, string, time
from funWrapper import timedcall

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def fast_solve(formula):
    f, letters = compile_formula_no_leading_zero(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            # split the tuple into multiple param inputs. like spread operator
            if f(*digits) is True:
                table = str.maketrans(letters, "".join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose=False):
    """
    Compile formula into a function. Also return letters found, as a str,
    in some order as params of function. For example, 'YOU == ME ** 2' returns
    lambda E, M, Y, O, U: (1*U+10*O+100*Y) == (1*E+10*M) ** 2, 'EMYOU'
    """
    # the order of char in letters does not matter, in fact, the order is different for every run.
    letters = "".join(set(re.findall("[A-Z]", formula))) 
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z]+)", formula))
    body = "".join(tokens)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


def compile_formula_no_leading_zero(formula, verbose=False):
    """For example, 'YOU == ME ** 2' => 
    lambda Y, M, E, U, O: Y != 0 and M != 0 and ((1*U+10*O+100*Y) == (1*E+10*M)**2) 
    """
    letters = "".join(set(re.findall("[A-Z]", formula)))
    firstLetters = set(re.findall(r"\b([A-Z])[A-Z]", formula))
    parms = ", ".join(letters)
    tokens = map(compile_word, re.split("([A-Z]+)", formula))
    body = "".join(tokens)
    if firstLetters:
        test = " and ".join(L + "!=0" for L in firstLetters)
        body = "%s and (%s)" % (test, body)
    f = "lambda %s: %s" % (parms, body)
    if verbose:
        print(f)
    return eval(f), letters


# print(re.split("([A-Z]+)", 'YOU == ME ** 2'))
# ['', 'YOU', ' == ', 'ME', ' ** 2']

# print(re.split("[A-Z]+", 'YOU == ME ** 2'))
# ['', ' == ', ' ** 2']

# print(fast_solve("YOU == ME ** 2"))

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
        print('%6.4f sec: %s ' % timedcall(fast_solve, example))
    print('%6.4f tot. ' % (time.process_time() - t0))


def main():
    test()


if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')