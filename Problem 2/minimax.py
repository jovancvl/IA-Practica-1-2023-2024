from state import *


def show_successors_of_state(s: State, successors: list[State]):
    print("Turn", s.turn, "with State:")
    s.show_state()
    print("Possible successors are:")
    for aux in successors:
        aux.show_state()
    print()


def minimax_alphabeta(curr_depth: int, max_depth: int, s: State, alpha: int, beta: int):
    if s.is_win() or curr_depth == max_depth:
        return s.calculate_value()
    elif s.turn == "A":
        """
        MAX function
        """
        successors = s.successors()
        show_successors_of_state(s, successors)
        for aux in successors:
            alpha = max(alpha, minimax_alphabeta(curr_depth + 1, max_depth, aux, alpha, beta))
            if alpha > beta:
                return alpha

        return alpha
    else:
        """
        MIN function
        """
        successors = s.successors()
        show_successors_of_state(s, successors)
        for aux in successors:
            beta = min(beta, minimax_alphabeta(curr_depth + 1, max_depth, aux, alpha, beta))
            if alpha > beta:
                return beta

        return beta


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
    minimax_alphabeta(0, m_d, initial_state, -1000, 1000)
