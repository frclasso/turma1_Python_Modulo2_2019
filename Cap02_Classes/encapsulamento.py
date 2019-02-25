#!/usr/bin/env python3

# encapsulamento

class Computer:

    def __init__(self):
        self.__maxprice = 900  #encapsular

    def sell(self):
        print('Selling price: US$ {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

macbook = Computer()
macbook.sell()

macbook.__maxprice = 1000 # Nao altera diretamente
macbook.sell()

macbook.setMaxPrice(2000)
macbook.sell()