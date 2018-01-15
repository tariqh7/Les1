def seizoen(nummer):
    seizoen = ' '
    if nummer >= 3 and nummer <=5:
        seizoen = 'lente'
    elif nummer >5 and nummer <=8:
        seizoen = 'zomer'
    elif nummer > 8 and nummer <=11:
        seizoen = 'herfst'
    else:
        seizoen = 'winter'
    return seizoen

for maand in range(1, 13):
    text = 'Voor maand {} is het seizoen {}'.format(str(maand), seizoen(maand))
    print(text)