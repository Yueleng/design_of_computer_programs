# File 11
from general_parser import grammar

URL = grammar("""
url => httpaddress | ftpaddress | mailtoaddress
httpaddress => http:// hostport /path? ?search?
ftpaddress => ftp:// login / path ; ftptype | ftp:// login / path
/path? => / path | ()
?search? => [?] search | ()
mailtoaddress => mailto: xalphas @ hostname
hostport => host : port | host
host => hostname | hostnumber
hostname => ialpha . hostname | ialpha
hostnumber => digits . digits . digits . digits
ftptype => A formcode | E formcode | I | L digits
formcode => [NTC]
port => digits | path
path => void | segment / path | segment
segment => xalphas
search => xalphas + search | xalphas
login => userpassword hostport | hostport
userpassword => user : password @ | user @
user => alphanum2 user | alphanum2
password => alphanum2 password | password
void => ()
digits => digit digits | digit
digit => [0-9]
alpha => [a-zA-Z]
safe => [-$_@.&+]
extra => [()!*''""]
escape => % hex hex
hex => [0-9a-fA-F]
alphanum => alpha | digit
alphanums => alphanum alphanums | alphanum
alphanum2 => alpha | digit | [-_.+]
ialpha => alpha xalphas | alpha
xalphas => xalpha xalphas | xalpha
xalpha => alpha | digit | safe | extra | escape
""", whitespace='()')

def verify(G):
    lhstokens = set(G) - set([' ']) # set(G) collects the keys of dictionary G
    rhstokens = set(t for alts in G.values() for alt in alts for t in alt)
    def show(title, tokens): print(title, '=', ' '.join(sorted(tokens)))
    show('Non-Terms', G)
    show('Terminals', rhstokens - lhstokens)
    show('Suspects', [t for t in (rhstokens - lhstokens) if t.isalnum()])
    show('Orphans  ', lhstokens - rhstokens)

if __name__ == '__main__':
    verify(URL)