# File 7
from decorator import decorator

# Cache Management: Memoization
@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up.
    """
    cache = {}
    def _f(*args):
        try: 
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            # i.e. args are not hashable.
            return f(*args) # Perter's mistake here
    return _f


@decorator
def countcalls(f):
    "Decorator that makes the function count calls to it, in callcounts[f]"
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

if __name__ == '__main__':
    callcounts = {}

    @countcalls
    def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

    print("%s %10s %10s %10s" % ('n', 'fib(n)', 'calls', 'call ratio'))
    for n in range(20):
        prev_counts = callcounts[fib]
        value_n = fib(n+1)
        print("%2s %10s %10s %5.4f" % (n+1, value_n, callcounts[fib], callcounts[fib] / prev_counts if prev_counts != 0 else 1))
        callcounts[fib] = 0

    @countcalls
    @memo
    def fib_memo(n): return 1 if n <= 1 else fib_memo(n-1) + fib_memo(n-2)

    print("%s %10s %10s %10s" % ('n', 'fib_memo(n)', 'calls', 'call ratio'))
    for n in range(20):
        prev_counts = callcounts[fib_memo]
        value_n = fib_memo(n+1)
        print("%2s %10s %10s %5.4f" % (n+1, value_n, callcounts[fib_memo], callcounts[fib_memo] / prev_counts if prev_counts != 0 else 1))
