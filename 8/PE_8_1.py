bruin = {'Boxtel', 'Best', 'Eindhoven', 'Helmond \'t hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel....'}

print('beide trajecten doen de volgende stations aan: {}'.format(bruin.intersection(groen)))
print('traject bruin doet als enige deze stations aan: {}'.format(bruin.difference(groen)))
print('alle stations op beide trajecten: {}'.format(bruin.union(groen)))