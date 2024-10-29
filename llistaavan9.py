#crie uma programa que simule uma agenda telefonica. o usuario deve poder adicionar, remover e buscar contatos (nome e telefone). 
contatos =[]
print("digite 1 para adicionar contato")
print("digite 2 para  remover contato")
print("digite 3 para  buscar contato")
print("digite 4 para sair")
while True:
    opcao = int(input("digite a opcao: "))
    if opcao == 1:
        nome = input("digite o nome: ")
        telefone = input("digite o telefone: ")
        contatos.append({"nome":nome, "telefone":telefone})
        print(f"Contato {nome} adicionado com sucesso!")
    elif opcao == 2:
        nome = input("digite o nome do contato a ser removido: ")
        contatos = [contato for contato in contatos if contato["nome"] != nome]
        print(f"Contato {nome} removido com sucesso!")
    elif opcao == 3:
        nome = input("digite o nome do contato a ser buscado: ")
        for contato in contatos:
            if contato["nome"] == nome:
                print=(f"nome: {contato['nome']}, telefone: {contato['telefone']}")
            break
        else:
            print(f"Contato {nome} não encontrado.")
    elif opcao == 4:
        print("Saindo da agenda telefônica.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
