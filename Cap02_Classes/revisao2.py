# classes

class Humanos:

    # variaveis de classe
    tempo_de_vida = 10

    # construtor de classe, define as variaveis
    def __init__(self, nome, idt, cpf, telefone):
        self.nome = nome
        self.identidade = idt
        self.cpf = cpf
        self.tel = telefone
        self.__salarioMinimo = 960.00 # encapsular

    def obterSalario(self):
        print("Salario :R${}".format(self.__salarioMinimo))

    def setSalario(self, salario):
        self.__salarioMinimo = salario


#Heranca - classe herda parametros
class Gerente(Humanos):
    def __init__(self, nome, idt, cpf, telefone, seção):
        super().__init__(nome, idt,cpf, telefone)
        self.secao = seção


pessoa = Humanos('Fabio', 123456, '345.567.667.89', '(48)999988877')

gerente_1 = Gerente('John', 12345, '444.555.678', "(48)3334445", 'Marketing')


print(pessoa.nome)
print(pessoa.identidade)
print(pessoa.cpf)
print(pessoa.tel)
print(pessoa.tel)
pessoa.obterSalario()
pessoa.setSalario(1000.00)
pessoa.obterSalario()


print(gerente_1.nome)
print(gerente_1.secao)
gerente_1.obterSalario()
gerente_1.setSalario(2000)
gerente_1.obterSalario()