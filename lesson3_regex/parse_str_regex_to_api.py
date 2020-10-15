# File 14
# Unit 3 Homework: parse/convert str regular expression to API 
REGRAMMAR = grammar("""
""", whitespace='')

def parse_re(pattern):
    return convert(parse('RE', pattern, REGRAMMAR))

def convert(tree):
    ## your conde here

