
class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.type  = "Cell"

    def __str__(self):
        return "Cell at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Cell at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.alive == other.alive

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y, self.alive))

class Vegetob(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Vegetob"

    def __str__(self):
        return "Vegetob at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Vegetob at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead") 

class Erbast(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Erbast"

    def __str__(self):
        return "Erbast at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Erbast at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

class Carviz(Cell):
    def __init__(self, x, y, alive):
        super().__init__(x, y, alive)
        self.type = "Carviz"

    def __str__(self):
        return "Carviz at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")

    def __repr__(self):
        return "Carviz at ({}, {}) is {}".format(self.x, self.y, "alive" if self.alive else "dead")
