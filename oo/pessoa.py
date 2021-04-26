class Pessoa:
    def __init__(self, nomme = None, idade = 35):
        self.idade = idade
        self.nome = nomme
    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    p = Pessoa('AGT')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Marcel'
    p.idade = 39
    print(p.nome)
    print(p.idade)