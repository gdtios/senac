lista_vazia = []
print(lista_vazia)

lista_inteiros = [2, 4, 6 ,8, 10]
print(lista_inteiros)

lista_reais = [9.0, 10.0, 8.5, 7.8]
print(lista_reais)

lista_frutas = ["abacaxi", "maça", "banana"]
print(lista_frutas)

lista_zerada = [0] * 5
print(lista_zerada) 

lista_strings = [""] * 4
print(lista_strings)  

#lista = [2, 4, 6, 8, 10]
#print(lista)
#lista = lista + [5.0]
#print(lista)

#lista = [2, 4, 6, 8, 10]
#print(lista)
#lista.append(99.0)
#print(lista)

lista = [2, 4, 6, 8, 10]
print(lista)
lista.extend([99.0, 10.1, 50])
print(lista)

# crie uma lista com os 20 primeiros numeros pares
#pares = []
#for i in range(2, 41, 2):
#    pares.append(i)
#    print(pares)


#crie uma lista com 10 numeros aleatorios entre 1 e 100. enconte o maior e o menor valor dessa lista
#import random
#numeros = [random.randint(1, 100) for _ in range(10)]
#maior = max(numeros)
#menor = min(numeros)
#print("maior numero:", maior)
#print("menor numero", menor)

#crie uma lista com 5 frutas. inverta a ordem dos elementos dessa lista
frutas= ["maça", "banana",  "laranja", "morango", "uva"]
frutas.reverse()
print(frutas)

#crie uma lista com numeros repetidos. remova os elementos duplicados e imprima a listra sem repeticoes
numeros = [1, 2, 3, 1, 5]
numeros_unicos = list(set(numeros))
print(numeros_unicos)

#crie uma lista de letras. conte quantas vezes a letra 'a' aparece nessa lista
letras=['a','b','c','a','d','a']
contagem_a =letras.count('a')
print("a letra 'a' aparece", contagem_a, "vezes")