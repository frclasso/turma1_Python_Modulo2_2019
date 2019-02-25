

# modulo teste

numberone = 1
ageofqueen = 78


def printhello():
    print('Hello')


def timesfour(input):
    print(input * 4)


class Piano:

    def __init__(self):
        self.type = input('What type of piano?')
        self.height = input('What height?')
        self.price = input('How much did it cost?')
        self.age = input('How old is it?')

    def details(self):
        print('This piano is a/an '+ self.height + 'foot.')
        print(self.type, 'piano, '+ self.age, 'years old and costing '
              + self.price + " dolars.")