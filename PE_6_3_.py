invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split('-')
lijst.sort()
gesorteerd = ("Gesorteerde list van ints: {}".format(lijst))
print(gesorteerd)

Grootste = max(lijst)
kleinste = min(lijst)
GK = ("Grootste getal: {} en kleinste getal {}".format(Grootste,kleinste))
print(GK)

gemiddelde = sum(lijst) / len(lijs)

Aantal = len(lijst)
som = sum(lijst)
aant = ("Aantal getallen: {} en som: {}".format(str(Aantal), str(som)))
print(Aantal)

