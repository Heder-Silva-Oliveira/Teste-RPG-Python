from Organizador import *
from time import sleep

from Organizador import cabecalho


def cap1gue():
    cabecalho('Seu grande cansaso esta em dilema com sua bravura em batalha')
    sleep(5)
    escolha = ('Você recua para recuperar o vigor ','Você se esforça e permanece na batalha')
    menu(escolha)


def cap2gue():
    cabecalho('A batalha acabou, sem gloria porem com a vitoria, você você vê alguns amigos, proximo a fogueira')
    sleep(5)
    escolha2 = ('Você vai ao encontro beber sobre a vitoria', 'Você vai até os feridos consola-los')
    menu(escolha2)


def cap3gue(guia):
    if guia == "MAA":
        cabecalho('')
        sleep(5)
        escolha = ('Preciso de criatividade')
        menu(escolha)
    if guia == "MAB":
        cabecalho('')
    if guia == "MAB":
        cabecalho('')
        sleep(5)
        escolha = ('')
        menu(escolha)
    if guia == "MBB":
        cabecalho('')
        sleep(5)
        escolha = ('')
        menu(escolha)