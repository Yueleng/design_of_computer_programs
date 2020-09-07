import itertools
from fractions import Fraction

sex = 'BG'

def product(*variables):
    "The cartesian product (as a str) of the possibilities for each variable."
    return map(''.join, itertools.product(*variables))

two_kids = product(sex, sex)

two_kids = [s for s in two_kids]

one_boy = [s for s in two_kids if 'B' in s]

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
    """Conditional probability: P(predicate(s) | s in event).
    The proportional of states in event for which predicate is true.
    """
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))


"""
Out of all families with two kids at least one boy born on a Tuesday,
what is the probability of two boys?
"""
day = 'SMTWtFs'

two_kids_bday = product(sex, day, sex, day)
two_kids_bday = [s for s in two_kids_bday]

boy_tuesday = [s for s in two_kids_bday if 'BT' in s]

print(condP(two_boys, boy_tuesday))

boy_anyday = [s for s in two_kids_bday if 'B' in s]

month = 'JFMAmJjaSOND'

two_kids_bmonth = product(sex, month, sex, month)
boy_december = [s for s in two_kids_bmonth if 'BD' in s]

def report(verbose=False, predicate=two_boys, predname='2 boys', 
            cases=[('2 kids', two_kids), ('2 kids born any day', two_kids_bday),
                   ('at least 1 boy', one_boy), ('at least 1 boy born any day', boy_anyday), 
                   ('at least 1 boy born on Tuesday', boy_tuesday), 
                   ('at least 1 boy born in December', boy_december)]):
    import textwrap
    for (name, event) in cases:
        print('P(%s | %s) = %s' % (predname, name, condP(predicate, event)))
        if verbose:
            print('Reason:\n"%s" has %d elements: \n%s' % (
                name, len(event), textwrap.fill(' '.join(event), 85)))
            good = [s for s in event if predicate(s)]
            print('of those, %d are "%s": \n%s\n\n' % (
                len(good), predname, textwrap.fill(' '.join(good), 85)))

report(verbose=True)
