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

print('Oto', numBDays, 'dni urodzin:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

print('W tej symulacji, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Kilka osób ma urodziny', dateText)
else:
    print('nie ma takich samych dni urodzin.')
print()

print('Generowanie ', numBDays, 'losowych dni urodzin 100 000 razy...')
input('Naciśnij Enter, aby rozpocząć...')

print('Przeprowadzmy kolejnych 100 000 symulacji.')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'przeprowadzonych symulacji...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100 000 przeprowadzonych symulacji.')

probability = round(simMatch / 100_000 * 100, 2)
print('Ze 100 000 symulacji dla ', numBDays, 'osób, ten sam')
print('dzień urodzin wystąpił', simMatch, 'razy. Oznacza to,')
print('że dla ', numBDays, 'ludzi istnieje ', probability, '% szans, iż')
print('dwie lub więcej osób będzie miało urodziny w tym samym dniu.')
print('To prawdopodobnie więcej, niż przypuszczałeś.')