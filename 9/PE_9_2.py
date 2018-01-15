import datetime
import csv

bestand = 'inloggers.csv'
#gebruik hier een herhalingslus:
while True:
    naam = input("Wat is je achternaam? ")
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    if naam == 'einde':
        break

    datumstr = datetime.datetime.now().strftime(( ''))

    with open(bestand, 'a') as inloggersfile:

        try: #maak eerst tuple
            waarde = (datumstr, voorl, gbdatum, email)
            writer = csv.writer(inloggersfile)
            writer.writerow(waarde)

        except IOError:
            print('mislukt om naar bestand te schrijven')






#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file