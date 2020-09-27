# File 8

from decorator import decorator

# -- write a decorator for 
@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level*indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('%s<-- %s === %s' % ( (trace.level - 1)* indent, signature, result))
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f


@trace
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)


if __name__ == "__main__":
    fib(6)