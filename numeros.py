numeros_lista = [1, 2, 3, 4, 5]
def calcular_media (lista):
    return sum(lista) / len(lista)
def calcular_variancia(lista):
    media = calcular_media(lista)
    return sum ((x -  media) **2 for x in lista) / len(lista)
def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    return  variancia ** 0.5

media = calcular_media(numeros_lista)
variancia = calcular_variancia(numeros_lista)
desvio_padrao = calcular_desvio_padrao(numeros_lista)
print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio Padrap: {desvio_padrao}")
