# File 10

import re
from cache_management import memo

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

    tokenizer = grammar[' '] + '(%s)' # white spaces that separate atoms

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text) # we are updating the text variable
            if text is None: return Fail
            result.append(tree)
        return result, text

    @memo
    def parse_atom(atom, text): # atom is any key in Gammar
        if atom in grammar: # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]: 
                tree, rem = parse_sequence(alternative, text)
                # because we return the parsed alternative sequence whenever text is not none.
                # That's why we may need to put more general alternative to the left
                if rem is not None: return [atom]+tree, rem # [atom, *tree], plus of list means concatenate
            return Fail
        else: # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    # Body of parse:
    return parse_atom(start_symbol, text)


if __name__ == '__main__':
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

    print(parse('Exp', 'a * x', G))