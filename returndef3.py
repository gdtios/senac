#faça um algoritmo para cadastrar veículos para uma seguradora. o veiculo deve ter cadastrado a placa, marca, modelo, valor, ano
#fazer uma funcao principal
#funcao com a media dos valores dos veiculos
#funcao com o veiculo mais caro
#funcao para buscar os dados do veiculo mais barato
#funcao para buscar todos os veiculos da mesma marca e modelo 
#funcao para imprimir os resultados em um arquivo txt
#funcao para o valor do seguro de 15% para veiculos com valor acima de 100.000 e 10% para o restante. 
#mostrar o valor do seguro de todos os carros
def buscar_veiculo_marca_modelo(veiculos, marca, modelo):
    veiculos_encontrados = []
    for veiculo in veiculos:
        if veiculo[2] == marca and veiculo[3] == modelo:
            veiculos_encontrados.append(veiculo)
    return veiculos_encontrados
def media_veiculos(totalvalor, veiculos):
    return totalvalor / veiculos if veiculos > 0 else 0

def encontrar_maior_valor_veiculo(veiculos):
    maior = 0
    for veiculo in veiculos:
        if veiculo[4] > maior:
            maior = veiculo[4]
            veiculomaior = veiculo
    return veiculomaior
def encontrar_menor_valor_veiculo(veiculos):
    menor= veiculos[0][4]
    veiculo_menor_valor = veiculos[0]
    for veiculo in veiculos:
        if veiculo[4] < menor:
            menor = veiculo[4]
            veiculo_menor_valor = veiculo
    return veiculo_menor_valor
def imprimir_resultados(veiculos, media, maiorvalor, menorvalor):
    with open("resultados_veiculos.txt", "w") as arquivo:
        arquivo.write("Dados dos Veículos:")
        for veiculo in veiculos:
            arquivo.write(f"Veículo: {veiculo[0]}, Placa: {veiculo[1]}, Marca: {veiculo[2]}, Modelo: {veiculo[3]}, Valor: {veiculo[4]:.2f}, Ano: {veiculo[5]}\n")
        arquivo.write(f"\nA média dos valores dos veículos é: {media:.2f}\n")
        arquivo.write(f"O veículo mais caro é: {maiorvalor[0]} com valor de {maiorvalor[4]:.2f}\n")
        arquivo.write(f"O veículo mais barato é: {menorvalor[0]} com valor de {menorvalor[4]:.2f}\n")
    
print("Relatório salvo!!!")
        
def principal():    
    dados_veiculos = []
    total_valor = 0
    while True:
        veiculo = input("Digite seu veiculo (ou 'sair' para sair): ")
        if veiculo == 'sair':
            break        
        placa = input("Digite a placa do veiculo: ")
        marca = input("Digite a marca do veiculo: ")
        modelo = input("Digite o modelo do veiculo: ")
        valor = float(input("Digite o valor do veiculo: "))
        ano = int(input("Digite o ano do veiculo: "))
        dados_veiculos.append([veiculo, placa, marca, modelo, valor, ano])
        total_valor += valor
    return dados_veiculos, total_valor

veiculos, total_valor = principal()
media = media_veiculos(total_valor, len(veiculos))
maiorvalor = encontrar_maior_valor_veiculo(veiculos)
menorvalor = encontrar_menor_valor_veiculo(veiculos)

marca_busca = input("Digite a marca para busca: ")
modelo_busca = input("Digite o modelo para busca: ")
veiculos_encontrados = buscar_veiculo_marca_modelo(veiculos, marca_busca, modelo_busca)

if veiculos_encontrados:
    print("Veículos encontrados:")
    for veiculo in veiculos_encontrados:
        print(f"Veículo: {veiculo[0]}, Placa: {veiculo[1]}, Marca: {veiculo[2]}, Modelo: {veiculo[3]}, Valor: {veiculo[4]:.2f}, Ano: {veiculo[5]}")
else:
    print("Nenhum veículo encontrado com essa marca e modelo.")

for veiculo in veiculos:
    print(f"Veículo: {veiculo[0]}, Placa: {veiculo[1]}, Marca: {veiculo[2]}, Modelo: {veiculo[3]}, Valor: {veiculo[4]:.2f}, Ano: {veiculo[5]}")
print("A média dos valores dos veículos é:", media)
print(f"O veículo mais caro é: {menorvalor[0]} com valor de {maiorvalor[4]:.2f}")
print(f"O veículo mais barato é: {menorvalor[0]} com valor de {menorvalor[4]:.2f}")
imprimir_resultados(veiculos, media, maiorvalor, menorvalor)
print("Resultados impressos em 'resultados_veiculos.txt'.")
