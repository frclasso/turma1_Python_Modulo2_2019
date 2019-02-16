

"""Desenvolver uma aplicação de cadastro de funcionarios"""


class PessoaFisica:
    #variaveis
    def __init__(self, nome,sobrenome, idade,identidade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.identidade = identidade
        self.cpf = cpf
        self.email = nome + '.' + sobrenome + '@empresa.coom.br'


# herança
class Gerente(PessoaFisica):
    pass


class Programadores(PessoaFisica):
    pass

class Secretaria(PessoaFisica):
    pass