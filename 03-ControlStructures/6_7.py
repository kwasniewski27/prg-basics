age = int(input('Enter your age: '))
if age < 13:
    print("you are a child")
elif age > 13 and age <= 19:
    print("you are a teenager")
elif age >= 20:
    print("you are an adult")
elif age >= 65:
    print("you are a senior")
