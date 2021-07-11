from Organizador import *


def cap1cac():
    cabecalho('tensionando o arco, em direção ao barulho, você ja de pé escuta muitos outros destes barulhos')
    sleep(5)
    escolha = ('Você tenta se esconder', 'Você atira a flexa no servo')
    menu(escolha)


#se for a escolha 2
def cap2cac():
    cabecalho('Você consegue abater e esfolar um servo, agora você tem carne e couro obastante para vender')
    sleep(5)
    escolha = ('Você vai direto para vila vender o ecedente', 'Você vai direto para casa guardar tudo')
    menu(escolha)


def cap3cac(guia):
    if guia == "MAA":
        cabecalho('')
        sleep(5)
        escolha = ('')
        menu(escolha)
    if guia == "MAB":
        cabecalho('')
    if guia == "MAB":
        cabecalho('')
        sleep(5)
        escolha = ('')
        menu(escolha)
    if guia == "MBB":
        cabecalho(',')
        sleep(5)
        escolha = ('')
        menu(escolha)





