from time import sleep


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



def tiktak(tempo):
    c = 0
    while True:
        print('.',end= ' ')
        sleep(0.3)
        c += 1
        if tempo == c:
            break





