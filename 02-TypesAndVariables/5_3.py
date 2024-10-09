###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
import math
a = input('a=')
b = input('b=')
c = input('c=')
a = float (a)
b = float (b)
c = float (c) 
cuboid_volume = a*b*c
cuboid_surface_area = a*b*2 + b*c*2 + a*c*2
print(f'the volume of cuboid equals {cuboid_volume}')
print(f'cuboids surface area equals {cuboid_surface_area}')