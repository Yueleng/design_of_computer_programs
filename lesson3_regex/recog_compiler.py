null = frozenset([])

# retern the remainders set.
def lit(x): return lambda text: set([text[len(x):]]) if text.startswith(x) else null

def seq(x, y): return lambda text: set([]).union(*map(y, x(text)))

def alt(x, y): return lambda text: x(text) | y(text)
# Alternative
# def alt(x, y): return lambda text: set([]).union(x(text)).union(y(text))

def oneof(chars): return lambda t: set(t[1:]) if (t and t[0] in chars) else null

dot = lambda t: set(t[1:]) if t else null
eol = lambda t: set(['']) if t == '' else null

def star(x): return lambda t: set([t]) | set(t2 for t1 in x(t) if t1 != t for t2 in star(x)(t1))
# Alternative, may not hold if pat(lit(''))
# def star(pat): return lambda t: set([t]).union(*map(star(pat), pat(t)))

def plus(pat): return lambda text: pat(text) | set([t2 for t1 in pat(text) if t1 != text for t2 in plus(pat)(t1)])
# Alternative, may not hold if pat(lit(''))
# def plus(pat): return lambda text: pat(text).union(*map(plus(pat), pat(text)))
# Alternative: use seq and star to construct plus
# def plus(x): return seq(x, star(x))

def match(pattern, text):
    "Match pattern agaist start of text; return longest match found or None"
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]


pat = lit('a')
print(pat)

print(pat('a string'))

pat2 = plus(pat)
print(pat2)
print(pat2('aaaaab'))

pat3 = star(pat)
print(pat3)
print(pat3('aaaaab'))

import dis 
from math import sqrt
dis.dis(lambda x, y: sqrt(x ** 2 + y ** 2))


