import csv

try:
    with open('practice_9_4_products.csv') as productsfile:
        reader = csv.reader(productsfile, delimiter= ';')

        artikelnummer = ''
        kleinste_voorraad = 0
        totaal = 0
        naam = ''
        hoogsteprijs = 0
        for row in reader:
            totaal += int(row[3])
            voorraad = int(row[3])
            if kleinste_voorraad == 0:
                kleinste_voorraad = voorraad
            else:
                if voorraad < kleinste_voorraad:
                    kleinste_voorraad = voorraad

            prijs = int(row[4])

            if prijs > hoogsteprijs:
                hoogsteprijs = prijs
                naam = row[2]
        print(  )
