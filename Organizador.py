def linha(tam = 40):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeçalho('')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1

