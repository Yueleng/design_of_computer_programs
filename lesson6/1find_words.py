
import time
# f = set(open("C:\Users\Yueleng\OneDrive\CS212\lession6\words4k.txt", 'r').read().upper().split())
# print(f)

# with open("words4k.txt") as mytxt:
#     for line in mytxt:
#         print(line)

# WORDS = set(file('words4k.txt').read().up())
# def find_words(hand):
#     "Find all words that can be made from the letters in hand."
#     results = set()
#     for a in hand:
#         if a in WORDS: result.add(a)



def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.time()
    result = fn(*args)
    t1 = time.time()
    return t1 - t0, result

path = r"C:\Users\Yueleng\OneDrive\CS212\lesson6\words4k.txt"
file = open(path, 'r')
WORDS = set(file.read().upper().split())

def find_words(hand):
    "Find all words that can be made from the letters in hand."
    results = set()
    for a in hand:
        if a in WORDS: results.add(a)
        for b in removed(hand, a):
            w = a + b
            if w in WORDS: results.add(w)
            for c in removed(hand, w):
                w = a+b+c
                if w in WORDS: results.add(w)
                for d in removed(hand, w):
                    w = a+b+c+d
                    if w in WORDS: results.add(w)
                    for e in removed(hand, w):
                        w = a+b+c+d+e
                        if w in WORDS: results.add(w)
                        for f in removed(hand, w):
                            w = a+b+c+d+e+f
                            if w in WORDS: results.add(w)
                            for g in removed(hand, w):
                                w = a+b+c+d+e+f+g
                                if w in WORDS: results.add(w)
    return results

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

# print(find_words('LETTERS'))

# print(find_words('ABECEDR'))
# print(find_words('AEINRST'))
# print(find_words('DRAMITC'))
# print(find_words('ADEINRST'))
# print(find_words('ETAOIN'))
# print(find_words('SHRDLU'))
# print(find_words('SHROUDT'))
# print(find_words('TOXENSI'))

hands = {
    'ABECEDR': set(['ARB', 'RACE', 'BAR', 'CARE', 'REC', 'ED', 'ER', 'CAB', 'DEB', 'DE', 'RE', 'DEE', 'REB', 'CAR', 'READ', 'BE', 'ARC', 'EAR', 'AD', 'RAD', 'REE', 'BRA', 'AE', 'ARE', 'CEE', 'BA', 'CAD', 'BAD', 'DAB', 'DEAR', 'BED', 'RED', 'AR', 'ACE', 'BEAR', 
'ERE', 'ERA', 'AB', 'BEE']), 
    'AEINRST': set(['AIR', 'EAST', 'NE', 'SIN', 'NIT', 'STAIN', 'INS', 'IS', 'TRAIN', 'SET', 'SER', 'TAS', 'ERA', 'ET', 'NET', 'TIS', 'STEARIN', 'EARN', 'ITS', 'ANE', 'RISE', 'EN', 'TEN', 'RES', 'TAN', 'RIA', 'SAT', 'RETINAS', 'ETA', 'AIT', 'RETSINA', 'TIE', 'TIN', 'RE', 'TAR', 'NA', 'AIS', 'SEA', 'RAIN', 'AI', 'SIT', 'STAIR', 'ENS', 'TEAR', 'ANTSIER', 'SEN', 'AN', 'ART', 'ANESTRI', 'ERS', 'IN', 'RAT', 'IRE', 'RETAINS', 'SENT', 'ATE', 'RIN', 'SEI', 'REST', 'SI', 'AR', 'STIR', 'REI', 'ANT', 'SEAT', 
'STAINER', 'SAE', 'ERN', 'AS', 'NEAR', 'RATINES', 'RAN', 'ARTS', 'TEA', 'ES', 'RAS', 'AIN', 'NAE', 'EAT', 'TAE', 'RAISE', 'NASTIER', 'TA', 'AT', 'EAR', 'ARE', 'ARS', 'RATE', 'TI', 'AE', 'ER', 'RET', 'ANI', 'SIR', 'SRI', 'IT']),
    'DRAMITC': set(['CAM', 'RIM', 'AIR', 'TAR', 'CAR', 'CAD', 'TIC', 'AID', 'AI', 'AD', 'MAR', 'ARC', 'AM', 'TAM', 'TAD', 'AR', 'MAC', 'MIR', 'CAT', 'DIM', 'TA', 'ARM', 'AT', 'MAD', 'MAT', 'MI', 'RAD', 'AMI', 'DAM', 'ACT', 'MID', 'RAM', 'ID', 'TI', 'ART', 'RIA', 'MA', 'RID', 'DIT', 'AIT', 'RAT', 'AIM', 'IT']),
    'ADEINRST': set(['AIR', 'EAST', 'NE', 'SIN', 'NIT', 'STAIN', 'INS', 'IS', 'DIN', 'TRAIN', 'AID', 'SET', 'SER', 'TAS', 'ERA', 'ET', 'NET', 'RAD', 'STEARIN', 'TIS', 'EARN', 'ITS', 'ANE', 'RISE', 'EN', 'TEN', 'RES', 'TAN', 'ANTIRED', 'RIA', 'SAID', 'SAT', 'ED', 'DINE', 'RETINAS', 'ETA', 'TRAINED', 'AIT', 'IDS', 'RETSINA', 'TIE', 'TIN', 'RE', 'TAR', 'NA', 'AIS', 'DETRAIN', 'AND', 
'SEA', 'RAISED', 'RAIN', 'IDEAS', 'AI', 'AD', 'SIT', 'INSTEAD', 'STAIR', 'ENS', 'TEAR', 'ANTSIER', 'SEN', 'AN', 'ART', 'SIDE', 'ANESTRI', 'ERS', 'DIT', 'IN', 'RAT', 'IRE', 'RED', 'RETAINS', 'DATE', 'SENT', 'ATE', 'END', 'TED', 'RIN', 'SAD', 'SEI', 'REST', 'SI', 'TAD', 'AR', 'STIR', 'READ', 'REI', 'RIDE', 'ANT', 'SEAT', 'STAINER', 'SAE', 'ID', 'ERN', 'DE', 'AS', 'NEAR', 'STAND', 'RATINES', 'TRIED', 'DIE', 'RID', 'RAN', 'ARTS', 'TEA', 'ES', 'RAS', 'AIN', 'DIS', 'NAE', 'EAT', 'TAE', 'ASIDE', 'ENDS', 'RAISE', 'IDEA', 'NASTIER', 'TA', 'SEND', 'TRADE', 'AT', 'DEN', 'DEAR', 'EAR', 'ARE', 'ARS', 'ADS', 'RATE', 'TI', 'AE', 'ER', 'RET', 'ANI', 'SIR', 'SRI', 'IT']),
    'ETAOIN': set(['TEA', 'TIE', 'TIN', 'NE', 'ONE', 'NA', 'NIT', 'AIN', 'TON', 'ON', 'NAE', 'ATE', 'EAT', 'TAE', 'AI', 'NOT', 'ION', 'OE', 'NO', 'TA', 'NOTE', 'OAT', 'AT', 'TO', 'TAO', 'ET', 'NET', 'ANT', 'ANE', 'AN', 'EN', 'TOE', 'TI', 'TEN', 'INTO', 'TAN', 
'AE', 'ANI', 'ETA', 'IN', 'EON', 'AIT', 'IT']),
    'SHRDLU': set(['URD', 'UH', 'SH', 'US']),
    'SHROUDT': set(['SOT', 'ODS', 'ROT', 'HOD', 'HOT', 'SO', 'UT', 'SOD', 'OUD', 'SHOT', 'DOS', 'HO', 'OR', 'OUT', 'SH', 'SOU', 'SHOUT', 'TOD', 'ORT', 'OUR', 'HUT', 'UH', 'HOUR', 'SHORT', 'OHS', 'ROD', 'THUS', 'DOR', 'DO', 'DOT', 'RUT', 'OH', 'TO', 'DUST', 'US', 'UTS', 'SORT', 'SOUTH', 'TOR', 'OS', 'URD', 'THO', 'OD', 'DUO', 'RHO', 'UDO', 'HOURS', 'ORS']),
    'TOXENSI': set(['XI', 'SOT', 'NIX', 'TIE', 'TIN', 'ES', 'NE', 'ONE', 'ONS', 'SO', 'NIT', 'SIN', 'INS', 'IS', 'NEXT', 'TON', 'SENT', 'ON', 'EX', 'SON', 'NOT', 'SEI', 'SI', 'SET', 'NOSE', 'ION', 'EXIST', 'SIT', 'SOX', 'OE', 'NO', 'OES', 'IT', 'OX', 'SEX', 'ONES', 'XIS', 'NOTE', 'ENS', 'TO', 'STONE', 'TIS', 'ET', 'NET', 'ITS', 'SEN', 'EN', 'TOE', 'TI', 'TEN', 'INTO', 'OS', 'SIX', 'NOS', 'IN', 'EON', 'OSE'])
}

def test_words():
    assert removed('LETTERS', 'L') == 'ETTERS'
    assert removed('LETTERS', 'T') == 'LETERS'
    assert removed('LETTERS', 'SET') == 'LTER'
    assert removed('LETTERS', 'SETTER') == 'L'
    t, results = timedcall(map, find_words, hands)
    for ((hand, expected), got) in zip(hands.items(), results):
        assert got == expected, "For %r, got %s, expected %s (diff %s)" % (
            hand, got, expected, expected ^ got
        )
    return t, 

print(test_words())
