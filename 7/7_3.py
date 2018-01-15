dic_prog = {'Anna de munk':'8.5' ,
            'Pieter de wit':'9' ,
            'Sjaak pieterse':'9.5' ,
            'Mandy':'7',
            'Henk':'10',
            'Marco':'5',
            'Jessie':'7.5',
            'lenny':'3.5'}

for student in dic_prog.keys():
    cijfer = dic_prog[student]
    cijfer = eval(cijfer)
    if cijfer >= 9:
        print('De student {} heeft het cijfer {}'.format(str(student) , str(cijfer)))