#crie uma lista com 10 numeros aleatorios. remova todos os pares

import random
numeros = [random.randint(1, 10) for _ in range(10)]
print(numeros)
numeros = [num for num in numeros if num % 2 != 0]
print(numeros)