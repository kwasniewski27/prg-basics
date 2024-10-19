###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
 # False - switch off, True - switch on
light_switch1 = str(input('first switch is on (True/False): '))
light_switch2 = str(input('second switch is on (True/False): '))
bulbs_on = '0'
if light_switch1 == True:
    bulbs_on + '1'
elif light_switch2 == True:
    bulbs_on + '2'
elif light_switch1 == False:
    bulbs_on += '0'
elif light_switch2 == False:
    bulbs_on += '0'
print(f'there is {bulbs_on} bulbs on')