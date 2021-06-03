from random import randint


def dado6(dano):
    dano = randint(1,6)
    if dano == 1:
        print('O oponente te atinge mas você foi rapido te acertando apenas de raspam')
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