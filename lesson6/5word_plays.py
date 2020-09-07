import time

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

def find_words(letters, pre='', results=None):
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L, '', 1), pre+L, results)
    return results

def word_plays(hand, board_letters):
    "Find all word plays from hand that can be made to abut with a letter on board."
    # Find prefix + L + suffix; L from board_letters, rest from hand
    results = set()
    for pre in find_prefixes(hand, '', set()):
        for L in board_letters:
            add_suffixes(removed(hand, pre), pre+L, results)
    return results

def find_prefixes(hand, pre='', results=None):
    "Find all prefixes (of words) that can be made from letters in hand."
    if results is None: results = set()
    if pre in PREFIXES:
        results.add(pre)
        for L in hand:
            find_prefixes(hand.replace(L, '', 1), pre+L, results)
    return results

# find_prefixes improved
prev_hand, prev_results = '', set() # cache for find_prefixes
def find_prefixes_cache(hand, pre='', results=None):
    ## Cache the most recent full hand (don't cache intermediate results)
    global prev_hand, prev_results
    if hand == prev_hand: return prev_results
    if results is None: results = set()
    if pre == '': prev_hand, prev_results = hand, results
    # Now do the computation
    if pre in WORDS or pre in PREFIXES: results.add(pre)
    if pre in PREFIXES:
        for L in hand:
            find_prefixes_cache(hand.replace(L, '', 1), pre+L, results)
    return results

def add_suffixes(hand, pre, results):
    """Return the set of words that can be formed by extending pre with letters in hand."""
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in hand:
            add_suffixes(hand.replace(L, '', 1), pre+L, results)
    return results


def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters
    

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1-t0, result

hands = {  ## Regression test
    'ABECEDR': set(['BE', 'CARE', 'BAR', 'BA', 'ACE', 'READ', 'CAR', 'DE', 'BED', 'BEE',
         'ERE', 'BAD', 'ERA', 'REC', 'DEAR', 'CAB', 'DEB', 'DEE', 'RED', 'CAD',
         'CEE', 'DAB', 'REE', 'RE', 'RACE', 'EAR', 'AB', 'AE', 'AD', 'ED', 'RAD',
         'BEAR', 'AR', 'REB', 'ER', 'ARB', 'ARC', 'ARE', 'BRA']),
    'AEINRST': set(['SIR', 'NAE', 'TIS', 'TIN', 'ANTSIER', 'TIE', 'SIN', 'TAR', 'TAS',
         'RAN', 'SIT', 'SAE', 'RIN', 'TAE', 'RAT', 'RAS', 'TAN', 'RIA', 'RISE',
         'ANESTRI', 'RATINES', 'NEAR', 'REI', 'NIT', 'NASTIER', 'SEAT', 'RATE',
         'RETAINS', 'STAINER', 'TRAIN', 'STIR', 'EN', 'STAIR', 'ENS', 'RAIN', 'ET',
         'STAIN', 'ES', 'ER', 'ANE', 'ANI', 'INS', 'ANT', 'SENT', 'TEA', 'ATE',
         'RAISE', 'RES', 'RET', 'ETA', 'NET', 'ARTS', 'SET', 'SER', 'TEN', 'RE',
         'NA', 'NE', 'SEA', 'SEN', 'EAST', 'SEI', 'SRI', 'RETSINA', 'EARN', 'SI',
         'SAT', 'ITS', 'ERS', 'AIT', 'AIS', 'AIR', 'AIN', 'ERA', 'ERN', 'STEARIN',
         'TEAR', 'RETINAS', 'TI', 'EAR', 'EAT', 'TA', 'AE', 'AI', 'IS', 'IT',
         'REST', 'AN', 'AS', 'AR', 'AT', 'IN', 'IRE', 'ARS', 'ART', 'ARE']),
    'DRAMITC': set(['DIM', 'AIT', 'MID', 'AIR', 'AIM', 'CAM', 'ACT', 'DIT', 'AID', 'MIR',
         'TIC', 'AMI', 'RAD', 'TAR', 'DAM', 'RAM', 'TAD', 'RAT', 'RIM', 'TI',
         'TAM', 'RID', 'CAD', 'RIA', 'AD', 'AI', 'AM', 'IT', 'AR', 'AT', 'ART',
         'CAT', 'ID', 'MAR', 'MA', 'MAT', 'MI', 'CAR', 'MAC', 'ARC', 'MAD', 'TA',
         'ARM']),
    'ADEINRST': set(['SIR', 'NAE', 'TIS', 'TIN', 'ANTSIER', 'DEAR', 'TIE', 'SIN', 'RAD', 
         'TAR', 'TAS', 'RAN', 'SIT', 'SAE', 'SAD', 'TAD', 'RE', 'RAT', 'RAS', 'RID',
         'RIA', 'ENDS', 'RISE', 'IDEA', 'ANESTRI', 'IRE', 'RATINES', 'SEND',
         'NEAR', 'REI', 'DETRAIN', 'DINE', 'ASIDE', 'SEAT', 'RATE', 'STAND',
         'DEN', 'TRIED', 'RETAINS', 'RIDE', 'STAINER', 'TRAIN', 'STIR', 'EN',
         'END', 'STAIR', 'ED', 'ENS', 'RAIN', 'ET', 'STAIN', 'ES', 'ER', 'AND',
         'ANE', 'SAID', 'ANI', 'INS', 'ANT', 'IDEAS', 'NIT', 'TEA', 'ATE', 'RAISE',
         'READ', 'RES', 'IDS', 'RET', 'ETA', 'INSTEAD', 'NET', 'RED', 'RIN',
         'ARTS', 'SET', 'SER', 'TEN', 'TAE', 'NA', 'TED', 'NE', 'TRADE', 'SEA',
         'AIT', 'SEN', 'EAST', 'SEI', 'RAISED', 'SENT', 'ADS', 'SRI', 'NASTIER',
         'RETSINA', 'TAN', 'EARN', 'SI', 'SAT', 'ITS', 'DIN', 'ERS', 'DIE', 'DE',
         'AIS', 'AIR', 'DATE', 'AIN', 'ERA', 'SIDE', 'DIT', 'AID', 'ERN',
         'STEARIN', 'DIS', 'TEAR', 'RETINAS', 'TI', 'EAR', 'EAT', 'TA', 'AE',
         'AD', 'AI', 'IS', 'IT', 'REST', 'AN', 'AS', 'AR', 'AT', 'IN', 'ID', 'ARS',
         'ART', 'ANTIRED', 'ARE', 'TRAINED', 'RANDIEST', 'STRAINED', 'DETRAINS']),
    'ETAOIN': set(['ATE', 'NAE', 'AIT', 'EON', 'TIN', 'OAT', 'TON', 'TIE', 'NET', 'TOE',
         'ANT', 'TEN', 'TAE', 'TEA', 'AIN', 'NE', 'ONE', 'TO', 'TI', 'TAN',
         'TAO', 'EAT', 'TA', 'EN', 'AE', 'ANE', 'AI', 'INTO', 'IT', 'AN', 'AT',
         'IN', 'ET', 'ON', 'OE', 'NO', 'ANI', 'NOTE', 'ETA', 'ION', 'NA', 'NOT',
         'NIT']),
    'SHRDLU': set(['URD', 'SH', 'UH', 'US']),
    'SHROUDT': set(['DO', 'SHORT', 'TOR', 'HO', 'DOR', 'DOS', 'SOUTH', 'HOURS', 'SOD',
         'HOUR', 'SORT', 'ODS', 'ROD', 'OUD', 'HUT', 'TO', 'SOU', 'SOT', 'OUR',
         'ROT', 'OHS', 'URD', 'HOD', 'SHOT', 'DUO', 'THUS', 'THO', 'UTS', 'HOT',
         'TOD', 'DUST', 'DOT', 'OH', 'UT', 'ORT', 'OD', 'ORS', 'US', 'OR',
         'SHOUT', 'SH', 'SO', 'UH', 'RHO', 'OUT', 'OS', 'UDO', 'RUT']),
    'TOXENSI': set(['TO', 'STONE', 'ONES', 'SIT', 'SIX', 'EON', 'TIS', 'TIN', 'XI', 'TON',
         'ONE', 'TIE', 'NET', 'NEXT', 'SIN', 'TOE', 'SOX', 'SET', 'TEN', 'NO',
         'NE', 'SEX', 'ION', 'NOSE', 'TI', 'ONS', 'OSE', 'INTO', 'SEI', 'SOT',
         'EN', 'NIT', 'NIX', 'IS', 'IT', 'ENS', 'EX', 'IN', 'ET', 'ES', 'ON',
         'OES', 'OS', 'OE', 'INS', 'NOTE', 'EXIST', 'SI', 'XIS', 'SO', 'SON',
         'OX', 'NOT', 'SEN', 'ITS', 'SENT', 'NOS'])}

def test_word_play():
    assert word_plays('ADEQUAT', set('IRE')) == {'RATE', 'AI', 'DATE', 'TEE', 'IT', 'EAU', 'TI', 'DUE', 'QUIT', 'RE', 'RET', 'QAID', 'RAD', 'ART', 'AE', 'AIT', 'AID', 'ER', 'ARE', 'ETA', 'QUIET', 'EAR', 'ED', 'TEAR', 'AQUAE', 'TAR', 'DE', 'ID', 'AREA', 'RED', 'DUI', 'QI', 'TIE', 'TRUE', 'URD', 'ET', 'QUITE', 'IDEA', 'ATE', 'TAE', 'DIT', 'TEA', 'TRADE', 'TED', 'QUID', 'EQUID', 'DEAR', 'DEE', 'TUI', 'AR', 'RAT', 'EAT', 'RUE', 'ADEQUATE', 'ERA', 'RUT', 'READ', 'DIE', 'QUADRATE'}
    return 'test passed'

print(test_word_play())

# longest words play
def longest_words(hand, board_letters):
    words_list = list(word_plays('ADEQUAT', set('IRE')))
    words_list.sort(key=lambda word: len(word), reverse=True)
    return words_list

def longest_words_u(hand, board_letters):
    words = word_plays(hand, board_letters)
    # sort will convert set into list
    return sorted(words, reverse=True, key=len)

print(longest_words_u('ADEQUAT',set('IRE')))


# Word Score
POINTS = dict(A=1, B=3, C=3, D=2, E=1, F=4, G=2, H=4, I=1, J=8, K=5, L=1, M=3, N=1, O=1, P=3, Q=10, R=1, S=1, T=1, U=1, V=4, W=4, X=8, Y=4, Z=10, _=0)
def word_score(word):
    return sum(POINTS[L] for L in word)

# Top N Hands
def topn(hand, board_letters, n=10):
    "Return a list of the top n words that hand can play, sorted by word score."
    words = word_plays(hand, board_letters)
    return sorted(words, reverse=True, key=word_score)[:n]

print(topn('ADEQUAT', set('IRE')))


# Row Plays
class anchor(set):
    "An anchor is where a new word can be placed; has a set of allowable letters."

LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ANY = anchor(LETTERS) # The anchor that can be any letter

# |A.....BE.C...D.|
mnx, moab = anchor('MNX'), anchor('MOAB')
a_row = ['|', 'A', mnx, moab, '.', '.', ANY, 'B', 'E', ANY, 'C', ANY, '.', ANY, 
         'D', ANY, '|']

a_hand = 'ABCEHKN'


def row_plays(hand, row):
    "Return a set of legal plays in row. A row play is an (start, 'WORD') pair"
    results = set()
    ## To each allowable prefix, add all suffixes, keeping words

    for (i, sq) in enumerate(row[1:-1], 1):
        if isinstance(sq, anchor):
            pre, maxsize = legal_prefix(i, row)
            if pre: ## Add to the letters already on the borad
                start = i - len(pre)
                add_suffixes(hand, pre, start, row, results, anchored=False)
            else: ## Empty to left: go through the set of all possible prefixes
                # for pre in find_prefixes(hand):
                for pre in find_prefixes_cache(hand):
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(removed(hand, pre), pre, start, row, results, anchored=False)
    return results

def legal_prefix(i, row):
    """A legal prefix of an anchor at row[i] is either a string or letters
    already on the board, or new letters that fit into empty space.
    Return the tuple (prefix_on_board, maxisize) to indicate this.
    E.g. legal_prefix(9, a_row) == ('BE', 2) and for 6, ('', 2)"""
    s = i # starting index
    while is_letter(row[s-1]): s -= 1
    if s < i: ## There is a prefix
        return ''.join(row[s:i]), i-s
    while is_empty(row[s-1]) and not isinstance(row[s-1], anchor): s -= 1
    return ('', i-s)

def is_empty(sq):
    return sq == '.' or sq == '*' or isinstance(sq, anchor)

def is_letter(sq):
    return isinstance(sq, str) and sq in LETTERS

def add_suffixes(hand, pre, start, row, results, anchored=True):
    "All all possible suffixes, and accumelate (start, word) pairs in results"
    i = start + len(pre)
    if pre in WORDS and anchored and not is_letter(row[i]):
        results.add((start, pre))
    if pre in PREFIXES:
        sq = row[i]
        if is_letter(sq):
            add_suffixes(hand, pre+sq, start, row, results)
        elif is_empty(sq):
            possibilities = sq if isinstance(sq, anchor) else ANY
            for L in hand:
                if L in possibilities:
                    add_suffixes(hand.replace(L, '', 1), pre+L, start, row, results)
    return results


def test_row():
    assert legal_prefix(2, a_row) == ('A', 1)
    assert legal_prefix(3, a_row) == ('', 0)
    assert legal_prefix(6, a_row) == ('', 2)
    assert legal_prefix(9, a_row) == ('BE', 2)
    assert legal_prefix(11, a_row) == ('C', 1)
    assert legal_prefix(13, a_row) == ('', 1)
    assert is_empty('.') and is_empty(ANY) and is_empty(anchor('ABC'))
    assert not is_empty('L') and not is_empty('|')
    assert row_plays(a_hand, a_row) == {(3, 'AB'), (3, 'BAN'), (14, 'DE'), (12, 'BED'), (7, 'BENCH'), (12, 'HAD'), (3, 'BAH'), (3, 'AE'), (13, 'EDH'), (3, 'AH'), (12, 'BAD'), (3, 'BA'), (10, 'CAN'), (12, 'AND'), (1, 'ANA'), (3, 'AN'), (12, 'END'), (13, 'ED'), (13, 'AD'), (3, 'BACKBENCH'), (3, 'BEN'), (3, 'BE'), (3, 'ANE'), (1, 'AN'), (10, 'CAB'), (3, 'ACE'), (12, 'CAD')}
    return 'test passed'

print(test_row())





print(find_prefixes_cache('ABCDE'))
print(find_prefixes('ABCDE'))

# Show the Board
def a_board():
    return list(map(list, ['|||||||||||||||||',
                      '|J............I.|',
                      '|A.....BE.C...D.|',
                      '|GUY....F.H...L.|',
                      '|||||||||||||||||']))

def show(board):
    "Print the board."
    result = ''
    for row in board:
        result += ''.join(row) + '\n'
    print(result)

# def show_u(board):
#     "Print the board."
#     for row in board:
#         for sq in row:
#             print sq,
#         print
show(a_board())

# Horizontal Plays
def horizontal_plays_a(hand, board):
    "Find all horizonal plays -- ((i,j), word) pairs -- across all rows."
    results = set()
    for (j, row) in enumerate(board[1: -1], 1):
        set_anchors(row, j, board)
        results.union( set(((i, j), word) for (i, word) in row_plays(hand, row)) )
    return results

def horizontal_plays(hand, board):
    "Find all horizonal plays -- (score, (i,j), word) pairs -- across all rows."
    results = set()
    for (j, row) in enumerate(board[1: -1], 1):
        set_anchors(row, j, board)
        for (i, word) in row_plays(hand, row):
            score = calculate_score(board, (i, j), ACROSS, hand, word)
            results.add( ( score, (i, j), word) )
    return results

def all_plays_a(hand, board):
    """
    All plays in both directions. A play is a (score, pos, dir, word) tuple,
    where pos is an (i, j) pair, and dir is ACROSS or DOWN.
    """
    hplays = horizontal_plays(hand, board)
    vplays = horizontal_plays(hand, transpose(board))
    results = set()
    for (score, (i, j), word) in hplays:
        results.add((score, (i,j), ACROSS, word))
    for (score, (j, i), word) in vplays:
        results.add((score, (i,j), DOWN, word))
    return results

def all_plays(hand, board):
    """
    All plays in both directions. A play is a (pos, dir, word) tuple,
    where pos is an (i, j) pair, and dir is ACROSS or DOWN.
    """
    hplays = horizontal_plays(hand, board)
    vplays = horizontal_plays(hand, transpose(board))
    return (set((score, (i,j), ACROSS, w) for (score, (i,j), w) in hplays) | 
           set((score, (i,j), DOWN, w) for (score, (j,i), w) in vplays) )

# Incrementing 1 in the i direction, (ACROSS)
# Incrementing 1 in the j direction, (DOWN)
ACROSS, DOWN = (1, 0), (0, 1)

# Set Anchors
# Mutate the input: row into row which can feed to row_plays(hand, row)
def set_anchors(row, j, board):
    """
    Anchors are empty squares with a neighboring letter. Some are restricted 
    by crosss-words to be only a subset of letters.
    """
    for (i, sq) in enumerate(row[1:-1], 1):
        neighborlist = (N, S, E, W) = neighbors(board, i, j)
        # Anchors are square adjacent to a letter. Plus the '*' square.
        if sq == '*' or (is_empty(sq) and any(map(is_letter, neighborlist))):
            if is_letter(N) or is_letter(S):
                # Find letters that fit with the cross (vertical) word
                (j2, w) = find_cross_word(board, i, j)
                row[i] = anchor(L for L in LETTERS if w.replace('.', L) in WORDS)
            else: # Unrestricted empty square -- any letter will fit.
                row[i] = ANY

# find_corss_word : (board, i, j) => (j2, w) where j2 = i, w = words
# find_cross_word(a_board(), 2, 2) returns (2, '.U')
# find_cross_word(a_board(), 1, 2) returns (1, 'JAG')

w = '.U'
print(anchor(L for L in LETTERS if w.replace('.', L) in WORDS))

def find_cross_word(board, i, j):
    """
    Find the vertical word that crosses board[j][i]. Return (j2, w),
    where j2 is the starting row, and w is the word
    """
    sq = board[j][i]
    w = sq if is_letter(sq) else '.'
    for j2 in range(j, 0, -1):
        sq2 = board[j2-1][i]
        if is_letter(sq2): w = sq2 + w
        else: break
    for j3 in range(j+1, len(board)):
        sq3 = board[j3][i]
        if is_letter(sq3): w = w + sq3
        else: break
    return (j2, w)

def neighbors(board, i, j):
    """
    Return a list of the contents of the four neighboring squares
    in the order N, S, E, W. 
    """
    return [board[j-1][i], board[j+1][i], 
            board[j][i+1], board[j][i-1]]

def transpose(matrix):
    """
    Transpose e.g. [[1,2,3], [4,5,6]] to [[1,4], [2,5], [3,6]]
    """
    return list(map(list, zip(*matrix)))

def transpose_u(matrix):
    """
    Transpose e.g. [[1,2,3], [4,5,6]] to [[1,4], [2,5], [3,6]]
    """
    return map(list, zip(*matrix))

# Final bird: scoring
def calculate_score(board, pos, direction, hand, word):
    "Return the total score for this play"
    total, crosstotal, word_mult = 0, 0, 1
    starti, startj = pos
    di, dj = direction
    other_direction = DOWN if direction == ACROSS else ACROSS
    for (n, L) in enumerate(word):
        i, j = starti + n*di, startj + n*dj
        sq = board[j][i]
        b = BONUS[j][i]
        word_mult *= (1 if is_letter(sq) else 3 if b == TW else 2 if b in (DW, '*') else 1)
        letter_mult = (1 if is_letter(sq) else 3 if b == TL else 2 if b == DL else 1)
        total += POINTS[L] * letter_mult
        if isinstance(sq, anchor) and sq is not ANY and direction is not DOWN: # MAIN FUNC ONLY CALLED IN horizontal_plays
            crosstotal += cross_word_score(board, L, (i, j), other_direction)
    return crosstotal + word_mult * total

def cross_word_score(board, L, pos, direction):
    """
    Return the score of a word made in the other direction from the main word
    """
    i, j = pos
    (j2, word) = find_cross_word(board, i, j)
    return calculate_score(board, (i, j2), DOWN, L, word.replace('.', L))

def bonus_template(quadrant):
    """
    Make a board from the upper-left quadrant.
    """
    return mirror(list(map(mirror, quadrant.split())))

def bonus_template_u(quadrant):
    """
    Make a board from the upper-left quadrant.
    """
    return mirror(map(mirror, quadrant.split()))

def mirror(sequence): return sequence + sequence[-2::-1]

SCRABBLE = bonus_template("""
|||||||||
|3..:...3
|.2...;..
|..2...:.
|:..2...:
|....2...
|.;...;..
|..:...:.
|3..:...*
""")

WWF = bonus_template("""
|||||||||
|...3..;.
|..:..2..
|.:..:...
|3..;...2
|..:...:.
|.2...3..
|;...:...
|...:...*
""")

BONUS = WWF
DW, TW, DL, TL = '23:;'


# Tests:
# Pending code

def show_all(board):
    "Print the board"
    for j, row in enumerate(board):
        row1 = ''
        for i, sq in enumerate(row):
            row1 += sq if (is_letter(sq) or sq == '|') else BONUS[j][i]    
        print(row1+'\n')

def make_play(play, board):
    "Put the word down on the board."
    (score, (i, j), (di, dj), word) = play
    for (n, L) in enumerate(word):
        board[j + n*dj][i + n*di] = L
    return board

NOPLAY = None

def best_play_a(hand, board):
    # Return the highest-scoring play. Or None
    all_possible_plays = all_plays(hand, board)
    best_score = 0
    best_play = (0, (0,0), (0,1), '')
    for play in all_possible_plays:
        score, _, _, _ = play
        if score > best_score:
            best_score = score
            best_play = play
    if all_possible_plays:
        return best_play
    return NOPLAY

def best_play(hand, board):
    "Return the highest-scoring play. Or None"
    plays = all_plays(hand,board)
    return sorted(plays)[-1] if plays else NOPLAY

def show_best(hand, board):
    print('Current board:')
    show_all(board)
    play = best_play(hand, board)
    if play:
        print('\nNew word: %r scores %d' % (play[-1], play[0]))
        show_all(make_play(play,board))
    else:
        print('Sorry, no legal plays')

show_best(a_hand, a_board())
