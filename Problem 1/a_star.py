"""

NOTES

store element and what is below it

3 lines of input, the element and what is below it

f = g + h
g = current step towards solution
h = number of elements not placed correctly (if the block below it is incorrect)

1 list of visited states
1 list of states to visit

Block class that contains info about the block (a, b, c) and what is below it
State class that inherits the block class and adds f, g and h to it, as well as parent state and action taken since the parent state

possible actions are:
    put block x below block y
        can only put x below y if:
            a) y isn't below a block already
            b) x isn't below a block already
    put ground below block x
        can only put ground below x if:
            a) x isn't below one of the other 2 blocks

at first only PriorityQueue works
    DFS - stack / LIFO
    BFS - queue / FIFO


"""
from queue import PriorityQueue, LifoQueue, Queue
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


def state_in_q(s: State, q):
    if type(q) == PriorityQueue:
        for (priority, aux_state) in q.queue:
            if s == aux_state:
                return True
        return False
    else:
        for aux_state in q.queue:
            if s == aux_state:
                return True
        return False

def add_to_q(s: State, q):
    if type(q) == PriorityQueue:
        q.put((s.get_f(), s))
    else:
        q.put(s)


def get_from_q(q):
    if type(q) == PriorityQueue:
        p, s = q.get()
        return p, s
    else:
        return None, q.get()


def expand(s: State, v: list, q):
    successors = s.successors()
    for new_state in successors:
        if state_in_q(new_state, q) or new_state in v:
            continue
        add_to_q(new_state, q)


def a_star(s: State, v: list, q, depth_limit: int) -> State:
    # add state to queue
    add_to_q(s, q)

    while not q.empty():
        # get next state
        _, curr_state = get_from_q(q)
        if curr_state.is_goal() or curr_state.g == depth_limit:
                return curr_state

        v.append(curr_state)
        expand(curr_state, v, q)

        print("---------------------------------------------------\nSTEP", curr_state.g)

        print("Visited list:")
        for aux in v:
            aux.show_state()
        print()
        print("Expanded list:")
        if type(q) == PriorityQueue:
            for (_, aux) in q.queue:
                aux.show_state()
        else:
            for aux in q.queue:
                aux.show_state()

    raise Exception("No solution found")


if __name__ == '__main__':
    visited = list()
    queueueue = PriorityQueue()
    #queueueue = Queue()
    #queueueue = LifoQueue()
    d_l = -1

    print("What element is below A? B C or T")
    below_a = input()
    print("What element is below B? A C or T")
    below_b = input()
    print("What element is below C? A B or T")
    below_c = input()

    init_state = parse_input(below_a.upper(), below_b.upper(), below_c.upper())
    # init_state = parse_input("B", "TABLE", "A")
    # init_state.show_state()
    sol = a_star(init_state, visited, queueueue, d_l)
    print("Solution is:")
    sol.show_path()
