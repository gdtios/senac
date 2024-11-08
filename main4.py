class Arvore:
    def __init__(self):
        self.folha = False
        self.altura = 0

    def brotar(self):
        if self.altura >= 1:
            self.folha = True

    def crescer(self, altura=0.5):
        self.altura += altura
        print(f"A árvore cresceu {altura} metros.")

    def ver_altura(self):
        print(f"Altura: {self.altura:.1f} m")

    def tem_folhas(self):
        if self.folha:
            print("Sim, a árvore tem folhas.")
        else:
            print("Não, a árvore ainda não tem folhas.")

# Teste
a = Arvore()

a.brotar()
print(a.folha)  
a.crescer()     
a.brotar()      
a.tem_folhas()  
a.ver_altura()  


a.crescer(0.6)  
a.brotar()     
a.tem_folhas()  
a.ver_altura() 
