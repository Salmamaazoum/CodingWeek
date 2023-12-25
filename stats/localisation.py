import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import heapq
from operator import itemgetter


def localisations(filename):
    df = pd.read_csv('./data/'+filename)
    file = open('./data/localisation_en_france.txt', 'r', encoding='UTF8')
    localisation_en_france = (file.read()).split('\n')
    file.close()
    L = []
    france = 0
    outside = 0
    no_data = 0
    for i in df.index:
        localisation = df['localisation'][i]
        if isinstance(localisation, str):
            localisation = localisation.lower()
            T = False
            for place in localisation_en_france:
                if place in localisation:
                    T = True
                    break
            if T == False:
                outside += 1
            else:
                france += 1
        else:
            no_data += 1
    return (france, outside, no_data)


def graph(filename):
    stats = localisations(filename)
    sum = stats[0]+stats[1]+stats[2]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'In_France', 'Outside_france', 'Unknown'
    sizes = [stats[0]*(360/sum), stats[1]*(360/sum), stats[2]*(360/sum)]
    explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title("tweets origin #"+(filename[:-4]), fontsize=15)

    plt.show()
    return


def local_useful_tweets():
    df = pd.read_csv('./data/useful_tweets.csv')
    D = dict()
    for i in df.index:
        a = (((df['localisation'][i]).lower()).split(','))[0]
        if a in D:
            D[a] += 1
        else:
            D[a] = 1
    return D


def freq_places():
    Dic0 = local_useful_tweets()
    Dic = dict()
    file = open('./data/localisation_en_france.txt', 'r', encoding='UTF8')
    localisation_en_france = ((file.read()).split('\n'))[:74]
    file.close()
    for place in Dic0:
        if place in localisation_en_france:
            Dic[place] = Dic0[place]
    topitems = heapq.nlargest(30, Dic.items(), key=itemgetter(1))
    topitemsasdict = dict(topitems)
    topics, numbers = list(topitemsasdict.keys()), topitemsasdict.values()
    topics = list(topics)
    gridsize = (16, 3)
    fig = plt.figure(figsize=(10, 3))
    topics_axis = np.arange(len(topics))
    plt.bar(topics_axis + 0.5, numbers, 0.2, color='tomato')
    plt.xticks(topics_axis, topics, rotation=30)
    plt.ylabel("Number of tweets from this location")
    plt.title("tweets origin", fontsize=15)
    plt.show()
    return


# freq_places()
# graph('Fusillade.csv')
