matriz = []
numeroLinhas = 2
numeroColunas = 2
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
        if i > j:
            soma += matriz[i][j]
print("A soma dos elementos abaixo da diagonal principal é:", soma)
with open('matriz.txt', 'w') as arquivo:
    for linha in matriz:
        linha_str = ' '.join(map(str, linha))
        arquivo.write(linha_str + '\n')
        arquivo.write("a soma dos elementos da matriz é:{soma}")
        print("matriz salva em matriz.txt")