import copy

memory = []

memory2 = [[[1],[[2],[[3]]],[[3],[[2]]]],[[2],[[1],[[3]]],[[3],[[1]]]],[[3],[[2],[[1]]],[[1],[[2]]]]]

states = [[1, 1], [2,1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]

simple_states = [[1, 1], [2,1], [3, 1]]

tree = {}

def create_tree(states):
    tree['0'] = states
    for i in range(0, len(states)):
        key = str(i + 1)
        new_states = states[:]
        new_states.pop(i)
        print(new_states)
        tree[key] = new_states

def grow_tree(tree):
    for k, v in sorted(tree.items()):
        indeces = int(k) + 1
        print(k + str(v))
