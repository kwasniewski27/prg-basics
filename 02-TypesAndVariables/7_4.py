#Enter tree circumference in cm: 120 
#Tree can be cut down: False
import math
tree_circumference = int(input('enter tree circumference in cm: '))
tree_diameter = tree_circumference / math.pi
tree_can_be_cut_down = tree_diameter >= 50
tree_cant_be_cut_down = tree_diameter < 50
print(f'tree can be cut down {tree_can_be_cut_down}')
print(f'tree cant be cut down {tree_cant_be_cut_down}')