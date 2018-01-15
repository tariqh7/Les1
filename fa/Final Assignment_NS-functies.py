

def standaardtarief():
    vast_pr = 15    #vaste prijs
    pr_50km = 0.60  #50 km prijs
    pr = 0.80       #standaard km prijs
    afstandKM = eval(input('Hoeveel km gaan we reizen ?'))
    if (afstandKM > 50 or afstandKM ==50):
        rit_pr = afstandKM*pr_50km + vast_pr
        return rit_pr
    else :
        rit_pr = afstandKM*pr
        return rit_pr

def ritprijs():
    weekend = input('Is het weekend ?') #Vraagt of het weekend is
    leeftijd = eval(input('Hoe oud ben je ?')) #Vraagt om je leeftijd
    korting = 0 #Variable aangemaakt voor de korting
    standaardtarief = eval(input('wat was het standaard tarief ?'))
    rit_pr = 0

    if (weekend == 'ja' or 'Ja'):
        if (leeftijd >= 65 or leeftijd <= 12):
            korting = 65
        else :
            korting = 60
    else :
        if (leeftijd >= 65 or leeftijd <= 12):
            korting = 70
        else :
            korting = 100
    rit_pr = standaardtarief / 100 * korting
    return (rit_pr)

a = standaardtarief()
print('Het Standaard tarief is' , a , 'euro')

b = ritprijs()
print('De rit prijs is' , b , 'euro inclusief de korting')