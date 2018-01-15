file = open('kaartnummers.txt')
lines = file.readlines()
file.close()

regelnummer = 0
regels = 0
hoogste = 0
for line in lines:
    regels = regels + 1
    lijst = line.split(',')
    nummer = int(lijst[0])
    if nummer > hoogste:
        hoogste = nummer
        regelnummer = regels
text = 'aantal regels is {}, en hoogste is {} regelnummer {}'.format(str(regels), str(hoogste), str(regelnummer))

print (text)


