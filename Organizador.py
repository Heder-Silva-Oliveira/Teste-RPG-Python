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

class Lutaesp:

    def batalhadef(inimigoataq):
        inimigoataq = randint(1, 20)
        print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
        if inimigoataq >= 12:
            print('Vocçe foi atingio')
            dano = randint(1, 6)
            if dano == 1:
                print('A espada passa em um arco descebdente, porém apenas de raspam')
            if dano == 2:
                print('A espada acerta seu alvo, um pequeno corte surge vermelho')
            if dano == 3:
                print('O golpe foi certeiro, causando grande dor e deixando exposto no local acertado')
            if dano == 4:
                print('A dor do ferimento é muito forte, deixando os olhos sem foco ')
            if dano == 5:
                print('A dor pe insuportavel os joelho se dobram e a mão vai até no local atingiddo')
            if dano == 6:
                print('Golce preciso o sangramento surge forte, causando o a queda ao chão e desfoque ')
        else:
            print('Você não foi atingio')


    def batalhaatq(meuataq):
        print(f'O meu ataque foi de {meuataq}, a CA do oponente é de {15}')
        if meuataq >= 15:
            print('Acertei o alvo')
            dano = randint(1, 6)
            if dano == 1:
                print('A espada passa em um arco descebdente, porém apenas de raspam')
            if dano == 2:
                print('A espada acerta seu alvo, um pequeno corte surge vermelho')
            if dano == 3:
                print('O golpe foi certeiro, causando grande dor e deixando exposto no local acertado')
            if dano == 4:
                print('A dor do ferimento é muito forte, deixando os olhos sem foco ')
            if dano == 5:
                print('A dor pe insuportavel os joelho se dobram e a mão vai até no local atingiddo')
            if dano == 6:
                print('Golce preciso o sangramento surge forte, causando o a queda ao chão e desfoque ')

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



