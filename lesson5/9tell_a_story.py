from functools import update_wrapper
from collections import defaultdict
goal = 40
states = [(0, me, you, pending)
            for me in range(41) 
            for you in range(41) 
            for pending in range(41)
            if me + pending <= goal]

other = {1:0, 0:1}

r = defaultdict(lambda: [0, 0])
r[100][0] = 2
r[100][1] = 3
r[200][1] = 1
r[200][0] = 5


for (delta, (wrolls, drolls)) in sorted(r.items()):
    print('%4d: %3d %3d' % (delta, wrolls, drolls))

def story():
    r = defaultdict(lambda: [0, 0])
    for s in states:
        w, d = max_wins(s), max_diffs(s)
        if w != d:
            _, _, _, pending = s
            i = 0 if (w == 'roll') else 1
            r[pending][i] += 1
    for (delta, (wrolls, drolls)) in sorted(r.items()):
        print('%4d: %3d %3d' % (delta, wrolls, drolls))


# help function
def max_wins(state):
    "The optimal pig strategy chooses an action with the highest win probability."
    return best_action(state, pig_actions, Q_pig, Pwin)

def max_diffs(state):
    """A strategy that maximizes the expected difference between my final score
    and my opponent's."""
    return best_action(state, pig_actions, Q_pig, win_diff)

def best_action(state, actions, Q, U):
    "Return the optimal action for a state, given U."
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU)

def pig_actions(state):
    "The legal actions from a state."
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']


def Q_pig(state, action, Pwin):  
    "The expected value of choosing action in state."
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    raise ValueError

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)





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

@memo
def win_diff(state):
    "The utility of a state: here the winning differential (pos or neg)."
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q_pig(state, action, win_diff)
                   for action in pig_actions(state))

story()                   