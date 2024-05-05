"""

NOTES

store element and what is below it

3 lines of input, the element and what is below it

f = g + h
g = current step towards solution
h = number of elements not placed correctly (if the block below it is incorrect)

1 list of visited states
1 list of states to visit

Block class that contains info about the block (a, b, c) and information around it (above, below it)
State class that inherits the block class and adds f, g and h to it, as well as parent state

possible actions are:
    put block x below block y
        can only put x below y if:
            a) y isn't below a block already
            b) x isn't below a block already
    put ground below block x

"""
from queue import PriorityQueue
from state import *


def parse_input(below_a: str, below_b: str, below_c: str):
    a = Block(Type.A, Type.TABLE)
    b = Block(Type.B, Type.TABLE)
    c = Block(Type.C, Type.TABLE)

    if below_a == "B":
        a.set_below(Type.B)
    elif below_a == "C":
        a.set_below(Type.C)
    else:
        a.set_below(Type.TABLE)

    if below_b == "A":
        b.set_below(Type.A)
    elif below_b == "C":
        b.set_below(Type.C)
    else:
        b.set_below(Type.TABLE)

    if below_c == "A":
        c.set_below(Type.A)
    elif below_c == "B":
        c.set_below(Type.B)
    else:
        c.set_below(Type.TABLE)

    return State(a, b, c, 0, None, None)


def state_in_q(s: State, q: PriorityQueue):
    for (priority, aux_state) in q.queue:
        if s == aux_state:
            return True
    return False


def expand(s: State, v: list, q: PriorityQueue):
    successors = s.successors()
    for new_state in successors:
        if state_in_q(new_state, q) or new_state in v:
            continue
        q.put((new_state.get_f(), new_state))


def a_star(s: State, v: list, q: PriorityQueue) -> State:
    q.put((s.get_f(), s))

    while not q.empty():
        priority, curr_state = q.get()
        if curr_state.is_goal():
            return curr_state
        v.append(curr_state)
        expand(curr_state, v, q)

    raise Exception("No solution found")


if __name__ == '__main__':
    visited = list()
    queueueue = PriorityQueue()

    print("What element is below A? B C or T")
    below_a = input()
    print("What element is below B? A C or T")
    below_b = input()
    print("What element is below C? A B or T")
    below_c = input()

    init_state = parse_input(below_a.upper(), below_b.upper(), below_c.upper())
    #init_state = parse_input("B", "TABLE", "A")
    #init_state.show_state()
    sol = a_star(init_state, visited, queueueue)
    sol.show_path()

