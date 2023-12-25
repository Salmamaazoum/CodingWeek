import argparse
import word_cloud
import localisation
import tweet_statistics
import most_used_words
import sys
import os


if __name__ == "__main__":
    # creating parser
    my_parser = argparse.ArgumentParser(
        prog='main.py', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40), description='Crime and tweet statistics for France', usage='python %(prog)s [options]')
    # adding different options to the parser
    my_parser.add_argument('-tp', '--table_polarity', action='store_true', required=False,
                           help='see Tweet Polarity barchart')
    my_parser.add_argument('-ts', '--table_sentiment', action='store_true', required=False,
                           help='see Tweet Sentiment barchart')
    my_parser.add_argument('-ta', '--table_all', action='store_true', required=False,
                           help='see Tweet polarity and sentiment barcharts')
    my_parser.add_argument('-bl', '--barloc', action='store_true',
                           help='see barchart of tweet location distribution')
    my_parser.add_argument('-wf', '--wordfrequency', action='store', choices=['police', 'viol', 'fusillade', 'all'], required=False,
                           metavar='[data]', type=str, nargs=1, help='see word frequency for each dataset (police,fusillade,viol,all)')
    my_parser.add_argument('-wc', '--wordcloud', action='store', choices=['police', 'viol', 'fusillade', 'all'], required=False,
                           metavar='[data]', type=str, nargs=1, help='see word cloud for each dataset (police,fusillade,viol,all)')
    # parse parser
    args = my_parser.parse_args()
    # setting options to call functions or run files
    if len(sys.argv) == 1:
        with open("./app.py", 'rb') as f:
            code = compile(f.read(), "./app.py", "exec")
        exec(code)
    if args.table_all:
        tweet_statistics.plot_tweet_histogram()
    if args.table_sentiment:
        tweet_statistics.plot_sen_histogram()
    if args.table_polarity:
        tweet_statistics.plot_polarity_histogram()
    if args.barloc:
        localisation.freq_places()
    if args.wordfrequency != None:
        most_used_words.plot_freq_words(
            'most_used_'+args.wordfrequency[0]+'.csv')
    if args.wordcloud != None:
        word_cloud.makeImage('most_used_100_'+args.wordcloud[0]+'.csv')
