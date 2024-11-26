stack = []
number = int(input('Enter your number: '))
while number != 0:
    rest = number%2
    stack.append(rest)
    number//=2
while stack:
    binary_digit=stack.pop()
    print(binary_digit)
