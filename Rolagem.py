from random import randint

#reformular os danos para servir tanto ao Jogaor quanto ao NPC
def dado6esp(dano):
    dano = randint(1,6)
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
        print('Golce preciso o sangramento surge forte, causando o equilibrio e desfoque ')


def dado6arq(dano):
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

