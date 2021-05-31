from Organizador import *
from time import sleep

from Organizador import cabecalho


def cap1gue():
    cabecalho('Seu grande cansaso esta em dilema com sua bravura em batalha')
    sleep(5)
    escolha = ('Você recua para recuperar o vigor ','Você se esforça e permanece na batalha')
    menu(escolha)


#se for a escolha 2
def cap2gue():
    cabecalho('continua')
    sleep(5)
    escolha2 = ('continua', 'continua')
    menu(escolha2)
