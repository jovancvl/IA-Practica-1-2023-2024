from state import *


def show_successors_of_state(s: State, successors: list[State]):
    print("Turn", s.turn, "with State:")
    print(s)
    print("Possible successors are:")
    for aux in successors:
        print(aux)
    print()


def minimax(curr_depth: int, max_depth: int, s: State):
    if s.is_win() or curr_depth == max_depth:
        return s.calculate_value()
    elif s.turn == "A":
        """
        MAX function
        """
        value = -1000
        successors = s.successors()

        for aux in successors:
            value = max(value, minimax(curr_depth + 1, max_depth, aux))

        s.set_value(value)
        show_successors_of_state(s, successors)
        return value
    else:
        """
        MIN function
        """
        value = 1000
        successors = s.successors()

        for aux in successors:
            value = min(value, minimax(curr_depth + 1, max_depth, aux))

        s.set_value(value)
        show_successors_of_state(s, successors)
        return value


if __name__ == '__main__':
    m_d = 6

    print("Player A starting position: [0-4]")
    p1_starting_pos = int(input())
    print("Player B starting position: [0-4]")
    p2_starting_pos = int(input())

    p1 = Player("A", p1_starting_pos)
    p2 = Player("B", p2_starting_pos)

    initial_state = State(p1, p2, "A", None)
    # initial_state.show_state()
    # print(initial_state)
    minimax(0, m_d, initial_state)
