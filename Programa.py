from Organizador import *
from random import randint

criaturas = ('Orque', 'Elfo', 'Humano')
tipo = ('Guereiro', 'Caçador', 'Mago')
atributos = {'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0,'Sabedoria': 0, 'Carisma': 0}
cabeçalho('Criando o personagem')
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
        classe = 'Guereiro'
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
print(personagem)
print(atributos)
if personagem['Raça'] == 'Orque':
    atributos['Força'] += 2
    atributos['Constituição'] += 1
    atributos['Carisma'] -= 2
if personagem['Raça'] == 'Elfo':
    atributos['Inteligência'] += 2
    atributos['Sabedoria'] += 1
    atributos['Força'] -= 2
if personagem['Raça'] == 'Humano':
    atributos['Força'] += 1
    atributos['Destreza'] += 1
    atributos['Carisma'] -= 1
if personagem['Classe'] == 'Guerreiro':
    atributos['Força'] += 2
    atributos['Constituição'] += 1
if personagem['Classe'] == 'Caçador':
    atributos['Destreza'] += 2
    atributos['Carisma'] += 1
if personagem['Classe'] == 'Mago':
    atributos['Sabedoria'] += 2
    atributos['Inteligência'] += 1
print(atributos)