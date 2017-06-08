import copy

memory = []

memory2 = [[[1],[[2],[[3]]],[[3],[[2]]]],[[2],[[1],[[3]]],[[3],[[1]]]],[[3],[[2],[[1]]],[[1],[[2]]]]]

states = [[[1, 1]], [[2,1]], [[3, 1]], [[4, 1]], [[5, 1]], [[6, 1]], [[7, 1]], [[8, 1]], [[9, 1]]]

simple_states = [[[1, 1]], [[2,1]], [[3, 1]]]

def append_states_to_mem(memory2, states2):
    memory2 = copy.deepcopy(states2)
    s1 = copy.deepcopy(states2)
    loop_states(memory2, s1)
    return memory2

v = 1
def loop_states(memory1, states1):
    global v
    for i in range(0, len(states1)):
        s2 = []

        if i == 0:
            s2 = states1[i + 1: len(states1)]
        elif i == len(states1) - 1:
            s2 = states1[0:len(states1)]
        else:
            for n in range(0, len(states1)):
                if i != n:
                    s2.append(states1[n])
        if len(s2) > 0:
            memory1[i].append(s2)
        print(memory1[i])
        print(i)
        print("v = " + str(v))
        v +=1
        try:
            loop_states(memory1[i][1], memory1[i][1])
        except IndexError:
            break
        else:
            break

memory = append_states_to_mem(memory, simple_states)

print(memory)

[[[1, 1], [[[2, 1], [[[3, 1]]]], [[3, 1]]]], [[2, 1]], [[3, 1]]]
