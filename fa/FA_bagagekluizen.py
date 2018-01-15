def toon_aantal_kluizen_vrij():
    file = open('kluizen.txt')
    regels = file.readlines()
    file.close()
    aantal = 12 - len(regels)
    print (" {} zijn er vrij".format(str(aantal)))


def nieuwe_kluis():
    beschikbarekluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    bestand.close()

    for regel in regels:
        kluisinfo = regel.split('t')
        kluisnummer = int(kluisinfo[0].strip())

        if kluisnummer in beschikbarekluizen:
            beschikbarekluizen.remove(kluisnummer)

    if len(beschikbarekluizen) > 0:
        kluiscode = input("voer kluiscode in: ")
        if len(kluiscode < 4):
            print ("minimaal 4 tekens")
            return
        print("U krijgt kluis me tnummer {} en code {}".format(beschikbarekluizen[0], kluiscode))

        bestand = open('kluizen.txt', 'a')
        bestand.write ('{};{}\n'.format(beschikbarekluizen[0], kluiscode))
        bestand.close()

    else:
        print('Er is helaas geen kluis meer vrij')

def kluis_openen():
    kluis_bewerken('openen')

def kluis_bewerken(actie):
    kluiscode = input('Kluiscode?')
    kluisnummer = eval(input("Kluisnummer: "))

    file = open('kluizen.txt')
    regels = file.readlines()
    file.close()

    gevonden = False
    for regel in regels:
        lijst = regel.split(";")
        kn = lijst[0] #kluisnummer
        kc = lijst [1] #kluiscode
        if kn == kluisnummer and kc == kluiscode:
            print('Kluisnummer {} gaan we {}'.format(str(kluisnummer), actie))
            gevonden = True
            if actie == 'teruggeven':
                regels.remove(regel)
                file = open('kluizen.txt', 'n')
                for nieuwe_regel in regels:
                    file.write(nieuwe_regel)
                file.close()

    if ! gevonden : #nietgevonde...
        print('Kluisnummer {} niet juist'.format(str(kluisnummer)))


def kluis_teruggeven():
    kluis_bewerken('teruggeven')



while True:
    print("1: Ik wil weten hoeveel kluizen vrij zijn")
    print("2..")
    print ("3...")
    print("4...")

    keuze = eval(input("maak uw keuze"))
    if keuze == 1:
        toon_aantal_kluizen_vrij()

    elif keuze == 2:
        nieuwe_kluis()

    elif keuze == 3:
        kluis_openen()

    elif keuze == 4:
        kluis_openen()

    elif keuze ==5:
        break
