def namen():
    namen_dic = {}
    nieuwe_naam = 'a'
    max_key = 0

    while nieuwe_naam != '':
        nieuwe_naam = input('Voer de naam van een leerling in: ')

        if nieuwe_naam not in namen_dic.keys():
            value = 1
            namen_dic[nieuwe_naam] = value


        else:
            value = namen_dic[nieuwe_naam]
            value += 1
            namen_dic[nieuwe_naam] = value

        if value > max_key:
            max_key = value



    namen_dic.pop('')

    for i in range(0 , max_key + 1):
        for tuple in namen_dic.items():
            if tuple[1] == i:
                if tuple[1] == 1:
                    print('Er is 1 student met de naam {}'.format(tuple[0]))
                else:
                    print('Er zijn {} studenten met de naam {}'.format(tuple[1] , tuple[0]))



namen()