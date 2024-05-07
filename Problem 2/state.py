from player import *


class State:
    def __init__(self, p1: Player, p2: Player, turn: str, parent):
        self.p1 = p1
        self.p2 = p2
        self.turn = turn
        self.parent = parent
        self.MIN_POS = 0
        self.MAX_POS = 4
        self.value = self.calculate_value()

    def is_win(self):
        return self.p1.pos == self.MAX_POS or self.p2.pos == self.MIN_POS

    def set_value(self, value):
        self.value = value

    def calculate_value(self):
        d_min = self.p2.pos
        d_max = self.MAX_POS - self.p1.pos
        if d_min == 0:
            return -1000
        if d_max == 0:
            return 1000
        return d_min - d_max

    def get_players_turn(self):
        if self.turn == "A":
            return self.p1, self.p2
        else:
            return self.p2, self.p1

    def successors(self):
        moves = []

        a, b = self.get_players_turn()

        if a.pos + 1 == b.pos:
            if a.pos + 2 <= self.MAX_POS:
                moves.append(2)
        elif a.pos + 1 <= self.MAX_POS:
            moves.append(1)

        if a.pos - 1 == b.pos:
            if a.pos - 2 >= self.MIN_POS:
                moves.append(-2)
        elif a.pos - 1 >= self.MIN_POS:
            moves.append(-1)

        successors = []

        for m in moves:
            p1 = None
            p2 = None
            if a.kind == "A":
                p1 = Player("A", a.pos + m)
                p2 = b
            else:
                p1 = b
                p2 = Player("B", a.pos + m)
            new_state = State(p1, p2, "B" if a.kind == "A" else "A", self)
            successors.append(new_state)

        return successors

    def __str__(self):
        s = ["_"] * 5
        s[self.p1.pos] = "A"
        s[self.p2.pos] = "B"
        output = "[ "
        for a in s:
            output += a + " "
        output += "]"
        output += " e = " + str(self.value)
        return output
