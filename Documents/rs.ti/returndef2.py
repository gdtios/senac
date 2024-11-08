alunos = []
alunas = 0
notas = 0
menor_nota = 999
maior_idade = 0
menor_idade = 999
sexo_menor_nota = ""
idade_menor_nota = 0

def media_notas(totalnotas, alunos):
    return totalnotas / alunos if alunos > 0 else 0

def encontrar_maior_idade(alunos):
    maior = 0
    for aluno in alunos:
        if aluno['idade'] > maior:
            maior = aluno['idade']
    return maior

def encontrar_menor_idade(alunos):
    menor = 999
    for aluno in alunos:
        if aluno['idade'] < menor:
            menor = aluno['idade']
    return menor
def contar_alunas(alunos):
    count = 0
    for aluno in alunos:
        if aluno['sexo'] == 'f':
            count += 1
    return count
def encontrar_menor_nota(alunos):
    menor_nota = 999
    sexo = ""
    idade = 0
    for aluno in alunos:
        if aluno['nota'] < menor_nota:
            menor_nota = aluno['nota']
            sexo = aluno['sexo']
            idade = aluno['idade']
    return menor_nota, sexo, idade

while True:
    sexo = input("Digite o sexo do aluno (m/f) ou 'fim' para finalizar: ").lower()
    if sexo == "fim":
        break
    if sexo not in ['m', 'f']:
        print("Sexo inválido, digite 'm' ou 'f'.")
        continue
    nota = float(input("Digite sua nota escolar: "))
    idade = int(input("Digite sua idade: "))

    alunos.append({'idade': idade, 'sexo': sexo, 'nota': nota})
    notas += nota

media = media_notas(notas, len(alunos))
maior_idade = encontrar_maior_idade(alunos)
menor_idade = encontrar_menor_idade(alunos)
alunas = contar_alunas(alunos)
menor_nota, sexo_menor_nota, idade_menor_nota = encontrar_menor_nota(alunos)

print(f"\nA média das notas dos alunos é: {media:.2f}")
print(f"A maior idade dos alunos é: {maior_idade}")
print(f"A menor idade dos alunos é: {menor_idade}")
print(f"A quantidade de alunas no SENACRS é: {alunas}")
print(f"O aluno com a menor nota tem {idade_menor_nota} anos e é do sexo {'feminino' if sexo_menor_nota == 'f' else 'masculino'}")
