import pandas as pd
import random

 # Parte 1
df = pd.read_csv('https://raw.githubusercontent.com/Matheusisac/previsaocopa/main/dados.csv')

class Team:
    Bestscore = 1837.6
    def __init__(self, content):
        teamData = content.split('|')
        self.name = teamData[0]
        self.score = float(teamData[1])

    def motivate(self):
        """ 
        A pior seleção da copa (GAN, segundo a FIFA) têm 1393.5 de score, o qual equivale a 75% do melhor score (BRA).
        Sendo assim, para que a aleatoriedade não seja tão determinante, podemos definir um intervalo inicial próximo de 75.
        Por exemplo, GAN poderia ter valores entre 70~75 (aproximadamente). Por outro lado, BRA teria 70~100 (maior chance de vitória).
        """
        self.lastMotivation = random.uniform(70, (self.score * 100)/Team.Bestscore)
        return self.lastMotivation


#Parte 2


# Mapa em que a chave será a letra do grupo e o valor as seleções (que ordenaremos pelas "melhores").
bestTeamsByGroup = {}
# Percorre o dataframe (dados do CSV) para criar nossos objetos/seleções.
for label, content in df.items():
    team1 = Team(content[0])
    team2 = Team(content[1])
    team3 = Team(content[2])
    team4 = Team(content[3])

    bestTeamsByGroup[label] = sorted([team1,team2,team3,team4], key = Team.motivate, reverse= True)

# TODO: Imprimir os grupos, ordenados pelas melhores seleções de cada (apenas 2 se classificam)
for grupo, motivatedTeams in bestTeamsByGroup.items():
  print(f'Grupo {grupo}: ', end="")
  for team in motivatedTeams:
    print(f'{team.name} ({team.lastMotivation:.2f}) ', end="")
  print()

#Parte 3


# Criando vaiáveis para as 2 melhores seleções de cada grupo:
team1A = bestTeamsByGroup['A'][0]
team2A = bestTeamsByGroup['A'][1]
team1B = bestTeamsByGroup['B'][0]
team2B = bestTeamsByGroup['B'][1]
team1C = bestTeamsByGroup['C'][0]
team2C = bestTeamsByGroup['C'][1]
team1D = bestTeamsByGroup['D'][0]
team2D = bestTeamsByGroup['D'][1]
team1E = bestTeamsByGroup['E'][0]
team2E = bestTeamsByGroup['E'][1]
team1F = bestTeamsByGroup['F'][0]
team2F = bestTeamsByGroup['F'][1]
team1G = bestTeamsByGroup['G'][0]
team2G = bestTeamsByGroup['G'][1]
team1H = bestTeamsByGroup['H'][0]
team2H = bestTeamsByGroup['H'][1]

quarta1 = team1A if team1A.motivate() > team2B.motivate() else team2B
quarta2 = team1C if team1C.motivate() > team2D.motivate() else team2D
quarta3 = team1E if team1E.motivate() > team2F.motivate() else team2F
quarta4 = team1G if team1G.motivate() > team2H.motivate() else team2H
quarta5 = team1B if team1B.motivate() > team2A.motivate() else team2A
quarta6 = team1D if team1D.motivate() > team2C.motivate() else team2C
quarta7 = team1F if team1F.motivate() > team2E.motivate() else team2E
quarta8 = team1H if team1H.motivate() > team2G.motivate() else team2G

#Parte 4

semi1 = quarta1 if quarta1.motivate() > quarta2.motivate() else quarta2
semi2 = quarta3 if quarta3.motivate() > quarta4.motivate() else quarta4
semi3 = quarta5 if quarta5.motivate() > quarta6.motivate() else quarta6
semi4 = quarta7 if quarta7.motivate() > quarta8.motivate() else quarta8

#Parte 5

if semi1.motivate() > semi2.motivate():
    final1 = semi1
    terceiro1 = semi2
else:
    final1 = semi2
    terceiro1 = semi1
    
if semi3.motivate() > semi4.motivate():
    final2 = semi3
    terceiro2 = semi4
else:
    final2 = semi4
    terceiro2 = semi3

#Parte 6

if final1.motivate() > final2.motivate():
    Primeiro = final1
    Segundo = final2
else: 
    Primeiro = final2
    Segundo = final1


if terceiro1.motivate() > terceiro2.motivate():
    Terceiro = terceiro1
    Quarto = terceiro2
else: 
    Terceiro = terceiro2
    Quarto = terceiro1

print(f'\nPrimeiro: {Primeiro.name} ({Primeiro.motivate():.2f})')
print(f'Segundo: {Segundo.name} ({Segundo.motivate():.2f})')
print(f'Terceiro: {Terceiro.name} ({Terceiro.motivate():.2f})')
print(f'Quarto: {Quarto.name} ({Quarto.motivate():.2f})')
