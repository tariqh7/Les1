hotel_prijs = 4356

try:
    aantal = int(input('Hoeveel mensen gaan er mee ?'))
    prijs_pp = hotel_prijs / aantal

    if aantal < 0:
        print('Negative invoer is niet toegestaan')
    else:
        print('De prijs per pesoon is {} euro'.format(prijs_pp))

except ZeroDivisionError:
    print('Delen door nul kan niet')
except ValueError:
    print('gebruik cijfers voor het invoeren van het aantal')
except:
    print('invoer is onjuist')









