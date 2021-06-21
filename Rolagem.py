from random import randint

#reformular os danos para servir tanto ao Jogaor quanto ao NPC
def dado6esp(dano):
    dano = randint(1,6)
    if dano == 1:
        print('O oponente te atinge mas você foi rapido, ele te acertando apenas de raspam')
    if dano == 2:
        print('Embora você seja rapido, o oponente conseque te asertar mas isso não muda sua situação')
    if dano == 3:
        print('Você é atingio causando grande dor, te deixando exposto no local acertado')
    if dano == 4:
        print('A dor é grande causado pelo ataque deixa você sem foco')
    if dano == 5:
        print('Você perde o equilibrio cai de joelho com a mão no local atingiddo')
    if dano == 6:
        print('Você é acertado em cheio e cai sangrando e terá ganha uma grande cicatriz se sobreviver')


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

