# -----------------
# User Instructions
# 
# Write the max_wins function. You can make your life easier by writing
# it in terms of one or more of the functions that we've defined! Go
# to line 88 to enter your code.

from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

other = {1:0, 0:1}

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def Q_pig(state, action, Pwin):  
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError

def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def pig_actions(state):
    "The legal actions from a state."
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']


goal = 40

@memo
def Pwin(state):
    """The utility of a state; here just the probability that an optimal player
    whose turn it is to move can win from the current state."""
    # Assume opponent also plays with optimal strategy.
    (p, me, you, pending) = state
    if me + pending >= goal:
        return 1
    elif you >= goal:
        return 0
    else:
        return max(Q_pig(state, action, Pwin)
                for action in pig_actions(state))

def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)


def test():
    assert(max_wins((1, 5, 34, 4)))   == "roll"
    assert(max_wins((1, 18, 27, 8)))  == "roll"
    assert(max_wins((0, 23, 8, 8)))   == "roll"
    assert(max_wins((0, 31, 22, 9)))  == "hold"
    assert(max_wins((1, 11, 13, 21))) == "roll"
    assert(max_wins((1, 33, 16, 6)))  == "roll"
    assert(max_wins((1, 12, 17, 27))) == "roll"
    assert(max_wins((1, 9, 32, 5)))   == "roll"
    assert(max_wins((0, 28, 27, 5)))  == "roll"
    assert(max_wins((1, 7, 26, 34)))  == "hold"
    assert(max_wins((1, 20, 29, 17))) == "roll"
    assert(max_wins((0, 34, 23, 7)))  == "hold"
    assert(max_wins((0, 30, 23, 11))) == "hold"
    assert(max_wins((0, 22, 36, 6)))  == "roll"
    assert(max_wins((0, 21, 38, 12))) == "roll"
    assert(max_wins((0, 1, 13, 21)))  == "roll"
    assert(max_wins((0, 11, 25, 14))) == "roll"
    assert(max_wins((0, 22, 4, 7)))   == "roll"
    assert(max_wins((1, 28, 3, 2)))   == "roll"
    assert(max_wins((0, 11, 0, 24)))  == "roll"
    return 'tests pass'

print(test())

@memo
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                   for action in pig_actions(state))

def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)

def test():
    # The first three test cases are examples where max_wins and
    # max_diffs return the same action.
    assert(max_diffs((1, 26, 21, 15))) == "hold"
    assert(max_diffs((1, 23, 36, 7)))  == "roll"
    assert(max_diffs((0, 29, 4, 3)))   == "roll"
    # The remaining test cases are examples where max_wins and
    # max_diffs return different actions.
    assert(max_diffs((0, 36, 32, 5)))  == "roll"
    assert(max_diffs((1, 37, 16, 3)))  == "roll"
    assert(max_diffs((1, 33, 39, 7)))  == "roll"
    assert(max_diffs((0, 7, 9, 18)))   == "hold"
    assert(max_diffs((1, 0, 35, 35)))  == "hold"
    assert(max_diffs((0, 36, 7, 4)))   == "roll"
    assert(max_diffs((1, 5, 12, 21)))  == "hold"
    assert(max_diffs((0, 3, 13, 27)))  == "hold"
    assert(max_diffs((0, 0, 39, 37)))  == "hold"
    return 'tests pass'

print(test())


## Using Tools to compare Pwin and max_diff
states = [(0, me, you, pending)
            for me in range(41) 
            for you in range(41) 
            for pending in range(41)
            if me + pending <= goal]
print(len(states))

from collections import defaultdict
r = defaultdict(int)

for s in states: r[max_wins(s), max_diffs(s)] += 1

print(dict(r))

print((3975 + 381) / 35301)