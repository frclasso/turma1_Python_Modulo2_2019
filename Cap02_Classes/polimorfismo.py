#!/usr/bin/env python3

# Polimorfismo

class Papagaio:

    def fly(self):
        print('Papagaio pode voar!')

    def swim(self):
        print('Papagaio NAO pode nadar!')


class Pinguim:

    def fly(self):
        print('Pinguim NAO pode voar!')

    def swim(self):
        print('Pinguim sabe nadar rápido!')


# interface teste comum  a ambas as classes
def flying_test(bird):
    bird.fly()


def swim_test(bird):
    bird.swim()

# intanciar obejtos
blue = Papagaio()
peggy = Pinguim()

# testando
flying_test(blue)
flying_test(peggy)

swim_test(blue)
swim_test(peggy)
