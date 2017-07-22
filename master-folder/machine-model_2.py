import copy

memory = []

memory2 = [[[1],[[2],[[3]]],[[3],[[2]]]],[[2],[[1],[[3]]],[[3],[[1]]]],[[3],[[2],[[1]]],[[1],[[2]]]]]

states = [[1, 1], [2,1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]

simple_states = [[1, 1], [2,1], [3, 1]]

tree = {}

def create_tree(states):
    tree['0'] = states[:]


def grow_tree(tree):
    for k, v in sorted(tree.items()):
        indeces = int(k) + 1
        print(k + str(v))

def grow(tree, start, states):
    for i in range(0, len(states)):
        new_states = states[:]
        key = start + str(new_states.pop(i)[0])
        print(new_states)
        if len(new_states) > 0:
            tree[key] = new_states
        grow(tree, key, new_states)
