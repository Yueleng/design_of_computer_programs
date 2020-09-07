# -----------------
# User Instructions
# 
# In this problem, you will define a function, boggle_words(), 
# that takes a board as input and returns a set of words that
# can be made from the board according to the rules of Boggle.

def boggle_words(board, minlength=3):
    "Find all the words on this  Boggle board; return as a set of words."
    result = set()
    N = size(board)

    def extend_path(prefix, path):
        if prefix in WORDS and len(prefix) >= minlength:
            result.add(prefix)
        if prefix in PREFIXES:
            for j in neighbors(path[-1], N):
                if j not in path and board[j] != BORDER:
                    extend_path(prefix + board[j], path + [j])

    for (i, L) in enumerate(board):
        if L != BORDER:
            extend_path(L, [i])
    return result


def test():
    b = Board('XXXX TEST XXXX XXXX')
    assert b == '|||||||XXXX||TEST||XXXX||XXXX|||||||'
    assert display(b) == """
||||||
|XXXX|
|TEST|
|XXXX|
|XXXX|
||||||""".strip()
    assert boggle_words(b) == set(['SET', 'SEX', 'TEST'])
    assert neighbors(20, 6) == (13, 14, 15, 19, 21, 25, 26, 27)
    assert len(boggle_words(Board('TPLER ORAIS METND DASEU NOWRB'))) == 317
    assert boggle_words(Board('PLAY THIS WORD GAME')) == set([
        'LID', 'SIR', 'OAR', 'LIS', 'RAG', 'SAL', 'RAM', 'RAW', 'SAY', 'RID', 
        'RIA', 'THO', 'HAY', 'MAR', 'HAS', 'AYS', 'PHI', 'OIL', 'MAW', 'THIS', 
        'LAY', 'RHO', 'PHT', 'PLAYS', 'ASIDE', 'ROM', 'RIDE', 'ROT', 'ROW', 'MAG', 
        'THIRD', 'WOT', 'MORE', 'WOG', 'WORE', 'SAID', 'MOR', 'SAIL', 'MOW', 'MOT', 
        'LAID', 'MOA', 'LAS', 'MOG', 'AGO', 'IDS', 'HAIR', 'GAME', 'REM', 'HOME', 
        'RED', 'WORD', 'WHA', 'WHO', 'WHOM', 'YID', 'DRAW', 'WAG', 'SRI', 'TOW', 
        'DRAG', 'YAH', 'WAR', 'MED', 'HIRE', 'TOWARDS', 'ORS', 'ALT', 'ORE', 'SIDE', 
        'ALP', 'ORA', 'TWA', 'ERS', 'TOR', 'TWO', 'AIS', 'AIR', 'AIL', 'ERA', 'TOM', 
        'AID', 'TOG', 'DIS', 'HIS', 'GAR', 'GAM', 'HID', 'HOG', 'PLAY', 'GOA', 'HOW', 
        'HOT', 'WARM', 'GOT', 'IRE', 'GOR', 'ARS', 'ARM', 'ARE', 'TOWARD', 'THROW'
    ])
    return 'tests pass'

def Board(text):
    """Input is a string of space-separated rows of N letters each;
    result is a string of size (N+2)**2 with boarders all around."""
    rows = text.split()
    N = len(rows)
    rows = [BORDER*N] + rows + [BORDER*N]
    return ''.join(BORDER + row + BORDER for row in rows)

def size(board): return int(len(board) ** 0.5)

def neighbors(i, N):
    return (i-N-1, i-N, i-N+1, i-1, i+1, i+N-1, i+N, i+N+1)

BORDER = '|'

def display(board):
    "Return a string representation of board, suitable for printing"
    N = size(board)
    return '\n'.join(board[i:i+N] for i in range(0, N**2, N))

# ------------
# Helpful functions
# 
# You may find that the following functioins useful. These functions
# are identical to those we defined in lecture.
def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist(r"C:\Users\Yueleng\OneDrive\CS212\lesson6\words4k.txt")

print(test())


