dic = {}
def func(a, b):
    for _ in range(50):
        print("funcionando")
    # try:
    #     print(dic['nome'])
    # except KeyError:
    try:
        return a/"B"
    except Exception as excecao:
        print(f"Ocorreu um erro: {excecao}")
    except ZeroDivisionError:
        print(f"ZeroDivisionError")

func(1, 2)