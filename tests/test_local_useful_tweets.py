from localisation import local_useful_tweets
from pytest import *


def test_localisations():
    # Then
    assert 'paris' in local_useful_tweets()
    # Then
    assert local_useful_tweets()['ile-de-france'] == 989
