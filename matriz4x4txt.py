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
soma_total = 0
soma_dp = 0
maior_que_17 = []
numeros_pares = []
numeros_impares = []
for i in range(numeroLinhas):
    for j in range(numeroColunas):
        valor = matriz[i][j]
        soma_total += valor
        if valor > 17:
            maior_que_17.append(valor)
        if valor % 2 == 0:
            numeros_pares.append(valor)
        else:
            numeros_impares.append(valor)
soma_dp += matriz[i][i]  
print("A soma dos VALORES da matriz é:", soma_total)
print("A soma dos elementos da diagonal principal é:", soma_dp)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Números maiores que 17:", maior_que_17)
with open('matriz_resultados.txt', 'w') as arquivo:
    arquivo.write("Matriz:\n")
    for linha in matriz:
        linha_str = ' '.join(map(str, linha))
        arquivo.write(linha_str + '\n')
    arquivo.write(f"Soma dos valores da matriz: {soma_total}\n")
    arquivo.write(f"Soma da diagonal principal: {soma_dp}\n")
    arquivo.write(f"Números pares: {numeros_pares}\n")
    arquivo.write(f"Números ímpares: {numeros_impares}\n")
    arquivo.write(f"Números maiores que 17: {maior_que_17}\n")
print("Resultados salvos em 'matriz_resultados.txt'.")