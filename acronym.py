def acronym(zin):
    woorden = zin.split()
    resultaat = ''
    for woord in woorden:
        character = woord[0]
        resultaat += character
        resultaat = resultaat.upper()
        return resultaat

antwoord = acronym('random acces memory')
print (antwoord)

antwoord = acronym('personal computer')
print (antwoord)