from time import sleep
from random import randint


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


def batalhadef(chama):
    inimigoataq = randint(1, 20)
    print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
    if inimigoataq >= 12:
        print('Vocçe foi atingio')
        rels = randint(1, 6)
        chama(rels)
    else:
        print('Você não foi atingio')


def batalhaatq(chama):
    meuataq = randint(1, 20)
    print(f'O meu ataque foi de {meuataq}, a CA do oponente é de {15}')
    if meuataq >= 15:
        print('Acertei o alvo')
        rels = randint(1, 6)
        chama(rels)
    else:
        print('Não atingi o alvo')


def tiktak(tempo):
    c = 0
    while True:
        print('.',end= ' ')
        sleep(0.4)
        c += 1
        if tempo == c:
            break


