def mc_problem(start=(3,3,1,0,0,0), goal=None):
    """Solve the missionaries and connibals problem.
    State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
    Find a path that goes from the initial state to the goal state (which, if 
    not specified, is the state with no people or boats on the start sdie.)"""

    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]

    explored = set() # set of states we have visited
    frontier = [[start]] # ordered list of paths we have blazed

    while frontier:
        path = frontier.pop(0) # Pick up the first path left in frontier collection.
        s = path[-1] # fetch the current state of the path
        for (state, action) in csuccessors(s).items():
            if state not in explored: # if state is in explored, it is either in previously poped path, or in paths in frontier collection.
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)

    return []

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    if 0 < M1 < C1 or 0 < M2 < C2: return {}

    items = []
    if B1 > 0: # '->'
        items += [(sub(state, delta), a + '->')
                   for delta, a in deltas.items()]
    if B2 > 0: # '<-'
        items += [(add(state, delta), '<-' + a)
                   for delta, a in deltas.items()]
    return dict(items)


deltas = {
    (2, 0, 1,     -2, 0, -1): "MM",
    (0, 2, 1,      0,-2, -1): "CC",
    (1, 1, 1,     -1,-1, -1): "MC",
    (1, 0, 1,     -1, 0, -1): "M",
    (0, 1, 1,      0,-1, -1): "C",
}

def sub(X, Y):
    "add two vectors, X and Y."
    return tuple(x-y for x,y in zip(X, Y))

def add(X, Y):
    "subtract vector Y from X."
    return tuple(x+y for x,y in zip(X, Y))


print(mc_problem())