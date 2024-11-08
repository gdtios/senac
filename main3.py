class Arvore:
    def  __init__(self):

        self.folha = False
        self.altura = 0
    def brotar(self):
        if self.altura >= 1:
            self.folha = True
    def crescer(self,  altura):
        self.altura += 0.5
    
    def ver_altura(self):
        print(f"altura {self.altura} m")
    
    def tem_folhas(self):
        if self.folha:
            print("Sim, a árvore tem folhas")
        else:
            print("nao, nao tem folhas")
    
a = Arvore()
a.brotar()
print(a.folha)
a.crescer()

a.brotar()
a.tem_folhas()
a.ver_altura()

a.brotar()
a.tem_folhas()
a.ver_altura()

a.brotar()
print(a.folha)
a.crescer()

a.brotar()
a.tem_folhas()
a.ver_altura()  