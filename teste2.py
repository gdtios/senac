cores= ['vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta']
print(cores)
cor = input("digite uma cor para remover do arco iris: ")
if cor in cores:
    print("a cor foi removida.")
else:
    print("A cor não existe no arco íris.")