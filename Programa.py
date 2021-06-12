from random import randint
from Organizador import *
from Mago import *
from Caçador import *
from Roteiro import *
from Guerreiro import *
from Rolagem import *


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
print(atributos)
print()

intro(personagem['Classe'])
sleep(2)
decisao1 = 0
decisao2 = 0
if personagem['Classe'] == 'Mago':
    cap1mag()
    decisao1 = int(input('Qual sua decisão?: '))
    jogomago(decisao1)
    sleep(5)
    cap2mag()
    decisao2 = int(input('Qual sua decisão?'))
    jogodormago2(decisao1, decisao2)
elif personagem['Classe'] == 'Caçador':
    cap1cac()
    decisao1 = int(input('Qual sua decisão?: '))
    jogocacador(decisao1)
    sleep(5)
    cap2cac()
    decisao2 = int(input('Qual sua decisão?'))
    jogodorcacador2(decisao1, decisao2)
elif personagem['Classe'] == 'Guerreiro':
    cap1gue()
    decisao1 = int(input('Qual sua decisão?: '))
    jogoguerreiro(decisao1)
    sleep(5)
    cap2gue()
    decisao2 = int(input('Qual sua decisão?'))
    jogoquerreiro2(decisao1, decisao2)


if classmago:
    inimigoataq = randint(1, 20)
    meuatq = randint(1, 20)
    print(f'Minha rolagem do D20 foi {meuatq} somando meu atributo é {atributos["Sabedoria"]}')
    print(f'O ataque inimigo foi de {inimigoataq}, minha CA é de {12}')
    if inimigoataq >= 20:
        print('Vocçe foi atingio')
        rels = randint(1, 6)
        dado6(rels)
    else:
        print('Você não foi atingio')


