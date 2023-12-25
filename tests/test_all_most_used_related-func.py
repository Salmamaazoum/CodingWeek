from most_used_words import *
from pytest import *


def test_tweet_to_words():
    # Given
    tweet = "Le gang G9 en famille et alliés a repris le contrôle de @TVarreux ce samedi. L'un des nouveaux chars achetés au Canada 🇨🇦 par le gouvernement de facto, d'@DrArielHenry a été perdu dans une fusillade. La bataille entre les hommes armés et la @pnh_officiel continue."
    # Then
    assert '#' not in tweet_to_words(tweet)
    tweet1 = "Ce système devient chaque jour plus fou : hâtons sa fin !"
    # Then
    assert '#' not in tweet_to_words(tweet1)
    tweet2 = "Bon je suis bête mais si le médecin choisi par la partie accusatrice,  après une consultation le même soir du supposé viol, a conclu à une absence de rapport sexuel les 16 heures précédentes,  pourquoi nous en sommes là ?"
    # Then
    assert '#' not in tweet_to_words(tweet2)
