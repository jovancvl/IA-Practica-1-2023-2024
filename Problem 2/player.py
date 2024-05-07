class Player:
    def __init__(self, kind: str, pos: int):
        self.kind = kind
        self.pos = pos

    def __eq__(self, other):
        return self.kind == other.kind

    def __str__(self):
        return self.kind + " pos " + str(self.pos)

    def set_pos(self, pos):
        self.pos = pos


