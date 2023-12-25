import numpy as np
from PIL import Image
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd


# def makeImage(text):
#     tweet_mask = np.array(Image.open("./data/twitter_logo.png"))

#     wc = WordCloud(background_color="white", max_words=1000,
#                    mask=tweet_mask, contour_color='blue')
#     # generate word cloud
#     wc.generate_from_frequencies(text)

#     # show
#     image_colors = ImageColorGenerator(tweet_mask)
#     plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#     plt.axis("off")
#     plt.show()
#     return

def makeImage(filename):
    tweet_mask = np.array(Image.open("./data/twitter_logo.png"))
    wc = WordCloud(background_color="white", max_words=1000,
                   mask=tweet_mask, contour_color='blue')
    df = pd.read_csv(f'./data/{filename}', encoding='utf-8')
    dct = df.set_index('text').transpose().to_dict('int')
    wc.generate_from_frequencies(dct['count'])
    image_colors = ImageColorGenerator(tweet_mask)
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()
    return


# fusillade = {'fusillade': 2175, 'Martinique': 618, 'blessé': 607, 'ordre': 481, 'an': 442, 'matin': 379, 'blesser': 372, 'assassiner': 356, 'paix': 352, 'aujourd’hui': 351, 'repose': 351, 'King': 350, 'Von': 350, 'triste': 350, 'perte': 349, 'domaine': 333, 'Salée': 285, 'grave': 279, 'concert': 272, 'force': 267, 'devoir': 259, 'vendredi': 254, 'faire': 251, 'collège': 246, 'place': 245, 'Rivière': 245, 'secours': 234, 'foule': 222, 'oasis': 213, 'Laval': 211, 'nov.': 208, '3h': 208, 'mouvement': 208, 'STIS': 208, 'Montmorency': 200, 'armé': 166, 'suite': 163, 'survenir': 152, 'mois': 132, 'mort': 131, 'recevoir': 128, 'Oasis': 124, 'tenir': 123, 'feu': 121, 'événement': 121, 'établissement': 119, 'victime': 116, '⚖': 116, 'fermeture': 116,
#              'préfecture': 114, 'fermer': 114, 'immédiatement': 114, 'conséquent': 114, 'annuler': 114, 'étendre': 114, 'https://t.co/klktn6adwy': 114, '🔴': 112, 'policier': 112, 'campus': 104, 'civil': 103, 'tirer': 94, 'novembre': 91, 'violence': 91, 'ville': 90, 'aller': 87, 'homme': 85, 'rue': 85, 'police': 84, 'arme': 84, 'pensée': 81, '\xa0': 80, 'ouvrir': 80, 'lieu': 74, 'soir': 72, 'ALERTE': 67, '🇺': 66, 'reste': 63, 'donner': 62, 'Virginie': 62, '🇦': 58, '|': 57, 'contact': 55, 'soldat': 54, 'citoyen': 54, '08': 54, 'service':   53, 'maire': 53, 'prendre': 52, '2': 51, 'régulier': 51, 'dernier': 51, 'mercenaire': 51, 'cours': 51, 'Marioupol': 50, 'capturer': 50, 'avoue': 50, 'Géorgie': 50, 'évidence': 50, 'hier': 50, 'Canada': 49}
# viol = {'viol': 36083, 'ministre': 14619, 'agression': 7623, 'accuser': 7597, 'mettre': 6309, 'semaine': 5692, 'mec': 5641, 'dernier': 5617, 'rentrer': 5549, 'rue': 5541, 'retrouver': 5535, 'nuit': 5460, '⚠': 5410, 'présumé': 5403, '\xa0': 5372, 'secteur': 5340, 'AGRESSIONS': 5339, 'lille': 5338, 'République/': 5337, 'Gambetta': 5337, 'seul(': 5337, 'affaire': 4921, 'examen': 4838, 'faire': 4674, 'an': 4556, 'justice': 4228, 'compte': 4216, 'public': 4002, 'transition': 3755, 'écologique': 3739, 'corruption': 3733, 'pétrole': 3730, 'industrie': 3669, 'macronie': 3470, 'intérieur': 3211, 'femme': 3209, 'lier': 3208, 'sexuel': 3166, 'génial': 3155, 'devoir': 3113, 'savoir': 3106, 'aller': 3044, 'pouvoir': 2920, 'adolescent': 2860, 'homme': 2840, 'victime': 2502, 'jour': 2421, '15': 2176, 'menace': 2042, 'raid': 1928,
#         "qu'": 1917, 'Paris': 1854, 'discord': 1810, 'étudiant': 1793, 'réunion': 1778, 'Nantes': 1522, 'juger': 1517, 'migrant': 1487, 'prêtre': 1482, 'meurtre': 1467, 'bébé': 1463, '17': 1374, 'France': 1362, 'passer': 1359, 'droit': 1347, 'violence': 1333, 'université': 1323, 'prochain': 1321, 'jeune': 1318, 'professeur': 1249, 'assister': 1239, 'archéologie': 1239, '@SorbonneParis1': 1238, 'Sorbonne': 1237, 'excellence': 1236, 'td': 1231, 'semestre': 1230, 'etudiante': 1229, 'Panthéon': 1229, 'fille': 1227, 'âgé': 1224, 'acte': 1212, 'suite': 1145, 'police': 1105, 'organiser': 1105, 'Vendée': 1084, 'alors': 1045, 'trouver': 1027, 'condamner': 1019, 'essayer': 994, 'voir': 992, 'mineur': 985, 'décrire': 975, 'équipe': 956, 'député': 951, 'Rennes': 949, 'mourir': 944, 'saisir': 934, 'Twitch': 931, 'juridique': 922}
# police = {'police': 46963, 'aller': 10582, 'faire': 7400, 'migrant': 6849, 'savoir': 5617, 'soignant': 5227, '\xa0': 4883, 'français': 4873, 'policier': 4817, 'passeur': 4308, 'italien': 4299, 'convoquer': 4287, 'ong': 4277, 'an': 4177, '…': 4131, 'alors': 3862, 'mal': 3846, 'France': 3689, 'suspendre': 3659, 'révéler': 3622, 'complicité': 3536, 'groupe': 3491, 'point': 3443, 'membre': 3404, 'déjà': 3384, 'existence': 3273, '70': 3273, 'échanger': 3269, 'traversée': 3267, 'emprunter': 3264, 'précis': 3261, 'gp': 3261, 'coordonné': 3258, 'WhatsApp': 3257, 'voir': 2942, 'devenir': 2755, 'famille': 2652, 'mort': 2645, 'avérer': 2605, 'pouvoir': 2582, 'autorité': 2532, '😡': 2525, 'novembre': 2512, 'jour': 2469, 'vouloir': 2386, '10': 2105, 'placer': 2028, 'arrêter': 2024, 'peur': 1978, 'homme': 1962, 'Gravelines': 1899,
#           'prendre': 1863, 'femme': 1856, 'service': 1817, 'municipal': 1817, 'ALERTE': 1815, 'petit': 1719, 'etat': 1691, 'Dunkerque': 1671, '🇷': 1667, 'devoir': 1591, 'nouveau': 1584, 'vaccination': 1540, 'eenquête': 1534, 'matin': 1523, 'attaquer': 1522, 'expulser': 1507, '🔴': 1502, 'justice': 1495, 'mairie': 1480, 'refus': 1437, 'convocation': 1418, 'public': 1414, 'suite': 1411, 'discrètement': 1399, 'média': 1396, '@cstrateges': 1374, 'autoritaire': 1358, 'suspension': 1357, 'punis': 1355, 'https://t.co/6uexmxm1es': 1355, 'peuple': 1340, 'interdire': 1332, 'pays': 1330, 'massif': 1326, '🇫': 1324, 'actuellement': 1323, '🛑': 1319, 'empêcher': 1268, 'appeler': 1264, 'tentative': 1247, 'attentat': 1237, 'bbateau': 1236, 'tenter': 1235, 'signaler': 1229, 'mettre': 1227, 'lien': 1211, 'LFI': 1208, 'Iran': 1201, 'député': 1197}
# all = {'police': 13538, 'viol': 10719, 'ministre': 3878, 'aller': 3780, 'faire': 3718, '\xa0': 3091, 'an': 2776, 'agression': 2675, 'savoir': 2483, 'migrant': 2355, 'accuser': 2321, 'nuit': 2311, 'dernier': 2215, 'rue': 2207, 'mettre': 2177, 'retrouver': 2164, 'semaine': 2150, 'mec': 2102, 'rentrer': 2034, '⚠': 2015, 'secteur': 1979, 'lille': 1973, 'présumé': 1966, 'AGRESSIONS': 1958, 'République/': 1958, 'Gambetta': 1958, 'seul(': 1958, 'français': 1580, 'jour': 1553, 'femme': 1533, 'affaire': 1520, 'homme': 1517, 'justice': 1492, 'France': 1436, '…': 1432, 'public': 1423, 'pouvoir': 1407, 'examen': 1392, 'devoir': 1387, 'alors': 1380, 'soignant': 1354, 'policier': 1319, 'passeur': 1248, 'italien': 1242, 'ong': 1234, 'compte': 1206, 'déjà': 1114, 'mort': 1111, 'convoquer': 1109,
#    'point': 1082, 'groupe': 1065, 'révéler': 1062, 'voir': 1042, 'victime': 1031, 'mal': 1025, 'membre': 1022, 'complicité': 1018, 'industrie': 1011, '70': 979, 'corruption': 960, 'suspendre': 955, 'échanger': 951, 'existence': 948, 'écologique': 948, 'transition': 947, 'macronie': 944, 'WhatsApp': 944, 'précis': 944, 'traversée': 944, 'pétrole': 943, 'gp': 942, 'emprunter': 942, 'coordonné': 941, 'sexuel': 937, 'Paris': 923, 'intérieur': 921, 'jeune': 871, 'adolescent': 868, 'prendre': 859, 'novembre': 858, 'raid': 852, '15': 847, 'vouloir': 831, 'lier': 819, 'suite': 818, '🔴': 811, 'génial': 793, '😡': 788, 'municipal': 780, 'menace': 768, 'avérer': 747, 'devenir': 744, 'fusillade': 730, 'famille': 730, 'autorité': 709, 'matin': 694, "qu'": 693, 'député': 689, 'bébé': 688, '10': 677}
# makeImage('most_used_100_fusillade.csv')

