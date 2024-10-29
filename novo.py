# crie uma lista com as notas de 5 alunos. calcule e imprima a media das notas

lista = [0] * 5  

for i in range(5):
    lista[i] = int(input(f"digite a nota dos 5 alunos: {i+1}°: "))
    media = sum(lista) / 5
print("As notas dos alunos são:", lista)
print("A média das notas é:", media)