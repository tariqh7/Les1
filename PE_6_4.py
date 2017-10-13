studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw=[]
    for cijfers_van_student in studentencijfers:
        som = sum(cijfers_van_student)
        aantal = len(cijfers_van_student)
        gemiddelde = som / aantal
        antw.append(gemiddelde)
        return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    lijst = gemiddelde_per_student(studentencijfers)
    antw = sum(lijst) / len(lijst)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))