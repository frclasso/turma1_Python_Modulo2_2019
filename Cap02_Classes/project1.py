

"""Desenvolver uma aplicação de cadastro de funcionarios"""


class PessoaFisica:
    #variaveis
    def __init__(self, nome,sobrenome, idade,identidade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.identidade = identidade
        self.cpf = cpf
        #self.email = nome + '.' + sobrenome + '@empresa.coom.br'

    def email(self):
        pass

    def fullname(self):
        pass

    def aumento(self):
        pass

# herança
class Gerente(PessoaFisica):
    def __init__(self, nome,sobrenome, idade,identidade, cpf,sala):
        super().__init__(nome, sobrenome,idade, identidade, cpf)
        self.sala = sala


class Programadores(PessoaFisica):
    def __init__(self, nome,sobrenome, idade,identidade, cpf,linguagem):
        super().__init__(nome, sobrenome,idade, identidade, cpf)
        self.linguagem = linguagem


class Secretaria(PessoaFisica):
    def __init__(self, nome,sobrenome, idade,identidade, cpf,idioma):
        super().__init__(nome, sobrenome,idade, identidade, cpf)
        self.idioma = idioma


# instanciem objetos
# criem metodos
