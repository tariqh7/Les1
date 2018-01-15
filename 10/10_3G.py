x = 1
y = 3

def doe1():
    global x
    y = 4
    x = 0
    return x+y

def doe2():
    x = doe1()
    x += 2
    return x

doe2()
print(x)
print('\n Antwoord is A')