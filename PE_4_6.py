letterlijst = ['a', 'b', 'c']
print (letterlijst)

def wijzig(letterlijst):
    qwert = ['d', 'e', 'f']
    for i in letterlijst:
        del i
    letterlijst.append(qwert)
wijzig(letterlijst)
print (letterlijst)