class Pessoa:

    olhos = 2   # ATRIBUTOS DE CLASSE

    def __init__(self, *filhos, nome=None, idade=16):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nomes_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):   # HOMEM HERDA DE PESSOA TODOS OS SEUS ATRIBUTOS E MÉTODOS
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Homem):
    olhos = 3

if __name__ == "__main__":
    joao = Homem(nome='João')
    pedro = Mutante(joao, nome='Pedro')
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Santos'
    del pedro.filhos
    pedro.olhos = 1
    print(pedro.__dict__)
    print(joao.__dict__)
    del pedro.olhos
    print(Pessoa.olhos)
    print(joao.olhos)
    print(pedro.olhos)
    print(Pessoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pessoa.nomes_e_atributos_de_classe(), pedro.nomes_e_atributos_de_classe())
