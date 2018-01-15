def convert(temperatuurC):
    temperatuurF = (temperatuurC * 1.8) + 32
    return (temperatuurF)

for i in range(-30, 41, 10):
    print(convert(i), (i))