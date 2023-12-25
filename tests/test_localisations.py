from stats.localisation import localisations
from pytest import *


def test_localisations():
    # Given
    filename = 'Fusillade.csv'
    # Then
    assert localisations(filename) == (738, 781, 759)
    # Given
    filename1 = 'Viol.csv'
    # Then
    assert len(localisations(filename1)) == 3
