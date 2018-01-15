f = open('hardlopers.txt','a')

number = input("What is the number of the runner?: ")
time = input("What is the time of the runner?: ")
f.write("The number is: " + number)
f.write("\n")
f.write("The time is: " + time)
f.write("\n")

f.close()