altura = float(input("Digite sua altura em metros : "))
peso = float(input("Digite seu peso em kg: "))

dic_pessoa = {
    "peso": peso,
    "altura": altura
}
imc = dic_pessoa['peso'] / (dic_pessoa['altura'] ** 2)

def calcular_imc(imc):
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif 18.5 <= imc <= 24.99:
        classificacao = "Normal"
    elif 25 <= imc <= 29.99:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    return imc, classificacao
print(f"Seu IMC é: {imc:.2f}")

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))


