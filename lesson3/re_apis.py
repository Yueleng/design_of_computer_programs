def test_search():
    a, b, c = lit('a'), lit('b'), lit('c')
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar = star(dot)
    assert search(lit('def'), 'abcdefg') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdefg') == None
    assert search(a, 'not the start') == 'a'
    assert match(a, 'not the start') == None
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

# intepretor vs compiler
# return remainders set
null = frozenset()
def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        # remainder is a singleton set. e.g. set(['g']) for text = 'defg' and x = 'def'.
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        # first get the remainder as t1 and then from t1 to get remainder t2 to form the remainder set.
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        # \ represents : union of two sets.
        # results is union of two remainder sets.
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        # deduct any character and the rest is the singleton remainder set.
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        # oneofIdx = text.find(x)
        #return set([text[:oneofIdx] + text[oneofIdx+1:]])
        # deduct any character in x and the rest is the singleton remainder set.
        return set([text[1:]]) if any(text.startswith(c) for c in x) else null
        # or return set([text[1:]]) if any(text.startswith(x) else null # str.startswith(x), x can be tuple, can we compare every char in the tuple, which is equivalent to the above 
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)



def components(pattern):
    "Return the op, x and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y



    
#------------------------------------------------------------------------------------------------

def search(pattern, text):
    "Match pattern anywhere in text; return longest earlies match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        # "if m:" does not hold here, because empty string '' is considered as fail but we need '' to return ''
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
def opt(x): return alt(lit(''), x) # opt(x) means that x is optional
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)



print(test_search())