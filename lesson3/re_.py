import re

def search(pattern, text):
    "Return True if pattern appears anywhere in text."
    if pattern.startswith('^'):
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)
def match(pattern, text):
    "Return True if pattern appears at the start of text."
    if pattern == '':
        return True
    elif pattern == '$':
        return text == ''
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                match(pat, text)
        return True
    else:
        return (match1(pattern[0], text) and 
                match(pattern[1:], text[1:])) # fill in this line

def match1(p, text):
    """Return true if first character of text matches pattern character p."""
    if not text: return False
    return p == '.' or p == text[0]

def match_star(p, pattern, text):
    """Return true if any number of char p, followed by pattern, matches text"""
    return (match(pattern, text) or 
            (match1(p, text) and match_star(p, pattern, text[1:])))


def test():
    assert search('baa*!', 'Sheep said baaaa!')
    assert search('baaa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert match('baa*!', 'baaaaaaaaa! said the sheep')
    assert search('def', 'abcdefg')
    assert search('def$', 'abcdef')
    assert search('def$', 'abcdefg') == False
    assert search('^start', 'not the start') == False
    assert match('start', 'not the start') == False
    assert match('a*b*c*', 'just anything')
    assert match('x?', 'text')
    assert match('text?', 'text')
    assert match('text?', 'tex')
    def words(text): return text.split()
    assert all(match('aa*bb*cc*$', s)
                for s in words('abc aaabbccc aaaabcccc'))
    assert not any(match('aa*bb*cc*$', s) 
                for s in words('ac aaabbcccd aaaa-b-cccc'))
    assert all(search('^ab.*aca.*a$', s)
                for s in words('abracadabra abacaa about-acacia-fa'))
    assert all(search('t.p', s)
                for s in words('tip top tap atypical tepid stop'))
    assert not any(search('t.p', s)
                for s in words('TYPE teepee tp'))
    return 'test passes'

print(test())


def test_search():
    a, b, c = lit('a'), lit('b'), lit('c')
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar = star(dot)
    assert search(lit('def'), 'abcdefg') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdefg') == None
    assert search(a, 'not the start') == 'a'
    assert match(a, 'not the start') == 'None'
    assert match(abcstars, 'aaabbbccccccccdef') == 'aaabbbcccccccc'
    assert match(abcstars, 'junk') == ''
    assert all(match(seq(abcstars, eol), s) == s
                for s in 'abc aaabbccc aaaabcccc'.split())
    assert all(match(seq(abcstars, eol), s) == None
                for s in 'cab aaabbcccd aaaa-b-cccc'.split())
    r = seq(lit('ab'), seq(dotstar, seq(lit('aca'), seq(dotstar, seq(a, eol)))))
    assert all(search(r, s) is not None
                for s in 'abracadabra abacaa about-acacia-flora'.split())
    assert all(match(seq(c, seq(dotstar, b)), s) is not None
                for s in 'cab cob carob cb carbuncle'.split())
    assert not any(match(seq(c, seq(dot, b)), s)
                for s in 'crab cb across scab'.split())
    return 'test_search passes'

#------------------------------------------------------------------------------------------------

def search(pattern, text):
    "Match pattern anywhere in text; return longest earlies match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        if m is not None:
            return m

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None"
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]


def lit(string): return ('lit', string)
def seq(x, y): return ('seq', x, y)
def alt(x, y): return ('alt', x, y)
def star(x): return ('star', x)
def plus(x): return seq(x, star(x))
def opt(x): return alt(lit(''), x)
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def components(pattern):
    "Return the op, x and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y
# intepretor
def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        # oneofIdx = text.find(x)
        #return set([text[:oneofIdx] + text[oneofIdx+1:]])
        return set([text[1:]]) if any(text.startswith(c) for c in x) else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)

null = frozenset()


def test():
    assert matchset(('lit', 'abc'), 'abcdef') == set(['def'])
    assert matchset(('seq', ('lit', 'hi'), ('lit', 'there')),
                    'hi there nice to meet you') == set(['nice to meet you'])
    assert matchset(('alt', ('lit', 'dog'), ('lit', 'cat')), 'dog and cat') == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'a'), 'aabc123')           == set(['abc123'])
    assert matchset(('eol',),'')                         == set([''])
    assert matchset(('eol',),'not end of line')          == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])
    return 'tests pass'

print(test())




# -- Compiler
def lit(s): return lambda t: set([t[len(s):]]) if t.startswith(s) else null
def seq(x, y): return lambda t: set().union(*map(y, x(t)))
# def alt(x, y): return lambda text: set().union(x(text)).union(y(text))
def alt(x, y): return lambda t: x(t) | y(t)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else null
dot = lambda t: set(t[1:]) if t else null
eol = lambda t: set(['']) if t == '' else null
def star(x): return lambda t: (set([t]) | 
                               set(t2 for t1 in x(t) if t1 != t for t2 in star(x)(t1) ))

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None"
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]



# def lit(s): return lambda Ns: set([s]) if len(s) in Ns else null

# Avoid repetition
def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
def oneof(chars):   return lambda Ns: set(chars) if 1 in Ns else null
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.


def genseq(x, y, Ns):
    Nss = range(max(Ns) + 1)
    return set(m1 + m2
                for m1 in x(Nss) for m2 in y(Nss)
                if len(m1 + m2) in Ns)

def genseq(x, y, Ns, startx=0):
    "Set of matches to xy whose total len is in Ns, with x-match's len in Ns_x and y-match's len in Ns_y"
    # Tricky part: x+ is defined as: x+ = x x*
    # To stop the recursion, the first x must generate at least 1 char, 
    # and then the recursive x* has that many fewer characters. We 
    # use startx=1 to say that x must match at least 1 chacter
    if not Ns:
        return null

    xmatches = x(set(range(startx, max(Ns) + 1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m>=0)
    ymatches = y(Ns_y)
    return set(m1 + m2
                for m1 in xmatches for m2 in ymatches
                if len(m1+m2) in Ns)


def test_gen():
    def N(hi): return set(range(hi + 1))
    a, b, c = map(lit, 'abc')
    
    assert star(oneof('ab'))(N(2)) == set(['', 'a', 'b', 'aa', 'ab', 'ba', 'bb'])
    
    assert (seq(star(a), seq(star(b), star(c)))(set([4])) == set(
        ['aaaa', 'aaab', 'aaac', 'aabb', 'aabc', 'aacc', 'abbb', 'abbc', 'abcc', 'accc', 
         'bbbb', 'bbbc', 'bbcc', 'bccc', 'cccc']
    ))

    assert (seq(plus(a), seq(plus(b), plus(c)))(set([5])) == set(
        ['aaabc', 'aabbc', 'aabcc', 'abbbc', 'abbcc', 'abccc']
    ))

    assert (seq(oneof('bcfhrsm'), lit('at'))(N(3)) == set(
        ['bat', 'cat', 'fat', 'hat', 'mat', 'rat', 'sat']
    ))

    assert (seq(star(alt(a,b)), opt(c))(set([3])) == set(
        ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc']
    ))

    assert lit('hello')(set([5])) == set(['hello'])

    assert lit('hello')(set([4])) == set()

    assert lit('hello')(set([6])) == set()
    
    return 'test_gen passes'


from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def n_ary(f):
    """Given binary function f(x,y), return an n_ary(f) such that f(x,y,z) = f(x,f(y,z)), etc. Also allow f(x) = x"""
    def n_ary_f(x, *args):
        # if len(args) == 0:
        #     return f(x)
        # elif len(args) == 1:
        #     return f(x, args[0])
        # else:
        #     return n_ary_f(n_ary_f(x, args[0]),*args[1:])
        return x if not args else f(x, n_ary_f(*args))
    # update_wrapper(n_ary, f)
    return n_ary_f

@n_ary
def seq(x, y): return ('seq', x, y)
seq = n_ary(seq)


# Decorator equivalence
def decorator(d):
    return lambda fn: update_wrapper(d(fn), fn)

decorator = decorator(decorator)


@decorator
def memo(f):
    """
    Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up.
    """
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f


@decorator
def countcalls(f):
    """
    Decorator that makes the function count calls to it,
    in callcounts[f].
    """
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}


# -- check the difference of countcalls with or without 

@countcalls
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

@countcalls
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)


# -- write a decorator for 
@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level*indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('%s--> %s === %s' % ( (trace.level - 1)* indent, signature, result))
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f


# Descriptionary
G = grammar(r"""
Exp => Term [+-] Exp | Term
Term => Factor [*/] Term | Factor
Factor => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps => Exp [,] Exps | Exp
Var => [a-zA-Z_]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
""")

def split(text, sep=None, maxsplit = -1):
    "Like str.split applied to text, but strips whitespace from each piece"
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]
def grammar(description):
    """Convert a description to a grammar."""
    G = {}
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G


# white space
def grammar(description, whitespace=r'\s*'):
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G


Fail = (None, None)

# parser
def parse(start_symbol, text, grammar):
    """
    Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole 
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the 
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'
    """

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    def parse_atom(atom, text):
        if atom in grammar: # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem
            return Fail
        else: # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    # Body of parse:
    return parse_atom(start_symbol, text)


