# -----------------
# User Instructions
# 
# Write a function, extend_prefix, nested in find_words,
# that checks to see if the prefix is in WORDS and 
# adds that to results if it is.
#
# If not, your function should check to see if the prefix
# is in PREFIXES, and if it is should recursively add letters
# until the prefix is no longer valid.

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def readwordlist(filename):
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset
    
WORDS, PREFIXES = readwordlist(r"C:\Users\Yueleng\OneDrive\CS212\lesson6\words4k.txt")

def find_words(letters):
    results = set()

    def extend_prefix(w, letters):
        if w in WORDS: results.add(w)
        if w not in PREFIXES: return
        for L in letters:
            extend_prefix(w+L, removed(letters, L))

    extend_prefix('', letters)
    return results

## Flatten Version
def find_words_f(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)

## Alternative

def find_words_al(letters, pre='', results=None):
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words_al(pre+L, letters.replace(L, '', 1), results)