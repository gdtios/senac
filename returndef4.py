#faça um programa para atendimento na UPA de Santa Maria, 
# onde o usuario passa pela triagem com a equipe de enfermagem e é solicitado 
#cpf, nome, data nascimento.
#onde é verificado o peso, altura, spo2 (saturacao), fc (frequencia cardiaca), 
#perguntado tambem se o usuario tem HAS (hipertensao arterial sistemica), 
# DM (diabetes melittus), apos o enfermeiro colocar seu nome o numero COREN
#fazer o cadastro do enfermeiro
#fazer o cadastro do paciente
#cadastrar os dados da consulta realizada pelo enfermeiro com o paciente
#imprimir os dados do paciente, do enfermeiro e da consulta
#fazer o imc de cada paciente e mostrar o valor e dua classificacao
#fazer a media de peso, mostrando tambem os dados do paciente com maior peso e de menor peso.
#fazer a media de altura, mostrando tambem os dados do paciente maior estatura e menor estatura
#faça um menu para ter acesso as opcoes do programa
#mostrar o total de consultas e a porcentagem dos pacientes que tem HAS ou DM
#para poder sair do sistema é obrigatório digitar SAIR
#o relatório deve ser impresso em um arquivo relatório_rsti.txt
# valores do imc: pessoas de 20 a 60 anos
#valor do imc     #classificacao
#menor que 18,5   #baixo peso
#de 19,5 a 24,99  #normal
#de 25 a 29,99    #sobrepeso
#maior que 30     #obesidade

def triagem():
    cpf = input("Digite o CPF do paciente: ")
    nome = input("Digite o nome do paciente: ")
    datanasc = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")

    peso = float(input("Digite o peso do paciente (kg): "))
    altura = float(input("Digite a altura do paciente (m): "))
    spo2 = int(input("Digite a saturação de oxigênio (SpO2 %): "))
    fc = int(input("Digite a frequência cardíaca (bpm): "))
    
    has = input("O paciente tem hipertensão arterial sistêmica (HAS)? (Digite 'sim' ou 'não'): ")
    dm = input("O paciente tem diabetes mellitus (DM)? (Digite 'sim' ou 'não'): ")

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
        "HAS": has == 'sim',  
        "DM": dm == 'sim',    
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
    return imc

def imprimir_resultados(dados_pacientes):
    with open("relatório_rsti.txt", "w") as arquivo:
        arquivo.write("Dados dos pacientes:\n")
        for paciente in dados_pacientes:
            arquivo.write(f"Paciente: {paciente['Nome']}, CPF: {paciente['CPF']}, Data de Nascimento: {paciente['Data de Nascimento']}, IMC: {calcular_imc(paciente):.2f},\n")
    print("Resultados impressos em 'relatório_rsti.txt'!!!")
    
def exibir_dados_paciente(paciente):
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

    maior_peso = dados_pacientes[0]
    menor_peso = dados_pacientes[0]
    maior_altura = dados_pacientes[0]
    menor_altura = dados_pacientes[0]

    for paciente in dados_pacientes:
        if paciente['Peso'] > maior_peso['Peso']:
            maior_peso = paciente
        if paciente['Peso'] < menor_peso['Peso']:
            menor_peso = paciente
        if paciente['Altura'] > maior_altura['Altura']:
            maior_altura = paciente
        if paciente['Altura'] < menor_altura['Altura']:
            menor_altura = paciente

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
    print("4. Sair")
    return input("Escolha uma opção: ")

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
                print("Não foi encontrado nenhum paciente com esse cpf e  data de nascimento.")

 