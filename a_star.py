"""

NOTES

store element and what is below it

3 lines of input, the element and what is below it

"""


def show_state(data: dict):
    return


if __name__ == '__main__':
    data = {
        "A": "table",
        "B": "table",
        "C": "table",
    }
    print("Input the initial state 1 line per element indicating the element and what is below it")
    print("Example:\n A table\n B C\n C table")
    print("This is the example state:")
    print("  B\nA C")
    for i in range(3):
        element, what_is_below = input().strip().split()
        data[element] = what_is_below
