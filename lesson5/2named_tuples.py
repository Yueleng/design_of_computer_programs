from collections import namedtuple
State = namedtuple('state', 'p me you pending')

def hold(state):
    return State(other[state.p], state.you, state.me + state.pending, 0)

def roll(state, d):
    if d == 1:    
        return State(other[state.p], state.you, state.me + 1, 0)
    else:
        return State(state.p, state.me, state.you, state.pending + d)

other = {0: 1, 1:0}


def test():
    assert hold(State(1, 10, 20, 7))    == State(0, 20, 17, 0)
    assert hold(State(0, 5, 15, 10))    == State(1, 15, 15, 0)
    assert roll(State(1, 10, 20, 7), 1) == State(0, 20, 11, 0)
    assert roll(State(0, 5, 15, 10), 5) == State(0, 5, 15, 15)
    return 'tests pass'

print(test())