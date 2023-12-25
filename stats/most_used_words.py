import heapq
from operator import itemgetter
import pandas as pd
import word_cloud as wc
import matplotlib.pyplot as plt
import numpy as np
import spacy
from textblob import TextBlob, Word
from textblob_fr import PatternAnalyzer, PatternTagger
import fr_core_news_md

nlp = spacy.load('fr_core_news_md')


def list_mots_unitils():
    f = open('./data/list_mots_unitils.txt', 'r', encoding='utf-8')
    List = (f.read()).split("\n")
    f.close()
    return List


def tweet_to_words(tweet):
    """ Revoie la liste des mots lématisées utilisés dans le tweet """
    Mots_lematises = []
    tweet = nlp(tweet)
    List = list_mots_unitils(
    )+['.', '..', '...', '#', '!', 'v.roy', '?', '🏼', ',', ":", '"', '»', '\n', '🕊', 'qu’', '🙏', '📆', '🚑', '❗', "-", "(", "n'", 'l’', '\n\n', 'd’', 'lors', '11', '6', ' ', '️', 's’', '7', '[', '/', ')', ']', '3', 'https://t.co/X3qx8ZyXji', '\n', 'rappeur', 'Resca', 'https://t.co/rd1irgaw7e', 'c’', '1', 'n’', '«']
    for token in tweet:
        mot = token.lemma_
        if mot not in List:
            Mots_lematises.append(mot)
    return Mots_lematises


def most_used(filename):
    Dic = dict()
    df = pd.read_csv('./data/'+filename)
    tweets = df['text']
    for i in tweets.index:
        tweet = tweets[i]
        Mots_utils = tweet_to_words(tweet)
        for mot in Mots_utils:
            if mot in Dic:
                Dic[mot] += 1
            else:
                Dic[mot] = 1
    topitems = heapq.nlargest(40, Dic.items(), key=itemgetter(1))
    topitemsasdict = dict(topitems)
    return topitemsasdict

# Plots barchart showing frequncy of top 40 words


def plot_freq_words(filename):
    df = pd.read_csv(f'./data/{filename}', encoding='utf-8')
    ax = df.plot.bar(x='text', y='count', rot=45)
    plt.show()
    return
