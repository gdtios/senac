#foi feita uma pesquisa no senacrs. foram coletados idade e sexo(m/f) dos alunos e nota. fa
#faça um programa que calcule e mostre:
#a media das notas dos alunos
#a maior e a menor idade dos alunos
#a quantidade de alunas do senacrs
#a idade e o sexo do aluno que possui a menor nota
alunos = []
alunas = 0
notas= 0
menor_nota = 0
maior_nota = 999
menor_idade= 999
maior_idade = 0
sexo_menor_nota = ""
idade_menor_nota = 0

def media_notas(totalnotas, alunos):
    return totalnotas / alunos
while True:
    sexo = input("Digite o sexo do aluno (m/f) ou fim para finalizar: ")
    if sexo == "fim":
        break
    nota = float(input("digite sua nota escolar"))
    idade = int(input("digite sua idade: "))

    alunos.append({'idade': idade, 'sexo': sexo, 'nota': nota})
    notas += nota
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if sexo == 'f':
        alunas += 1
    if nota < menor_nota:
        menor_nota = nota
        sexo_menor_nota = sexo
        idade_menor_nota = idade
if len(alunos) > 0:
    media = media_notas(notas, len(alunos))
else:
    media = 0

print(f"A média das notas dos alunos é:", media)
print(f"A maior idade dos alunos é: {maior_idade}")
print(f"A menor idade dos alunos é: {menor_idade}")
print(f"A quantidade de alunas no SENACRS é: {alunas}")
print(f"O aluno com a menor nota tem {idade_menor_nota} anos e é do sexo {'feminino' if sexo_menor_nota == 'f' else 'masculino'}")