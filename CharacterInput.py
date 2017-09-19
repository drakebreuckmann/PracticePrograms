name = raw_input("What is your name? ")

age = int(raw_input("How old are you? "))

prints = int(raw_input("How many copies do you want? "))

year = 2017
ohyear = (year + (100-age))


print (prints * ("\n" + "Your name is " + name + "\n" + "You are " + str(age) + " years old" + "\n" + "You will turn 100 in " + str(ohyear) + "\n"))
