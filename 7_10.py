import random
computer = random.randint(1,6)
you = input("Enter your number: ")
is_correct = computer == you
print(f'you won: {is_correct}')