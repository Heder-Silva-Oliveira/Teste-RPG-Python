from Mago import *
from Caçador import *
from Roteiro import *
from Guerreiro import *
from Rolagem import *


print('Este é um jogo de RPG e tem a finalidade de desenvolver a tecnica de programação do autor')
criaturas = ('Orque', 'Elfo', 'Humano')
tipo = ('Guerreiro', 'Caçador', 'Mago')
atributos = {'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0,'Sabedoria': 0, 'Carisma': 0}
cabecalho('Criando o personagem')
personagem = {}
nome = str(input("Ecolha o nome do personagem: "))
menu(criaturas)
escolha = int(input("Ecolha a Raça: "))
menu(tipo)
escolha1 = int(input("Escolha a classe: "))
classe = ''
raca = ''
while True:
    if escolha == 1:
        raca = 'Orque'
        break
    elif escolha == 2:
        raca = 'Elfo'
        break
    elif escolha == 3:
        raca = 'Humano'
        break
    else:
        print('Raça não existente')
        escolha = input("Ecolha a Raça: ")
while True:
    if escolha1 == 1:
        classe = 'Guerreiro'
        break
    elif escolha1 == 2:
        classe = 'Caçador'
        break
    elif escolha1 == 3:
        classe = 'Mago'
        break
    else:
        print('Raça não existente')
        escolha = input("Ecolha a Classe: ")
for i, k in atributos.items():
    atributos[i] = randint(1, 20)

personagem["Nome"] = nome
personagem['Raça'] = raca
personagem['Classe'] = classe

print(atributos)
classmago = {'Sabedoria': 2, 'Inteligência': 1, 'Força': -1}
classguerreiro = {'Força': 2, 'Constituição': 1, 'Inteligência': -1}
classcacador = {'Destreza': 2, 'Carisma': 1, 'Força': -1}
classetotal = ([classmago], [classguerreiro], [classcacador])
cont = 0


def classper(escolha1):
    if escolha1 == 1:
        return classguerreiro
    if escolha1 == 2:
        return classcacador
    if escolha1 == 3:
        return classmago


for i in classper(escolha1):
    atributos[i] += classper(escolha1)[i]
    if atributos[i] > 20:
        atributos[i] = 20
    if atributos[i] < 1:
        atributos[i] = 1
    cont += 1
for i, k in atributos.items():
    print(f'Seu atributo {i} recebe o valor {k}')
print('Seus atributos com modificadores de Classe:')
print(atributos)
print()

intro(personagem['Classe'])
tiktak(10)
print()
guia = ''
decisao = 0
decisao1 = decisao3 = decisao20 = 0
if personagem['Classe'] == 'Mago':
    guia = 'M'
    cap1mag()
    decisao1 = int(input('Qual sua decisão?: '))
    while decisao1 not in (1, 2):
        decisao1 = int(input('Qual sua decisão?: '))
    jogomago(decisao1)
    if decisao1 == 1:
        guia += 'A'
    if decisao1 == 2:
        guia += 'B'
    tiktak(3)
    print()
    cap2mag()
    decisao2 = int(input('Qual sua decisão?'))
    while decisao2 not in (1, 2):
        decisao2 = int(input('Qual sua decisão?: '))
    jogodormago2(decisao1, decisao2)
    if decisao2 == 1:
        guia += 'A'
    if decisao2 == 2:
        guia += 'B'
    tiktak(5)
    print()
    cap3mag(guia)
    decisao3 = int(input("Qual sua decisão?: "))
    while decisao3 not in (1, 2):
        decisao3 = int(input('Qual sua decisão?: '))
    if decisao3 == 1:
        guia += 'A'
    if decisao3 == 2:
        guia += 'B'
    tiktak(3)
    jogodormago3(guia)
    if guia == 'MBBB' or 'MBBA' or 'MAB':
        vida = 20
        inimigo = 20
        while vida > 0 or inimigo > 0:
            if guia == 'MAAA':
                break
            if guia ==  "MAAB":
                break
            if guia ==  "MBAB":
                break
            if guia ==  "MBBA":
                break
            cabecalho(f'\033[1;31m O inimigo ataca, vida do inimigo {inimigo}\033[m')
            tiktak(6)
            inimigoataq = randint(1, 20)
            dano = randint(1, 6)
            vida -= dano
            batalhadefmag(inimigoataq, dano)
            cabecalho(f"\033[1;34m Você ataca, minha vida {vida}\033[m")
            tiktak(6)
            meuataq = 2 + randint(1, 20)
            dano = randint(1, 6)
            inimigo -= dano
            batalhaatqmag(meuataq, dano)
            if vida <= 0:
                print("A batalha se inicia, agora será rodado um dado de 20 lados, \n"
                      "se você acertar mais que 15, você consegue atingir o inimigo, \n"
                      "e depois um dado de 6 lados será lançado para definir quanto de\n"
                      "dano você eu, e o mesmo serve para ele te atacar")
                break
            if inimigo <= 0:
                print('Você vence o adversário')


elif personagem['Classe'] == 'Caçador':
    guia = 'C'
    cap1cac()
    decisao1 = int(input('Qual sua decisão?: '))
    while decisao1 not in (1, 2):
        decisao1 = int(input('Qual sua decisão?: '))
    jogocacador(decisao1)
    if decisao1 == 1:
        guia += 'A'
    if decisao1 == 2:
        guia += 'B'
    tiktak(10)
    print()
    cap2cac()
    decisao2 = int(input('Qual sua decisão?'))
    while decisao2 not in (1, 2):
        decisao2 = int(input('Qual sua decisão?: '))
    jogodorcacador2(decisao1, decisao2)
    if decisao2 == 1:
        guia += 'A'
    if decisao2 == 2:
        guia += 'B'

elif personagem['Classe'] == 'Guerreiro':
    guia = 'G'
    cap1gue()
    decisao1 = int(input('Qual sua decisão?: '))
    while decisao1 not in (1, 2):
        decisao1 = int(input('Qual sua decisão?: '))
    jogoguerreiro(decisao1)
    if decisao1 == 1:
        guia += 'A'
    if decisao1 == 2:
        guia += 'B'
    tiktak(10)
    print()
    cap2gue()
    decisao2 = int(input('Qual sua decisão?'))
    while decisao2 not in (1, 2):
        decisao2 = int(input('Qual sua decisão?: '))
    print("No seu caminho você encontra algo que te chama a atenção, você para e")
    itens()
    tiktak(3)
    jogoquerreiro2(decisao1, decisao2)
    if decisao2 == 1:
        guia += 'A'
    if decisao2 == 2:
        guia += 'B'

print('Suas escolhe te trouxeram até aqui, o que poderia resultar de ecolhas diferentes? \n'
      'vovê pode rejogar e fazer nova escolhas.')
print(guia)
