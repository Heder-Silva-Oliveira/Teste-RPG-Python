from Organizador import *

criaturas = ('Orque', 'Elfo', 'Humano')
classe = ('Guereiro', 'Caçador', 'Mago')
atributos = {'Força': 0, 'Destreza': 0, 'Constituição': 0, 'Inteligência': 0,'Sabedoria': 0, 'Carisma': 0}
cabeçalho('Criando o personagem')
personagem = {}
nome = str(input("Ecolha o nome do personagem: "))
menu(criaturas)
escolha = int(input("Ecolha a Raça: "))
raca = ''
if escolha == 1:
    raca = 'Orque'
elif escolha == 2:
    raca = 'Elfo'
elif escolha == 3:
    raca = 'Humano'
else:
    print('Raça não existente')
    escolha = input("Ecolha a Raça: ")


personagem["Nome"] = nome
personagem['Raça'] = raca

print(personagem)