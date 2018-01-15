def code(string):
    waarde = ''
    for char in string:
        o = ord(char)
        o = o + 3
        nieuwe_char = chr(o)
        waarde = waarde + nieuwe_char
    return waarde

string = input("geef naam beginstation eindstation")
a = code(string)

print('de code is {}'.format(a))


