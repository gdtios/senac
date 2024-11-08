class Caneta:
    def __init__(self, cor, carga):
        self.cor = cor
        self.tampado = True
        self.quebrado = True
        self.carga = carga
    def destampar(self):
        if self.tampado:
            self.tampado = False
            print("Destampando... a caneta  foi destampada")
        else:
            print("A caneta já está destampada")
        
    def testar(self):
        if not self.quebrado:
            print("a caneta está quebrada")
        else:  print("Testando... A caneta está funcionando")
    def escrever(self):
        if  self.carga:
            self.carga -= 50
            print(f"Escrevendo... Carga restante: {self.carga}")
        else:
            print("A caneta está sem carga.")    
    def recarregar(self):
        if  self.carga <= 0:
            self.carga += 100
        print(f"carga recarregada: {self.carga}")
    def tampar(self):
        if  not self.tampado:
            self.tampado = True
            print("A caneta foi tampada")
        else:
            print("a caneta ja esta tampada")
    def guardar(self):
        if not self.tampado:
            print("A caneta  nao está tampada, não pode ser guardada")
        else:
            print("A caneta foi guardada")
            

         
caneta_azul = Caneta("azul", 100)
print(caneta_azul.cor)
print(caneta_azul.tampado)
caneta_azul.destampar()
caneta_azul.testar()
caneta_azul.escrever()
caneta_azul.escrever()
caneta_azul.escrever()
caneta_azul.recarregar()
caneta_azul.guardar()
caneta_azul.tampar()
caneta_azul.guardar()
print(caneta_azul.tampado)
