def sum_digits(number):
    number = abs(number)
    # Convert to string and iterate over each digit
    total = 0
    for digit in str(number):
        total += int(digit)  # Convert character back to integer and sum it up
    
    return total

# Main program
any_number = int(input('Enter an integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}.')