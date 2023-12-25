import os
import json
import pandas as pd
import numpy as np
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from functions_stats import *

# function returns: Department; Region


def departement_region():
    """retourne la liste des départements dans chaque région"""

    Dic = {'Corse': []}
    file = open('./data/departements-region.csv', 'r', encoding='utf-8')
    List = ((file.read()).split('\n'))[1:]
    i = 0
    for line in List:
        departement = line.split(',')
        if i == 97:
            break
        if departement[2] == 'Corse':
            Dic[departement[2]].append(departement[0])
        elif departement[2] in Dic:
            Dic[departement[2]].append(int(departement[0]))
        else:
            Dic[departement[2]] = [int(departement[0])]
        i += 1
    return Dic

# following function returns:   classe; annee; Code.département; Code.région; unité.de.compte;faits;tauxpourmille


def read_and_load_crimes_committed():
    lst = []
    file = (open('./data/crimes_committed.csv', 'r',
            encoding='utf-8').read()).split('\n')
    check = True
# removing unecessary columns: POP, LOG, millPOP, millLOG
    for line in file:
        lne = line.split(';')
        del lne[5:7]
        del lne[6:8]
        if check:
            row1 = lne
            check = False
            continue
    # need to only include departments of France that are in the mainland
        try:
            if int(lne[2]) <= 96:
                lst.append(lne)
    # some department have a letter at the end and it needs to be removed (eg. 2A,2B)
        except:
            if int(lne[2][:-1]) <= 96:
                lst.append(lne)
    df = pd.DataFrame(lst, columns=row1)
    return df


# following function returns:   Department; Number of Gendarmerie; Number of Commissariat; Region


def read_and_load_gend_and_services():
    # function returns: Department; Number of Gendarmerie
    def read_and_load_gendarmaerie():
        dct = {k: 0 for k in range(1, 97)}
        file = (open(f'./data/gendarmerie.csv', 'r',
                encoding='utf-8').read()).split('\n')
        for line in file[1:]:
            lne = line.split(';')
            try:
                if int(int(lne[4][1:-1])) <= 96:
                    dct[int(lne[4][1:-1])] += 1
            except ValueError:
                if lne[4][1:-1] not in dct:

                    dct[lne[4][1:-1]] = 1
                else:
                    dct[lne[4][1:-1]] += 1
        df = pd.DataFrame(dct.items(), columns=[
            'Department', 'Number of Gendarmerie'])
        return (df)

    # function returns: Department; Number of Commissariat
    def read_and_load_services_de_police():
        dct = {k: 0 for k in range(1, 97)}
        file = (open(f'./data/services_de_police.csv', 'r',
                encoding='utf-8').read()).split('\n')
        for line in file[1:]:
            lne = line.split(';')
            try:
                if int(int(lne[3][1:-1])) <= 96:
                    dct[int(lne[3][1:-1])] += 1
            except ValueError:
                if lne[3][1:-1] not in dct:

                    dct[lne[3][1:-1]] = 1
                else:
                    dct[lne[3][1:-1]] += 1
        df = pd.DataFrame(dct.items(), columns=[
            'Department', 'Number of Commissariat'])
        return (df)

    # create dataframe joining both dataframes on Department
    dataframe1 = read_and_load_gendarmaerie().set_index('Department').join(
        read_and_load_services_de_police().set_index('Department'))
    dct2 = dict()
    for dept in dataframe1.index:
        for key in departement_region():
            if dept in departement_region()[key]:
                dct2[dept] = key
    dataframe2 = pd.DataFrame(dct2.items(), columns=['Department', 'Region'])
    # create dataframe joining exsting dataframe and region
    return dataframe1.merge(dataframe2.set_index('Department'), on='Department', how='left')


# When given a text (in french) will return the polarity and sentiment of the text as a tuple


def sentiment_analysis(text):
    blob = TextBlob(text, pos_tagger=PatternTagger(),
                    analyzer=PatternAnalyzer())
    return blob.sentiment

# read and load tweets from json format into a dataframe of columns: text;date;description;localisation;polarity;sentiment
# polarity: ranges between [-1,1] where 1 is positive and -1 is negative
# sentiment: ranges between [0,1] where the higher the number indicates the text is less subjective (higher personal opinion/emotions and has less factual information)


def process_tweets(filename):
    lst = []
    for file in [json_file for json_file in os.listdir(f'./{filename}')]:
        with open(f'./{filename}/' + file, encoding='utf-8') as json_file:
            data = json.load(json_file)
            lst.append({'text': data['text'],
                        'date': data['date'],
                        'description': data['description'],
                        'localisation': data['localisation'],
                        'polarity': round(sentiment_analysis(data['text'])[0], 2),
                        'sentiment': round(sentiment_analysis(data['text'])[1], 2)})
    return pd.DataFrame(lst)


# <-- process json folder into a dataframe and store as a csv with the following function
# process_tweets('Viol').to_csv('Viol.csv', index=False)


def useful_tweets():
    List_tweets_files = ['Viol.csv']
    # Creating an empty Dataframe with column names only
    dfObj = pd.DataFrame(
        columns=['text', 'date', 'description', 'localisation', 'polarity', 'sentiment'])
    file = open('./data/localisation_en_france.txt',
                'r', encoding='UTF8')
    localisation_en_france = (file.read()).split('\n')
    file.close()
    for tweets_file in List_tweets_files:
        df = pd.read_csv('./data/'+tweets_file)
        for i in df.index:
            localisation = df['localisation'][i]
            if isinstance(localisation, str):
                localisation = localisation.lower()
                T = False
                for place in localisation_en_france:
                    if place in localisation:
                        T = True
                        break
                if T == True:
                    dfObj = pd.concat([dfObj, df.loc[[i]]], ignore_index=True)

    return dfObj


def departement_nom():  # create dataframe with the link between department number and name
    """retourne la liste des départements et le nombre associé"""

    Dic = {'Number': [], 'Department': []}
    file = open('./data/departements-region.csv', 'r', encoding='utf-8')
    List = ((file.read()).split('\n'))[1:]
    i = 0
    for line in List:
        departement = line.split(',')
        i += 1
        if i == 96:
            break
        if departement[1] == 'Corse-du-Sud':
            Dic['Number'].append("2A")
            Dic['Department'].append("Corse-du-Sud")
            i = i - 1
        if departement[1] == 'Haute-Corse':
            Dic['Number'].append("2A")
            Dic['Department'].append("Haute-Corse")
        else:
            Dic['Number'].append(str(i))
            Dic['Department'].append(departement[1])
    return pd.DataFrame.from_dict(Dic)

# def function to create right dictionnary for each department

def right_dictionnary(i): # create the right dictionnary to plot data from the function nb_crimes_per_depart_per_year, i is the number of the department
    data = nb_crimes_per_depart_per_year()[str(i)]
    df = {}
    df["years"] = []
    df["crimes"] = []
    for elt in data:
        df["years"].append(elt)
        df["crimes"].append(data[elt])

    df = pd.DataFrame.from_dict(df)
    return df # for the department i we have a dictionnary {'year':[],'crimes':[]}
