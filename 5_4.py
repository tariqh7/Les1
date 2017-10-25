while True:
    naam = input('Wat is je naam? ')
    if naam == 'stop':
        break
    else:
        text = '{} {}\n'.format(s, naam)
        outfile.write(text)

outfile.close()

#5.4