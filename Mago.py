from Organizador import *
from time import sleep

from Organizador import cabecalho


def cap1mag():
    cabecalho('Tudo isso começa a te incomodar e você fica diante de duas escolhas')
    sleep(5)
    escolha = ('Você tenta abrir o olho e se livrar disso', 'Você tenta manter o foco e encontrar a reposta')
    menu(escolha)


def cap2mag():
    cabecalho('Ao seu redor varios outros magos, a maioria ja havia desistido, e apenas um ainda continua o intento')
    sleep(5)
    escolha2 = ('Você decide deixa-lo concentrado em conjurar a aurea', 'Você tenta discretamente desconcentra-lo')
    menu(escolha2)


def cap3mag(guia):
    if guia == "MAA":
        cabecalho('Você se pergunta como esteve ela o culta aos olhos os demais e o que ela esconde?')
        sleep(5)
        escolha = ('Você escolhe entrar', 'Você escolhe não entrar')
        menu(escolha)
    if guia == "MAB":
        cabecalho('Te resta apenas preparar-se para luta')
    if guia == "MAB":
        cabecalho('Você vê aquele ato do forasteiro e se pergunta se deve ou não ir ao encalço do mago')
        sleep(5)
        escolha = ('Você corre atrás do mago', 'Você o deixa sair sem persegui-lo')
        menu(escolha)
    if guia == "MBB":
        cabecalho('Você sabe que aquela confusão é por sua culpa, e outra pessoa pode se ferir por sua culpa,')
        sleep(5)
        escolha = ('Você  não se mete na confusão', 'Você intervém na confusão')
        menu(escolha)