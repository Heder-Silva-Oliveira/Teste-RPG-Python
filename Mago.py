from Organizador import *
from time import sleep

from Organizador import cabecalho


def cap1mag():
    cabecalho('Tudo isso começa a te incomodar e você fica diante de duas escolhas')
    sleep(5)
    escolha = ('Você tenta abrir o olho e se livrar disso', 'Você tenta manter o foco e encontrar a reposta')
    menu(escolha)


def cap2mag():
    cabecalho('Ao seu redor varios outros magos, a maioria ja havia desistido, e apenas dois ainda continuam o intento')
    sleep(5)
    escolha2 = ('Você decide deixa-los concentrados em conjurar a aurea', 'Você tenta discretamente desconcentra-los')
    menu(escolha2)


def cap3mag():
    cabecalho('')