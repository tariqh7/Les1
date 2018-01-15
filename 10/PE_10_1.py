import xmltodict

def verwerk_xml():
    bestand = open('practice_10_10_products.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

artikelen = verwerk_xml()

for artikel in artikelen ['artikelen']['artikel']:
    print(artikel['naam'])


#of

