matriz = []
numeroLinhas = 3
numeroColunas = 3

for linha in range(numeroLinhas):
    inserir = [] 
    for coluna in range(numeroColunas):
        valor = int(input(f"Digite o valor para a posição [{linha}, {coluna}]: "))
        inserir.append(valor)  
    matriz.append(inserir) 

print("Matriz criada:")
for imprimir in matriz:
    print(imprimir)

    