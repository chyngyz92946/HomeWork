

class Figure():
    def __init__(self):
        pass
    def P(self):
        pass
    def S(self):
        pass

class Triangle(Figure):

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def P(self):
        p = self.a + self.b + self.c
        print('Периметр равен: ' + str(p))

    def S(self):
        s = self.a * self.b / 2
        print('Площадь равна: ' + str(s))


tr = Triangle(5, 5, 5)
tr.P()
tr.S()
