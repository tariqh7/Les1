while True:
    woord = input("Geef een woord van vier karakters: ")
    if len(woord)!= 4:
        print ('{} heeft {} lengte'.format(woord, str(len(woord))))
    else:
        print("{} heeft goede lengte 4".format(woord))
        break