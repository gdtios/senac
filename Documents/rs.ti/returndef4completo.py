def triagem():
    cpf = input("Digite o CPF do paciente: ")
    nome = input("Digite o nome do paciente: ")
    datanasc = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")

    peso = float(input("Digite o peso do paciente (kg): "))
    altura = float(input("Digite a altura do paciente (m): "))
    spo2 = int(input("Digite a saturação de oxigênio (SpO2 %): "))
    fc = int(input("Digite a frequência cardíaca (bpm): "))

    has = input("O paciente tem hipertensão arterial sistêmica (HAS)? (S/N): ")
    dm = input("O paciente tem diabetes mellitus (DM)? (S/N): ")

    enfermeiro_nome = input("Digite o nome do enfermeiro: ")
    enfermeiro_coren = input("Digite o número do COREN do enfermeiro: ")

    paciente = {
        "CPF": cpf,
        "Nome": nome,
        "Data de Nascimento": datanasc,
        "Peso": peso,
        "Altura": altura,
        "SpO2": spo2,
        "FC": fc,
        "HAS": has.upper() == 'S',
        "DM": dm.upper() == 'S',
        "Enfermeiro": enfermeiro_nome,
        "COREN": enfermeiro_coren
    }

    return paciente

def buscar_paciente_cpf_nome(dados_pacientes, cpf, datanasc):
    pacientes_encontrados = []
    for paciente in dados_pacientes:
        if paciente["CPF"] == cpf and paciente["Data de Nascimento"] == datanasc:
            pacientes_encontrados.append(paciente)
    return pacientes_encontrados

def calcular_imc(paciente):
    imc = paciente['Peso'] / (paciente['Altura'] ** 2)
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif 18.5 <= imc <= 24.99:
        classificacao = "Normal"
    elif 25 <= imc <= 29.99:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    return imc, classificacao

def imprimir_resultados(dados_pacientes):
    with open("relatório_rsti.txt", "w") as arquivo:
        arquivo.write("Dados dos pacientes:\n")
        for paciente in dados_pacientes:
            imc, classificacao = calcular_imc(paciente)
            arquivo.write(f"Paciente: {paciente['Nome']}, CPF: {paciente['CPF']}, Data de Nascimento: {paciente['Data de Nascimento']}, IMC: {imc:.2f}, Classificação: {classificacao}, Enfermeiro: {paciente['Enfermeiro']}, COREN: {paciente['COREN']}\n")
    print("Resultados impressos em 'relatório_rsti.txt'!!!")

def exibir_dados_paciente(paciente):
    imc, classificacao = calcular_imc(paciente)
    print("\nDados do Paciente:")
    print(f"CPF: {paciente['CPF']}")
    print(f"Nome: {paciente['Nome']}")
    print(f"Data de Nascimento: {paciente['Data de Nascimento']}")
    print(f"Peso: {paciente['Peso']} kg")
    print(f"Altura: {paciente['Altura']} m")
    print(f"Saturação de oxigênio (SpO2): {paciente['SpO2']}%")
    print(f"Frequência Cardíaca (FC): {paciente['FC']} bpm")
    print(f"Hipertensão Arterial Sistêmica (HAS): {'Sim' if paciente['HAS'] else 'Não'}")
    print(f"Diabetes Mellitus (DM): {'Sim' if paciente['DM'] else 'Não'}")
    print(f"Enfermeiro Responsável: {paciente['Enfermeiro']}")
    print(f"COREN: {paciente['COREN']}")
    print(f"IMC: {imc:.2f} - Classificação: {classificacao}")

def relatorio_geral(dados_pacientes):
    if not dados_pacientes:
        print("Nenhum paciente cadastrado.")
        return

    total_consultas = len(dados_pacientes)
    pacientes_com_has = sum(1 for p in dados_pacientes if p['HAS'])
    pacientes_com_dm = sum(1 for p in dados_pacientes if p['DM'])

    print(f"\nTotal de consultas: {total_consultas}")
    print(f"Porcentagem de pacientes com HAS: {100 * pacientes_com_has / total_consultas:.2f}%")
    print(f"Porcentagem de pacientes com DM: {100 * pacientes_com_dm / total_consultas:.2f}%")

    media_peso = sum(p['Peso'] for p in dados_pacientes) / total_consultas
    media_altura = sum(p['Altura'] for p in dados_pacientes) / total_consultas

    maior_peso = max(dados_pacientes, key=lambda x: x['Peso'])
    menor_peso = min(dados_pacientes, key=lambda x: x['Peso'])
    maior_altura = max(dados_pacientes, key=lambda x: x['Altura'])
    menor_altura = min(dados_pacientes, key=lambda x: x['Altura'])

    print(f"Média de peso: {media_peso:.2f} kg")
    print(f"Paciente com maior peso: {maior_peso['Nome']} - {maior_peso['Peso']} kg")
    print(f"Paciente com menor peso: {menor_peso['Nome']} - {menor_peso['Peso']} kg")

    print(f"Média de altura: {media_altura:.2f} m")
    print(f"Paciente com maior altura: {maior_altura['Nome']} - {maior_altura['Altura']} m")
    print(f"Paciente com menor altura: {menor_altura['Nome']} - {menor_altura['Altura']} m")

def menu():
    print("\nMenu:")
    print("1. Realizar triagem de um paciente")
    print("2. Buscar paciente")
    print("3. Relatório geral")
    print("4. Sair (Digite SAIR para encerrar)")
    return input("Escolha uma opção: ").strip().upper()

def principal():
    dados_pacientes = []
    while True:
        opcao = menu()
        if opcao == '1':
            print("\nIniciar triagem do paciente:")
            paciente = triagem()
            dados_pacientes.append(paciente)
        elif opcao == '2':
            cpf_busca = input("\nDigite o CPF para busca: ")
            datanasc_busca = input("Digite a data de nascimento (DD/MM/AAAA) para busca: ")
            pacientes_encontrados = buscar_paciente_cpf_nome(dados_pacientes, cpf_busca, datanasc_busca)

            if pacientes_encontrados:
                print("\nPacientes encontrados:")
                for paciente in pacientes_encontrados:
                    exibir_dados_paciente(paciente)
            else:
                print("Nenhum paciente encontrado com esse CPF e data de nascimento.")
        elif opcao == '3':
            relatorio_geral(dados_pacientes)
        elif opcao == 'SAIR':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    imprimir_resultados(dados_pacientes)

principal()
