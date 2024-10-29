#funcao soma, funcao triplo somar
def somar_dois_numeros(a, b):
    resultado = a + b
    return resultado
def novo(soma):
    triplo = soma * 3
    return triplo
    
a = float(input("digite o primeiro numero"))
b = float(input("digite o segundo numero"))

soma = somar_dois_numeros(a, b)
somax = novo(soma)
print(f"a soma dos dois numeros é", soma)
print(f"a soma mais o triplo dos dois numeros é", somax)

          
