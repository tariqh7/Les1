def seizoen(maand):
    if maand >= 3 and maand <=5:
        print("Het is lente")

    elif maand >= 9 and maand <=11:
        print ("Het is herfst ")

    elif maand >=12 and maand <=2:
        print("het is winter")

    elif maand >= 6 and maand <=8:
        print("Het is zomer")

    elif maand >13:
        print('Vul getal kleiner in dan 12')



    
seizoen(int(input("Vul maandnummer in: ")))












#https://stackoverflow.com/questions/15193927/what-does-these-operators-mean-python