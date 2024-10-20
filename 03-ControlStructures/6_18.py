x = int(input('Enter x coordination: '))
y = int(input( 'Enter y coordination: '))
P = (x,y)
if x > 0 and y > 0:
    p_location = 2
elif x > 0 and y < 0:
    p_location = 3
elif x < 0 and y > 0:
    p_location = 1
elif x < 0 and y < 0:
    p_location = 4
print(f'Point P{P} is in {p_location} quadrant of the system')