from blocks import *


class State:
    def __init__(self, a: Block, b: Block, c: Block, g: int, parent, action_taken):
        self.a = a
        self.b = b
        self.c = c
        self.parent = parent
        self.action_taken = action_taken
        #self.valid_state()
        self.g = g
        self.h = self.calculate_h()
        self.actions = [
            (self.a, self.b),
            (self.a, self.c),
            (self.b, self.a),
            (self.b, self.c),
            (self.c, self.a),
            (self.c, self.b),
            (Block(Type.TABLE, Type.TABLE), self.a),
            (Block(Type.TABLE, Type.TABLE), self.b),
            (Block(Type.TABLE, Type.TABLE), self.c)
        ]

    def __eq__(self, other):
        if self.a.below == other.a.below and self.b.below == other.b.below and self.c.below == other.c.below:
            return True
        return False

    def __lt__(self, other):
        return self.get_f() < other.get_f()

    def get_f(self):
        return self.g + self.h

    def set_parent(self, parent):
        self.parent = parent

    def valid_state(self) -> bool:
        """
        check if what is below each block is valid

        not necessary? assume initial state is correct
        """

    def get_last_block(self, x: Block, y: Block):
        aux = []
        if x == self.a:
            aux.append(Type.A)
        elif x == self.b:
            aux.append(Type.B)
        else:
            aux.append(Type.C)

        if y == self.a:
            aux.append(Type.A)
        elif y == self.b:
            aux.append(Type.B)
        else:
            aux.append(Type.C)

        if Type.A not in aux:
            return self.a
        elif Type.B not in aux:
            return self.b
        else:
            return self.c

    def get_other_two(self, y: Block):
        if y == self.a:
            return self.b, self.c
        elif y == self.b:
            return self.a, self.c
        else:
            return self.a, self.b

    def valid_action(self, x: Block, y: Block) -> bool:
        """
        x goes below y
        """
        if x == Block(Type.TABLE, Type.TABLE):
            i, j = self.get_other_two(y)
            if i.below == y.name:
                """
                y below i
                """
                return False
            if j.below == y.name:
                """
                y below j
                """
                return False
        else:
            aux = self.get_last_block(x, y)
            if aux.below == x.name or aux.below == y.name:
                """
                x below aux
                y below aux
                """
                return False

        if x.below == y.name or y.below == x.name:
            """
            y below x
            x below y
            """
            return False

        return True

    def action(self, x: Block, y: Block):
        """
        only happens if the action is valid
        """
        new_a = None
        new_b = None
        new_c = None

        if x == self.a and y == self.b:
            new_b = Block(Type.B, Type.A)
        elif x == self.a and y == self.c:
            new_c = Block(Type.C, Type.A)
        elif x == self.b and y == self.a:
            new_a = Block(Type.A, Type.B)
        elif x == self.b and y == self.c:
            new_c = Block(Type.C, Type.B)
        elif x == self.c and y == self.a:
            new_a = Block(Type.A, Type.C)
        elif x == self.c and y == self.b:
            new_b = Block(Type.B, Type.C)
        elif x == Block(Type.TABLE, Type.TABLE) and y == self.a:
            new_a = Block(Type.A, Type.TABLE)
        elif x == Block(Type.TABLE, Type.TABLE) and y == self.b:
            new_b = Block(Type.B, Type.TABLE)
        elif x == Block(Type.TABLE, Type.TABLE) and y == self.c:
            new_c = Block(Type.C, Type.TABLE)

        if new_a is None:
            new_a = self.a
        if new_b is None:
            new_b = self.b
        if new_c is None:
            new_c = self.c

        return State(new_a, new_b, new_c, self.g+1, self, (x, y))

    def calculate_h(self):
        """
        h = how many misplaced blocks
        """
        count = 0
        if self.a.below != Type.B:
            count += 1
        if self.b.below != Type.C:
            count += 1
        if self.c.below != Type.TABLE:
            count += 1
        return count

    def successors(self):
        successors = []
        for a in self.actions:
            (x, y) = a
            if self.valid_action(x, y):
                new_state = self.action(x, y)
                successors.append(new_state)
        return successors  # (action, new state)

    def is_goal(self):
        if self.a.below == Type.B and self.b.below == Type.C and self.c.below == Type.TABLE:
            return True
        return False

    def show_state(self):
        print("State step", self.g)
        print("h =", self.h)
        print("f =", self.get_f())
        print("Action taken:", self.action_taken[1].name, "put on", self.action_taken[0].name) if self.action_taken is not None else print("Action taken: init State")
        print(self.a)
        print(self.b)
        print(self.c)
        print()

    def show_path(self):
        self.show_state()
        s = self.parent
        while s is not None:
            s.show_state()
            s = s.parent
