import doctest

class TestBrdige: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

"""


def bsuccessors(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light, and t is a number indicating the elapsed time."""
    here, there, t = state
    if 'light' in here:
        return dict(((here  - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a,b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')  
        
def elapsed_time(path):
    return path[-1][2]

def bridge_problem(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    ## modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        if path[-1][0] == set(['light']) or not path[-1][0]:  ## That is, nobody left here
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                # Don't check for solution when we extend a path
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
                
                
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


print(doctest.testmod())