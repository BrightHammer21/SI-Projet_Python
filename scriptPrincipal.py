import csv
import character 
from random import *


characters_list = []


with open('characters.csv', newline='') as fichier:
    a = csv.reader(fichier, delimiter=',', quotechar=',')
    for row in a:
        print(', '.join(row))
        characters_list.append(''.join(row))




