def standaardprijs(afstandKM):
    if afstandKM > 50:
        return 15 + (afstandKM - 50) * 0.6
    elif afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.8


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)
    prijs = 0
    if leeftijd <= 12 or leeftijd >= 65:
        if weekendrit:
            prijs = standaard * 0.65
        else:
            prijs = standaard * 0.7
    elif weekendrit:
        prijs = standaard * 0.6
    return prijs


