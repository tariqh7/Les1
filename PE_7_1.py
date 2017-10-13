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
