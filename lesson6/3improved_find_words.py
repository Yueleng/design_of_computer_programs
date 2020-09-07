def readwordlist(filename):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename, 'r') # opens file
    text = file.read()    # gets file into string
    # your code here
    prefixset = set([])
    wordset = set(text.upper().split())
    for word in wordset:
        wordPrefixes = set([word[:i] for i in range(len(word))])
        prefixset = prefixset.union(wordPrefixes)
    return wordset, prefixset
    
WORDS, PREFIXES = readwordlist(r"C:\Users\Yueleng\OneDrive\CS212\lesson6\words4k.txt")

def find_words(hand):
    "Find all words that can be made from the letters in hand."
    results = set()
    for a in hand:
        if a in WORDS: results.add(a)
        if a not in PREFIXES: continue
        for b in removed(hand, a):
            w = a + b
            if w in WORDS: results.add(w)
            if w not in PREFIXES: continue
            for c in removed(hand, w):
                w = a+b+c
                if w in WORDS: results.add(w)
                if w not in PREFIXES: continue
                for d in removed(hand, w):
                    w = a+b+c+d
                    if w in WORDS: results.add(w)
                    if w not in PREFIXES: continue
                    for e in removed(hand, w):
                        w = a+b+c+d+e
                        if w in WORDS: results.add(w)
                        if w not in PREFIXES: continue
                        for f in removed(hand, w):
                            w = a+b+c+d+e+f
                            if w in WORDS: results.add(w)
                            if w not in PREFIXES: continue
                            for g in removed(hand, w):
                                w = a+b+c+d+e+f+g
                                if w in WORDS: results.add(w)
                                if w not in PREFIXES: continue
    return results

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

