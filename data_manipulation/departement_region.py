import os


def departement_region():
    """retourne la liste des départements dans chaque région"""

    Dic = {'Corse': []}
    file = open('./data/departements-region.csv', 'r', encoding='utf-8')
    List = ((file.read()).split('\n'))[1:]
    i = 0
    for line in List:
        departement = line.split(',')
        if i == 96:
            break
        if departement[2] == 'Corse':
            Dic[departement[2]].append(departement[0])
        elif departement[2] in Dic:
            Dic[departement[2]].append(int(departement[0]))
        else:
            Dic[departement[2]] = []
        i += 1
    return Dic
