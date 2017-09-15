cijferICOR = 7.0
cijferPROG = 7.0
cijferCSN = 7.0

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) /3


beloning = (cijferCSN + cijferPROG + cijferICOR) *30.00
overzicht = 'Mijn cijfer (gemiddeld een ' + str(gemiddelde) + ") leveren een beloning van €" + str(beloning) + " op!"

print (overzicht)
#