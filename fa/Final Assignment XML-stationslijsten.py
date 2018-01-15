import xmltodict

def verwerk_xml():
    bestand = open('stations.xml')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

stations = verwerk_xml()

print('dit zijn de codes en types van de stations:')
for station in stations ['Stations']['Station']:
    print('{:4} - {}'.format(station['Code'], station['Type']))


print('\nDit zijn alle stations met een of meer synoniemen:')

for station in stations ['Stations']['Station']:
    if station['Synoniemen'] is not None:
        for synoniem in station['Synoniemen']['Synoniem']:
            print('{} - {}'.format(station['Code'], synoniem))

print('Dit zijn de codes en de lange van de stations:')
for station in stations ['Stations']['Station']:
    print('{:4} - {}'.format(station['Code'], station ['Namen']['Lang']))