num1 = int(raw_input("Give a number: "))
num2 = int(raw_input("Give another number: "))
mod = num1 % num2

if mod == 0:
    print(str(num2) + " is a factor of " + str(num1))
else:
    print(str(num2) + " is not a factor of " + str(num1))
