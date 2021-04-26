class Pessoa:                   #classe
    olhos = 2                   #atributo de classe

    def __init__(self, *filhos, nomme = None, idade = 35): #Objeto com atributos sendo *filhos um atributo complexo
        self.idade = idade                #Variáveis do objeto
        self.nome = nomme                 #Variáveis do objeto
        self.filhos = list(filhos)        #Variável complexa do objeto

    def cumprimentar(self):    #método
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
    adobe.sobrenome = 'RML'
    print(adobe.__dict__)
    del adobe.filhos
    adobe.olhos = 1
    del adobe.olhos
    print(adobe.__dict__)
    print(borel.__dict__)
    print(Pessoa.olhos)
    print(adobe.olhos)
    print(corel.olhos)
    print(id(Pessoa.olhos), id(adobe.olhos), id(corel.olhos))