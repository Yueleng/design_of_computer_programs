# File 5

# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

from functools import update_wrapper
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # Wrong Solution:
        # if len(args) == 0:
        #     return f(x)
        # elif len(args) == 1:
        #     return f(x, args[0])
        # else:
        #     return n_ary_f(n_ary_f(x, args[0]),*args[1:])
        return x if not args else f(x, n_ary_f(*args))
    # if there was any documentation string for sequence, that would appear here as well.
    # Without update_wrapper, the helper function will display: n_ary_f(x, *args)
    # Helps in debugging, doesn't really help in execution
    update_wrapper(n_ary_f, f)
    return n_ary_f



# In fact this pattern is so common in Python that there's a special notation for it: @n_ary, a decorator notation.
# def seq(x, y): return ('seq', x, y)
# seq = n_ary(seq)

@n_ary
def seq(x, y): return ('seq', x, y)

help(seq)