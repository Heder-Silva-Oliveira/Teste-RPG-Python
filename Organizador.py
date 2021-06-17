from time import sleep
from random import randint
from Rolagem import dado6

def linha(tam = 40):
    return '-' *tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho(' ')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha(40))


def batalhadef():
    inimigoataq = randint(1, 20)
    print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
    if inimigoataq >= 20:
        print('Vocçe foi atingio')
        rels = randint(1, 6)
        dado6(rels)
    else:
        print('Você não foi atingio')


def tiktak(tempo):
    c = 0
    while True:
        print('.',end= ' ')
        sleep(0.4)
        c += 1
        if tempo == c:
            break









