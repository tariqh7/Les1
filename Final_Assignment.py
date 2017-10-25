for line in lines:
    print (line)
    nummer_naam = line.split(',')
    naam = nummer_naam[1].strip()
    nummer = nummer_naam[0].strip()
    text = '{} heeft kaartnummer: {}'.format(naam, nummer)


    #met .strip() haal je spaties weg