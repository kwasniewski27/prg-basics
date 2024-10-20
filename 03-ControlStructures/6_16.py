###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')
if extra_rinse == 'yes':
    extra_rinse_time = 15
elif extra_rinse == 'no':
    extra_rinse_time = 0
if extra_spin == 'yes':
    extra_spin_time = 9
elif extra_spin == 'no':
    extra_spin_time = 0
if program == 'j':
    total_washing_time = 40 + extra_rinse_time + extra_spin_time
    print(f'your total washing time is {total_washing_time}')
elif program == 'u':
    total_washing_time = 70 + extra_rinse_time + extra_spin_time
    print(f'your total washing time is {total_washing_time}')
elif program == 's':
    total_washing_time = 20 + extra_rinse_time + extra_spin_time
    print(f'your total washing time is {total_washing_time}')
else:
    print('wrong program')
