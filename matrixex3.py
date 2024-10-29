matriz = []
numeroLinhas = 5
numeroColunas = 5
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
for i in range(numeroLinhas):
    for j in range(numeroColunas):
        if i < j:  
            soma += matriz[i][j]

print("A soma dos elementos acima da diagonal principal é: ", soma)