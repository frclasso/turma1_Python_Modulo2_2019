

class Pai:

    def __init__(self):
        print("Construtor da classe Pai")
        self.x = 1000


class Filha:

    def __init__(self):
        print('Construtor da classe Filha')
        Pai.__init__(self)  # classe derivada
        self.y = 500


class Neta(Pai):  # heranca

    def __init__(self):
        super().__init__()
        print('Classe neta')


f = Filha()
print(f.x)
print(f.y)

n = Neta()
print(n.x)