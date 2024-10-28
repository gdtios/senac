#desenvolver um sistema simples para uma clinica medica utilizando python que permita:
#cadastrar medicos e suas especialidades 
#cadastrar pacientes
#agendar consulta, associando medico, paciente e data
#consultar informacoes sobre medicos pacientes e consultas
#--extrutura de dados:
#medico:
#-nome
#-CRM
#-especialidade
#paciente:
#-nome
#-datanascimento
#consultas:
#-medico
#-paciente
#-data
#-descricao
#funcionalidades:
#1. Cadastro
#cadastrar novo medico
#cadastro de paciente
#agendar uma consulta
#2. Consulta:
#listar todos os medicos
#listar todos os pacientes
#listar todas as consultas
#buscar uma consulta por data
#buscar uma consulta por medico especifico
#buscar uma consulta por paciente especifico
medicos = []
pacientes = []
consultas = []
def cadastrar_medico():
    nome = input("Digite o nome do médico: ")
    crm = input("Digite o CRM do médico: ")
    especialidade = input("Digite a especialidade do médico: ")
    medico = {"Nome": nome, "CRM": crm, "Especialidade": especialidade}
    medicos.append(medico)
    print(f"Médico {nome} cadastrado com sucesso!")
def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    datanasc = input("Digite a data de nascimento do paciente (dia/mes/ano")
    paciente = {"Nome": nome, "datanasc": datanasc}
    pacientes.append(paciente)
    print(f"paciente {nome} cadastrado com sucesso!")  
def agendar_consulta():
    print("\nAgendar consulta:")
    crm = input("Digite o CRM do médico: ")
    medico = buscar_medico_crm(crm)
    if not medico:
        print("Médico não encontrado.")
        return
    nome_paciente = input("Digite o nome do paciente: ")
    paciente = buscar_paciente_nome(nome_paciente)
    if not paciente:
        print("Paciente não encontrado.")
        return
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    descricao = input("Digite a descrição da consulta: ")
    consulta = {"Médico": medico, "Paciente": paciente, "Data": data, "Descrição": descricao}
    consultas.append(consulta)
    print(f"Consulta agendada com sucesso para {paciente['Nome']} com o Dr(a). {medico['Nome']}.")
def buscar_medico_crm(crm):
    for medico in medicos:
        if medico["CRM"] == crm:
            return medico
    return None
def buscar_paciente_nome(nome):
    for paciente in pacientes:
        if paciente["Nome"] == nome:
            return paciente
    return None
def listar_medicos():
    if not medicos:
        print("Nenhum médico cadastrado.")
        return
    print("\nMédicos cadastrados:")
    for medico in medicos:
        print(f"Nome: {medico['Nome']}, CRM: {medico['CRM']}, Especialidade: {medico['Especialidade']}")    
def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    print("\npacientes cadastrados:")
    for paciente in pacientes:
         print(f"Nome: {paciente['Nome']}, Data de Nascimento: {paciente['Data de Nascimento']}")     
def listar_consultas():
    if not consultas:
        print("Nenhuma consulta agendada.")
        return
    print("\nConsultas agendadas:")
    for consulta in consultas:
        print(f"Paciente: {consulta['Paciente']['Nome']}, Médico: {consulta['Médico']['Nome']}, Data: {consulta['Data']}, Descrição: {consulta['Descrição']}")
def buscar_consulta_por_data():
    data_busca = input("Digite a data da consulta (DD/MM/AAAA): ")
    consultas_encontradas = [consulta for consulta in consultas if consulta["Data"] == data_busca]
    
    if consultas_encontradas:
        print(f"\nConsultas encontradas para {data_busca}:")
        for consultas in consultas_encontradas:
            print(f"Paciente: {consultas['Paciente']['Nome']}, Médico: {consultas['Médico']['Nome']}, Descrição: {consultas['Descrição']}")
    else:
        print("Nenhuma consulta encontrada para esta data.")      
def buscar_consulta_por_medico():
    crm = input("Digite o CRM do médico: ")
    medico = buscar_medico_crm(crm)
    
    if not medicos:
        print("Médico não encontrado.")
        return   
    consultas_encontradas = [consulta for consulta in consultas if consulta["Médico"] == medico]
    if consultas_encontradas:
        print(f"\nConsultas encontradas para o Dr(a). {medico['Nome']}:")
        for consulta in consultas_encontradas:
            print(f"Paciente: {consulta['Paciente']['Nome']}, Data: {consulta['Data']}, Descrição: {consulta['Descrição']}")
    else:
        print(f"Nenhuma consulta encontrada para o Dr(a). {medico['Nome']}.")       
def buscar_consulta_por_paciente():
    nome_paciente = input("Digite o nome do paciente: ")
    paciente = buscar_paciente_nome(nome_paciente)   
    if not paciente:
        print("paciente não encontrado.")
        return 
    consultas_encontradas = [consulta for consulta in consultas if consulta["paciente"] == paciente]
    if consultas_encontradas:
        print(f"\nConsultas encontradas para paciente {paciente['Nome']}:")
        for consultas in consultas_encontradas:
            print(f"Paciente: {consultas['medico']['Nome']}, Data: {consultas['Data']}, Descrição: {consultas['Descrição']}")
    else:
        print(f"Nenhuma consulta encontrada para o Dr(a). {paciente['Nome']}.")
def menu():
    print("\nMenu:")
    print("1. Cadastrar médico")
    print("2. Cadastrar paciente")
    print("3. Agendar consulta")
    print("4. Listar médicos")
    print("5. Listar pacientes")
    print("6. Listar consultas")
    print("7. Buscar consulta por data")
    print("8. Buscar consulta por médico")
    print("9. Buscar consulta por paciente")
    print("0. Sair")
    return input("Escolha uma opção: ")
def principal():
    while True:
        opcao = menu()
        if opcao == '1':
            cadastrar_medico()
        elif opcao == '2':
            cadastrar_paciente()
        elif opcao == '3':
            agendar_consulta()
        elif opcao == '4':
            listar_medicos()
        elif opcao == '5':
            listar_pacientes()
        elif opcao == '6':
            listar_consultas()
        elif opcao == '7':
            buscar_consulta_por_data()
        elif opcao == '8':
            buscar_consulta_por_medico()
        elif opcao == '9':
            buscar_consulta_por_paciente()
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
principal()