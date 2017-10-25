def kwadraten_som(grondgetallen):
    som = 0
    for x in grondgetallen:
        if x > 0:

            som = som + x ** 2
    return som


a = (kwadraten_som([2,5,8,6,-3]))
print (a)

