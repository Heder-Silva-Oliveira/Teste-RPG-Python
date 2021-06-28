from random import randint


def dado6arq(dano):
    dano = randint(1,6)
    if dano == 1:
        print('O tiro passa atingindo a pele de raspam')
    if dano ==2:
        print('A flexa acerta o alvo mas não aprofunda na carne')
    if dano == 3:
        print('A flexa atinge o alvo causando sangramento mas não crava na carne')
    if dano == 4:
        print('O impacto foi forte causanso o desequilibrio e o sangue verte manchando o corpo')
    if dano == 5:
        print('A dor da lamina da flexa e o impacto dela no corpo tira totalmente o equilibrio')
    if dano == 6:
        print('A flexa crava facil na carne impactando e sangrando, o corpo cai ao chão ')


def dado6mag(dano):
    dano = randint(1,6)
    if dano == 1:
        print()
    if dano ==2:
        print()
    if dano == 3:
        print()
    if dano == 4:
        print()
    if dano == 5:
        print()
    if dano == 6:
        print()


def dado4(itens):
    itens = randint(1, 4)
    if itens == 1:
        print('Você encontra uma bolsa com 20 moedas de ouro')
    if itens == 2:
        print('Você encontra um anel com uma estranha figura gravada')
    if itens == 3:
        print('Você encontra um pequeno livro com uma gravura e pentagrama na capa')
    if itens == 4:
        print('Você encontra uma adaga com a lamina negra e punho prateado ')

