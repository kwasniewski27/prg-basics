dogs_age = int(input('Enter your dogs age: '))
human_age_after_2years = 10.5
if dogs_age == 1:
    dogs_years = human_age_after_2years
elif dogs_age == 2:
    dogs_years = human_age_after_2years*2
elif dogs_age > 2:
    dogs_years = human_age_after_2years*2 + (dogs_age - 2)*4
print(f'your dog is {dogs_years} dogs years old')