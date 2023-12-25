import pandas as pd
from utils import *

#############################################################################################################


def nb_crimes_per_depart_global():

    ### returns a dictionnary with de the following form : {nb of depart : nb of crimes} ###

    df = read_and_load_crimes_committed()
    nb_crimes = {i: 0 for i in [str(i) for i in range(1, 97)]}
    nb_crimes['2A'] = 0  # La corse
    nb_crimes['2B'] = 0  # La corse encore...

    for idx in df.index:
        dep = df['Code.département'][idx]
        crimes = df['faits'][idx]

        # fix issues such as 01 (can't convert into int immediately)

        if dep[0] == '0':
            dep = dep[1]

        nb_crimes[dep] = nb_crimes[dep] + int(crimes)

    return nb_crimes


#############################################################################################################

def nb_crimes_per_depart_per_year():

    ### returns a dictionnary with de the following form : {nb of depart : {year, nb of crimes this year}} ###

    df = read_and_load_crimes_committed()
    nb_crimes = {i: dict() for i in [str(i) for i in range(1, 97)]}
    nb_crimes['2A'] = dict()  # La corse
    nb_crimes['2B'] = dict()  # La corse encore...

    for idx in df.index:

        # ne donne que les deux derniers chiffres de l'année dans la database
        year = "20" + df['annee'][idx]
        dep = df['Code.département'][idx]
        crimes = df['faits'][idx]

        # fix issues such as 01 (can't convert into int immediately)

        if dep[0] == '0':
            dep = dep[1]

        if year not in nb_crimes[dep]:
            nb_crimes[dep][year] = int(crimes)
        else:
            nb_crimes[dep][year] = nb_crimes[dep][year] + int(crimes)

    return nb_crimes


# print(nb_crimes_per_depart_per_year())

def formating(dict):
    return pd.DataFrame(list(dict.items()),
                        columns=['Département', 'Nombre de délits et crimes'])


# print(formating(nb_crimes_per_depart_global()))
