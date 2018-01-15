invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split('-')
nieuwe_lijst = []
for text in lijst:
    nummer = int(text)
    nieuwe_lijst.append(nummer)

nieuwe_lijst.sort()
print(nieuwe_lijst)

max = max(nieuwe_lijst)
min = min(nieuwe_lijst)

aantal = len(nieuwe_lijst)
som = sum(nieuwe_lijst)

gemiddeld = som // aantal

text = 'Max is {}, min is {}, gemiddeld {}'.format(str(max),str(min),str(gemiddeld))
print(text)
