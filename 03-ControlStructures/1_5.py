###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('correct tasks: '))

if tasks_ok >= total_tasks/2 :
    test_passed = True
else:
    test_passed = False

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')