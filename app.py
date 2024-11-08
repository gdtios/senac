import PySimpleGUI as sg

nome = input("qual seu nome:")
idade = int(input("qual seu idade:"))
nota = float(input("1ºsemestre:"))
nota2 = float(input("2ºsemestre:"))
nota3 = float(input("3ºsemestre:"))


if nota >= 10:
    print('numero incorreto')
else:
    nota2 = float(input("2ºsemestre:"))
    nota3 = float(input("3ºsemestre:"))
     
     
calculo=(nota+nota2+nota3)/3

print(f'{nome} sua media e {calculo}')




