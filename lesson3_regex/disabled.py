# File 9
from trace import trace

def disabled(f): return f
trace = disabled

@trace
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)



if __name__ == "__main__":
    fib(5)
