class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=16):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == "__main__":
    joao = Pessoa(nome='João')
    pedro = Pessoa(joao, nome='Pedro')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joao.olhos)
    print(pedro.olhos)
