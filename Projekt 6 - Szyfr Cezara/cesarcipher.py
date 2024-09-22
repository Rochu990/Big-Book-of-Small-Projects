
try:
    import pyperclip
except:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Szyfr cezara szyfruje litery poprzez przesunięcie ich o liczbę,')
print('która jest kluczem. Na przykład klucz 2 oznacza, że litera A jest')
print(' zmieniona na C, litera B na D i tak dalej')
print()

while True:
    print('Czy chcesz (z)aszyfrować, czy (o)dszyfrować?')
    response = input('> '.lower())
    if response.startswith('z'):
        mode = 'zaszyfrowania'
        break
    elif response.startswith('o'):
        mode = 'odszyfrowania'
        break
    print('Proszę podać litrerę z lub o')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Proszę podać klucz (0 do {}).'.format(maxKey))
    response = input('> '.upper())
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Wpisz wiadomość do ().'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'zaszyfrowania':
            num = num + key
        elif mode == 'odszyfrowania':
            num = num - key
        
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)
        

