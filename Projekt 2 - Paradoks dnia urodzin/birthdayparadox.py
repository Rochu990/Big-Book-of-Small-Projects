import datetime, random     

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.datetime(2001, 1, 1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

print('''Paradoks dnia urodzin
      Paradoks dnia urodzin pokazuje, że w grupie N osób szansan
      na dwie osoby mają urodziny w tym samym dniu, jest zaskakująco duża.
      Ten program wykorzystuje metodę Monte Carlo (czyli powtarzalne losowe
      symulacja), by ustalic to prawdopodobieństwo

      To tak naprawdę nie jest paradoks, tylko zaskakujący wynik.
      ''') 

MONTHS = ('Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
          'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru')

while True:
    print('Ile urodzin powinienem wygenerować?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()