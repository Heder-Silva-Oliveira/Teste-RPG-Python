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


    def batalhadefesp(inimigoataq):
        inimigoataq = randint(1, 20)
        print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
        if inimigoataq >= 12:
            print('Você foi atingido')
            dano = randint(1, 6)
            if dano == 1:
                print('A espada passa em um arco descendente, porém apenas de raspam')
            if dano == 2:
                print('A espada acerta seu alvo, um pequeno corte surge vermelho')
            if dano == 3:
                print('O golpe foi certeiro, causando grande dor e deixando exposto no local acertado')
            if dano == 4:
                print('A dor do ferimento é muito forte, deixando os olhos sem foco ')
            if dano == 5:
                print('A dor é insuportável os joelho se dobram e a mão vai até no local atingido')
            if dano == 6:
                print('O gole preciso o sangramento surge forte, causando o a queda ao chão e desfoque ')
        else:
            print("Você não foi atingido")


    def batalhaatqesp(meuataq):
            print(f'O meu ataque foi de {meuataq}, a CA do oponente é de {15}')
            if meuataq >= 15:
                print('Acertei o alvo')
                dano = randint(1, 6)
                if dano == 1:
                    print('A espada passa em um arco descendente, porém apenas de raspam')
                if dano == 2:
                    print('A espada acerta seu alvo, um pequeno corte surge vermelho')
                if dano == 3:
                    print('O golpe foi certeiro, causando grande dor e deixando exposto no local acertado')
                if dano == 4:
                    print('A dor do ferimento é muito forte, deixando os olhos sem foco ')
                if dano == 5:
                    print('A dor é insuportável os joelho se dobram e a mão vai até no local atingido')
                if dano == 6:
                    print('O golpe preciso o sangramento surge forte, causando o a queda ao chão e desfoque ')
            else:
                print('Não atingi o alvo')


class Lutafle:

    def batalhadeffle(inimigoataq):
        inimigoataq = randint(1, 20)
        print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
        if inimigoataq >= 12:
            print('Você foi atingido')
            dano = randint(1, 6)
            if dano == 1:
                print('O tiro passa atingindo a pele de raspam')
            if dano == 2:
                print('A flecha acerta o alvo mas não aprofunda na carne')
            if dano == 3:
                print('A flecha atinge o alvo causando sangramento mas não crava na carne')
            if dano == 4:
                print('O impacto foi forte causando o desequilíbrio e o sangue verte manchando o corpo')
            if dano == 5:
                print('A dor da lamina da flecha e o impacto dela no corpo tira totalmente o equilíbrio')
            if dano == 6:
                print('A flecha crava fácil na carne impactando e sangrando, o corpo cai ao chão ')
        else:
            print('Você não foi atingido')


def batalhaatqfle(meuataq):
        print(f'O meu ataque foi de {meuataq}, a CA do oponente é de {15}')
        if meuataq >= 15:
            print('Acertei o alvo')
            dano = randint(1, 6)
            if dano == 1:
                print('O tiro passa atingindo a pele de raspam')
            if dano == 2:
                print('A flecha acerta o alvo mas não aprofunda na carne')
            if dano == 3:
                print('A flecha atinge o alvo causando sangramento mas não crava na carne')
            if dano == 4:
                print('O impacto foi forte causando o desequilíbrio e o sangue verte manchando o corpo')
            if dano == 5:
                print('A dor da lamina da flecha e o impacto dela no corpo tira totalmente o equilíbrio')
            if dano == 6:
                print('A flecha crava fácil na carne impactando e sangrando, o corpo cai ao chão ')
        else:
            print('Não atingi o alvo')


class Lutamag:

    def batalhadefmag(inimigoataq):
        inimigoataq = randint(1, 20)
        print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
        if inimigoataq >= 12:
            print('Você foi atingio')
            dano = randint(1, 6)
            if dano == 1:
                print('O oponente te empurra para trás com um golpe cinético')
                if dano == 2:
                    print('Uma nuvem azul gelada te envolve deixando-o desorientado')
                if dano == 3:
                    print('Uma seta espectral te atinge causando muita dor')
                if dano == 4:
                    print('Uma rajada de gelo te imobiliza por alguns segundos, as lascas de gelo causa sangramento')
                if dano == 5:
                    print('Do chão surte laminas de pedra muito afiadas sangrando suas pernas e te prendendo')
                if dano == 6:
                    print('Um redemoinho de fogo te envolve irando sua orientação e te queimando por completo')
            else:
                print('Você não foi atingido')


def batalhaatqmag(meuataq):
        print(f'O meu ataque foi de {meuataq}, a CA do oponente é de {15}')
        if meuataq >= 15:
            print('Acertei o alvo')
            dano = randint(1, 6)
            if dano == 1:
                print('Você estende a mão ao oponente e um pulso de ar quente empurra o inimigo para trás')
            if dano == 2:
                print('Um fogo verte surge em direção ao inimigo com um sinal de suas mãos e causa dor ao oponente')
            if dano == 3:
                print('Uma sombra é conjurada de suas mão e envolve o inimigo, deixando sem visão momentânea')
            if dano == 4:
                print('A você conjura um expecto que atravessa o inimigo, deixando desorientado, e com muita dor')
            if dano == 5:
                print('Uma seta de gelo sai de seus dedos e crava na carne do inimigo causando muita dor a ele')
            if dano == 6:
                print('Uma bola de fogo surge de sua mão você lança contra o algo, queimando por todo corpo')
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



