import math

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função para calcular a média
def calcular_media(lista):
    return sum(lista) / len(lista)

# Função para calcular a variância
def calcular_variancia(lista):
    media = calcular_media(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

# Função para calcular o desvio padrão
def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    return math.sqrt(variancia)

# Exemplo de uso
media = calcular_media(numeros)
variancia = calcular_variancia(numeros)
desvio_padrao = calcular_desvio_padrao(numeros)

print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
