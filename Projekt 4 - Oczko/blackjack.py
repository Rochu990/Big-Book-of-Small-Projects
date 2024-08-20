import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS =  chr(9827)
BACKSIDE = 'tył'

def main():
    print(""" Oczko
    Zasady:
        Spróbuj uzyskać liczbę punktów jak najbardziej zbliżoną do 21, ale nie większą.
        Króle, damy i walety mają 10 punktów.
        Asy mają 1 lub 11 punktów.
    """
    )