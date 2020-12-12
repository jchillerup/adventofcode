import math
import re
orders = open('input.txt').read().strip().split("\n")
order_pattern = re.compile("([NSEWLRF])([0-9]+)")

direction = 0
position = (0,0)

def sail(order, direction, position):
    m = order_pattern.match(order)
    assert(m is not None)
    assert(len(m.groups()) == 2)
    action = m.groups()[0]
    magnitude = int(m.groups()[1])
    
    if action == 'L':
        direction = (direction + magnitude) % 360
    elif action == 'R':
        direction = (direction - magnitude) % 360
    elif action == 'F':
        offset = (magnitude*math.cos(math.radians(direction)), magnitude*math.sin(math.radians(direction)))
        position = (position[0]+offset[0], position[1]+offset[1])
    elif action == 'N':
        position = (position[0], position[1]+magnitude)
    elif action == 'S':
        position = (position[0], position[1]-magnitude)
    elif action == 'E':
        position = (position[0]+magnitude, position[1])
    elif action == 'W':
        position = (position[0]-magnitude, position[1])
    
    return direction, position
    

for order in orders:
    direction, position = sail(order, direction, position)
print(position)

print(abs(position[0]) + abs(position[1]))