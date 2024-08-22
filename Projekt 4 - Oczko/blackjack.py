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
        Karty od 2 do 10 mają odpowiednią do swojego numeru liczbę punktów.
        Naciśnij H, aby wziąć kolejną kartę.
        Klawisz S zatrzymuje dobieranie kart.
        Przy swojej pierwszej rozgrywce możesz wcisnąć P, by podwoić swój zakład,
        ale musisz to zrobić dokładnie jeden raz przed zakończeniem dobierania kart.
        W przypadku remisu postawiona kwota jest zwracana graczowi.
        krupier kończy dobierać karty przy wartości 17.
    """
    )

    money = 5000
    while True:
        if money <= 0:
            print("Jesteś spłukany")
            print("Dobrze, że nie grałeś na prawdziwe pieniądze.")
            print("Dziękuję za grę!")
            sys.exit()
    
        print("Budżet: ", money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Zakład:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'P':
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print('Sakład zwiększony do kwoty {}.'.format(bet))
                print('Zakład:', bet)

            if move in ('D', 'P'):
                newCard = deck.pop()
                rank, suit = newCard
                print('Wziąłeś {} {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ('S', 'P'):
                break