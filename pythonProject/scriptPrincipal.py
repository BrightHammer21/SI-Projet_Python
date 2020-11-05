import csv
import character 
from random import *


characters_list = []

with open('characters.csv', newline='') as fichier:
    a = csv.reader(fichier, delimiter=',', quotechar=',')
    for row in a:
       characters_list.append(character.Character(*row))



