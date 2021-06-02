from random import randint
from Organizador import *
from Mago import *
from Caçador import *
from Roteiro import *
from Guerreiro import *


criaturas = ('Orque', 'Elfo', 'Humano')
tipo = ('Guereiro', 'Caçador', 'Mago')
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

print(atributos)
classmago = {'Sabedoria': 2, 'Inteligência': 1}
classguerreiro = {'Força': 2, 'Constituição': 1}
classcacador = {'Destreza': 2, 'Carisma': 1}
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
    cont += 1
for i, k in atributos.items():
    if k > 20:
        k = 20
    if k < 1:
        k = 1
    print(f'Seu atributo {i} recebe o valor {k}')
print(atributos)


intro(personagem['Classe'])
sleep(2)
if personagem['Classe'] == 'Mago':
    cap1mag()
    decisao = int(input('Qual sua decisão?: '))
    jogomago(decisao)
    sleep(5)
    cap2mag()
elif personagem['Classe'] == 'Caçador':
    cap1cac()
    decisao = int(input('Qual sua decisão?: '))
    jogocacador(decisao)
    sleep(5)
    cap2cac()
elif personagem['Classe'] == 'Guerreiro':
    cap1gue()
    decisao = int(input('Qual sua decisão?: '))
    jogoguerreiro(decisao)
    sleep(5)
    cap2gue()
print("CONTINUA...")
