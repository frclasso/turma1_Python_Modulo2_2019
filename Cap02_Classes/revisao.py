#!/usr/bin/env python3


# revisao

# declaracao da classe
class Pessoa_Fisica:

    idade = 40 # variaveis de classe

    def __init__(self, nome, sobrenome, salario): # construtor de classe, inicializa as var
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    def nome_completo(self): # metodo de classe
        return '{} {}'.format(self.nome, self.sobrenome)


class Desenvolvedor(Pessoa_Fisica): # herança

    def __init__(self, nome, sobrenome, salario, linguagem):
        super().__init__(nome, sobrenome,salario) # construtor da classe Pai
        self.linguagem = linguagem


# instancia de classe
fabio = Pessoa_Fisica('Fabio', 'Classo', 5000)
homem_aranha = Pessoa_Fisica('Peter', 'Parker', 20000)

kevin = Desenvolvedor('Kevin', 'Mitnick', 1000000, 'Python')

print(fabio.idade)
print(fabio.nome)
print(fabio.sobrenome)
print(fabio.salario)

print(f'{fabio.nome_completo()} tem {fabio.idade} anos')
print(kevin.nome_completo())