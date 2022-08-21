name = input("Please put your first name here:")
age = int(input("Hello "+name+",what is your age?:"))
print("Hello "+name+".")
age = str(age)
print("You are "+age+".")
age = int(age)
if age < 21:
    print("You have a whole world to explore.")
elif age == 21:
    print("You can legally drink in the USA.")
else:
    print("You are an inspiration.")