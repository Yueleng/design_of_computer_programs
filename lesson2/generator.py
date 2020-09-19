def sq(x): print('sq called ' +  str(x)); return x * x

g = (sq(x) for x in range(10) if x % 2 == 0)
print(g)

next(g)
next(g)
next(g)
next(g)
next(g)
# next(g) # raises StopIteration exception


for x2 in (sq(x) for x in range(10) if x % 2 == 0): pass

print(list((sq(x) for x in range(10) if x % 2 == 0)))