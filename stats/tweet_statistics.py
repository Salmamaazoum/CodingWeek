import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py
import plotly.tools as tls
from dash import dcc
# plots are returns a histogram of tweet polarity for each dataframe(BY PROPORTION)

# plotting histogram for polarity where the frequency is measured by proportion


def plot_polarity_histogram():
    df1 = pd.read_csv('./data/Fusillade.csv')
    df2 = pd.read_csv('./data/Police.csv')
    df3 = pd.read_csv('./data/Viol.csv')

    fig, ax = plt.subplots()

# set height, range and weights
    a_heights, a_bins = np.histogram(
        df1['polarity'], range=[-1, 1], weights=np.ones_like(df1['polarity'])/len(df1))
    b_heights, b_bins = np.histogram(
        df2['polarity'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df2['polarity'])/len(df2))
    c_heights, c_bins = np.histogram(
        df3['polarity'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df3['polarity'])/len(df3))

    width = (a_bins[1] - a_bins[0])/4

# set color and width
    ax.bar(a_bins[:-1], a_heights, width=width,
           facecolor='cornflowerblue', label='Fusillade')
    ax.bar(b_bins[:-1]+width, b_heights, width=width,
           facecolor='palegreen', label='Police')
    ax.bar(c_bins[:-1]+2*width, c_heights, width=width,
           facecolor='firebrick', label='Viol')

# setting labels
    ax.legend()
    ax.set_title('Histogram by proportion of polarity in tweets')
    ax.set_xlabel('Polarity')
    ax.set_ylabel('Frequency')
    plt.show()
    return

# plotting histogram for sentiment where the frequency is measured by proportion


def plot_sen_histogram():
    df1 = pd.read_csv('./data/Fusillade.csv')
    df2 = pd.read_csv('./data/Police.csv')
    df3 = pd.read_csv('./data/Viol.csv')

    fig, ax = plt.subplots()

# set height, range and weights

    a_heights, a_bins = np.histogram(
        df1['sentiment'], range=[-1, 1], weights=np.ones_like(df1['sentiment'])/len(df1))
    b_heights, b_bins = np.histogram(
        df2['sentiment'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df2['sentiment'])/len(df2))
    c_heights, c_bins = np.histogram(
        df3['sentiment'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df3['sentiment'])/len(df3))

# set color and width

    width1 = (a_bins[1] - a_bins[0])/4

    ax.bar(a_bins[:-1], a_heights, width=width1,
           facecolor='cornflowerblue', label='Fusillade')
    ax.bar(b_bins[:-1]+width1, b_heights, width=width1,
           facecolor='palegreen', label='Police')
    ax.bar(c_bins[:-1]+2*width1, c_heights, width=width1,
           facecolor='firebrick', label='Viol')


# setting labels
    ax.legend()
    ax.set_title('Histogram by proportion of sentiment in tweets')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Frequency')
    plt.show()
    return

# plot histogram containing both polarity and sentiment by proportion


def plot_tweet_histogram():
    df1 = pd.read_csv('./data/Fusillade.csv')
    df2 = pd.read_csv('./data/Police.csv')
    df3 = pd.read_csv('./data/Viol.csv')

    fig, ax = plt.subplots()

    a_heights, a_bins = np.histogram(
        df1['sentiment'], range=[-1, 1], weights=np.ones_like(df1['sentiment'])/len(df1))
    b_heights, b_bins = np.histogram(
        df2['sentiment'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df2['sentiment'])/len(df2))
    c_heights, c_bins = np.histogram(
        df3['sentiment'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df3['sentiment'])/len(df3))
    d_heights, d_bins = np.histogram(
        df1['polarity'], range=[-1, 1], weights=np.ones_like(df1['polarity'])/len(df1))
    e_heights, e_bins = np.histogram(
        df2['polarity'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df2['polarity'])/len(df2))
    f_heights, f_bins = np.histogram(
        df3['polarity'], range=[-1, 1], bins=a_bins, weights=np.ones_like(df3['polarity'])/len(df3))

    width1 = (a_bins[1] - a_bins[0])/4
    width2 = (d_bins[1]-d_bins[0])/4

    ax.bar(a_bins[:-1], a_heights, width=width1,
           facecolor='darkblue', label='Fusillade-sentiment', alpha=0.6)
    ax.bar(b_bins[:-1]+width1, b_heights, width=width1,
           facecolor='darkgreen', label='Police-sentiment', alpha=0.6)
    ax.bar(c_bins[:-1]+2*width1, c_heights, width=width1,
           facecolor='darkred', label='Viol-sentiment', alpha=0.6)
    ax.bar(d_bins[:-1], d_heights, width=width2,
           facecolor='blue', label='Fusillade-polarity', alpha=0.6)
    ax.bar(e_bins[:-1]+width2, e_heights, width=width2,
           facecolor='lawngreen', label='Police-polarity', alpha=0.7)
    ax.bar(f_bins[:-1]+2*width2, f_heights, width=width2,
           facecolor='orangered', label='Viol-polarity', alpha=0.7)

    ax.legend()
    ax.set_title('Histogram by proportion of polarity and sentiment in tweets')
    ax.set_ylabel('Frequency')
    plt.show()
    return
