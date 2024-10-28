numeros = []
print("Aperte 1 para adicionar um número")
print("Aperte 2 para mostrar números que aparecem mais de uma vez")
print("Aperte 3 para sair")

while True:
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        numero = int(input("Digite o número: "))
        numeros.append(numero)
        print(f"Número {numero} adicionado com sucesso!")
        
    elif opcao == 2:
        print("Mostrando números que aparecem mais de uma vez:")
        numeros_unicos = list(set(numeros))
        numeros_repetidos = [numero for numero in numeros_unicos if numeros.count(numero) > 1]
        if numeros_repetidos:
            print(numeros_repetidos)
        else:
            print("Nenhum número se repete.")
    
    elif opcao == 3:
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
