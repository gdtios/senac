matriz = []
numeroLinhas = 4
numeroColunas = 4
for linha in range(numeroLinhas):
    inserir = [] 
    for coluna in range(numeroColunas):
        valor = int(input(f"Digite o valor para a posição [{linha}, {coluna}]: "))
        inserir.append(valor)  
    matriz.append(inserir) 

print("Matriz criada:")
for imprimir in matriz:
    print(imprimir)
soma = 0
for i in range(min(numeroLinhas, numeroColunas)):
    soma += matriz[i][i]

print("A soma dos elementos da diagonal principal é:", soma)