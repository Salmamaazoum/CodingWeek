import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# plots are returns a histogram of tweet polarity for each dataframe(BY PROPORTION)
def plot_tweet_histogram():
    df1 = pd.read_csv('./tweets/Fusillade.csv')
    df2 = pd.read_csv('./tweets/Police.csv')
    df3 = pd.read_csv('./tweets/Viol.csv')
    df4 = pd.read_csv('./tweets/Crime.csv')

    fig, ax = plt.subplots()

    a_heights, a_bins = np.histogram(
        df1['polarity'], weights=np.ones_like(df1['polarity'])/len(df1))
    b_heights, b_bins = np.histogram(
        df2['polarity'], bins=a_bins, weights=np.ones_like(df2['polarity'])/len(df2))
    c_heights, c_bins = np.histogram(
        df3['polarity'], bins=a_bins, weights=np.ones_like(df3['polarity'])/len(df3))
    d_heights, d_bins = np.histogram(
        df4['polarity'], bins=a_bins, weights=np.ones_like(df4['polarity'])/len(df4))

    width = (a_bins[1] - a_bins[0])/5

    ax.bar(a_bins[:-1], a_heights, width=width,
           facecolor='cornflowerblue', label='Fusillade')
    ax.bar(b_bins[:-1]+width, b_heights, width=width,
           facecolor='palegreen', label='Police')
    ax.bar(c_bins[:-1]+2*width, c_heights, width=width,
           facecolor='firebrick', label='Viol')
    ax.bar(d_bins[:-1]+3*width, d_heights, width=width,
           facecolor='goldenrod', label='Crime')
    ax.legend()
    ax.set_title('Histogram by proportion of polarity in tweets')
    ax.set_xlabel('Polarity')
    ax.set_ylabel('Frequency')
    plt.show()
    return


plot_tweet_histogram()

# More things TODO to make histogram nicer:
# Add KDE plots for each plot individually
# Add buttons thing to switch between plots
# maybe still need histogram for each set of data to display it without proportion
