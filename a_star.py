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

def is_goal(state):
    return state["A"] == "B" and state["B"] == "C" and state["C"] == "table"


def can_take_action(state):



def a_star():
    if is_goal(state):
        show_state(state)
    else:

def parse_input(data):
    result = {"A": data[0][1], "B": data[1][1], "C": data[2][1], "parent": None, "g": 0}
    result["h*"] = get_h(result)
    result["f*"] = result["g"] + result["h*"]
    return result

def show_state(data: dict):
    print("Step: ", data["g"])
    print("A |", data["A"])
    print("B |", data["B"])
    print("C |", data["C"])
    print()


def get_h(data: dict):
    count = 0
    if data["A"] != "B":
        count += 1
    if data["B"] != "C":
        count += 1
    if data["C"] != "table":
        count += 1
    return count


if __name__ == '__main__':
    state = {
        "A": "table",
        "B": "table",
        "C": "table",
        "parent": None,
        "g": 0,
        "h*": 0,
        "f*": 0
    }
    previous_states = []
    q = PriorityQueue()  # tuple (priority, state)
    print("Input the initial state 1 line per element indicating the element and what is below it")
    print("Example:\n A table\n B C\n C table")
    print("This is the example state:")
    print("  B\nA C\n")

    raw_data = []
    for i in range(3):
        element, what_is_below = input().strip().split()
        raw_data.append((element, what_is_below))

    state = parse_input(raw_data)

    show_state(state)
