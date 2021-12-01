import math
import re
orders = open('input.txt').read().strip().split("\n")
order_pattern = re.compile("([NSEWLRF])([0-9]+)")

direction = 0
ship_position = (0,0)
waypoint_position = (1, 10)

def sail(order, direction, ship_position, waypoint_position):
    m = order_pattern.match(order)
    assert(m is not None)
    assert(len(m.groups()) == 2)
    action = m.groups()[0]
    magnitude = int(m.groups()[1])
    
    if action == 'L':
        x, y = waypoint_position
        theta = math.radians(-1*magnitude)

        waypoint_position = (x * math.cos(theta) - y * math.sin(theta) ,
                             y * math.cos(theta) + x * math.sin(theta) )
    elif action == 'R':
        x, y = waypoint_position
        theta = math.radians(magnitude)

        waypoint_position = (x * math.cos(theta) - y * math.sin(theta) ,
                             y * math.cos(theta) + x * math.sin(theta) )
    elif action == 'F':
        ship_position = (ship_position[0]+magnitude*waypoint_position[0], ship_position[1]+magnitude*waypoint_position[1])
    elif action == 'N':
        waypoint_position = (waypoint_position[0]+magnitude, waypoint_position[1])
    elif action == 'S':
        waypoint_position = (waypoint_position[0]-magnitude, waypoint_position[1])
    elif action == 'E':
        waypoint_position = (waypoint_position[0], waypoint_position[1]+magnitude)
    elif action == 'W':
        waypoint_position = (waypoint_position[0], waypoint_position[1]-magnitude)
    
    return direction, ship_position, waypoint_position
    
print("NOP", "ship", ship_position, "wayp", waypoint_position)
for order in orders:
    direction, ship_position, waypoint_position = sail(order, direction, ship_position, waypoint_position)
    print("%3s" %order, "ship", ship_position, "wayp", waypoint_position)
print(ship_position)

print(abs(ship_position[0]) + abs(ship_position[1]))