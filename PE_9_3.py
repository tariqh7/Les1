import csv
bestandsnaam = 'practice_9_3_scores.csv'
try:
    with open(bestandsnaam) as gamersfile:
        reader = csv.reader(gamersfile, delimiter = ';')

        hoogstescore = -1
        naam = ''
        datum = ''
        for row in reader:
            score = int(row[2])
            if score > hoogstescore:
                naam = row[0]
                datum = row[1]
                hoogstescore = score
        print('De hoogste score is {} op {} behaald door {}'.format(str(hoogstescore), datum, naam))

except IOError:
    print('kan bestand niet lezen')
except NameError:
    print('Score is onjuist')