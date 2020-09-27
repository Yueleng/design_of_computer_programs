
# white space
def grammar(description, whitespace=r'\s*'):
    """
    Convert a description to a grammar. 
    Each line is a rule for a non-terminal symbol; it looks like this:
        Symbol => A1 A2 ... | B1 B2 ... | C1 C2 ...
        where the right-hand side is one or more alternatives, separated by the '|' sign.
    Each alternative is a sequence of atoms, separated by spaces. 
    An atom is either a symbol on some left-hand side, or it is a regular expression that will be passed to re.match
        to match a token.
    Notation for *, +, or ? not alloed in a rule alternative (but ok within a token).
    Use '\' to continue long lines.
    You must include spaces or tabs around '=>' and '|'. 
    That's within the grammar description itself.
    The grammar that gets defined allows whitespace between tokens by default specify '' as the second argument to grammar()
        to disallow this (or supply any regular expression to describe allowable whitespace between tokens)
    """
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G

def split(text, sep=None, maxsplit = -1):
    "Like str.split applied to text, but strips whitespace from each piece"
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

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


print(G)