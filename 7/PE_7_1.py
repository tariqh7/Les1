som = 0
aantal = 0
while True:
    getal = int(input("voer een getal in: "))
    if getal == 0:
        break

    else:
            som += getal
    aantal += 1

print ('{} aantal getallen en som {}'.format(str(aantal), str(som)))


getal = 1
som = 0
aantal = 0
while getal != 0:
    getal = int(input('geef een getal'))
    som = getal + som
    aantal = aantal + 1
aantal = aantal - 1
print('{} getallen ingevoerd en som is {}'.format(str(aantal), str(som)))