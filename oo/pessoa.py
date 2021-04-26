class Pessoa:
    def __init__(self, *filhos, nomme = None, idade = 35):
        self.idade = idade
        self.nome = nomme
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    borel = Pessoa(nomme='SHIELD')
    acorde = Pessoa(nomme = 'MARVEL')
    corel = Pessoa(nomme='RLD')
    adobe = Pessoa(corel, borel, acorde, nomme='AGT')
    print(Pessoa.cumprimentar(adobe))
    print(id(adobe))
    print(adobe.cumprimentar())
    print(adobe.nome)
    print(adobe.idade)
    for filho in adobe.filhos:
        print(filho.nome)