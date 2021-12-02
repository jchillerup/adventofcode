
inp = open('input', 'r').read().strip().split('\n')

hpos = 0
vpos = 0
aim = 0

for order in inp:
    direction, value = order.split(' ')
    
    if direction == "forward":
        hpos += int(value)
        vpos += aim * int(value)
    elif direction == "down":
        aim += int(value)
    elif direction == "up":
        aim -= int(value)
    else:
        raise ValueError("Undefined direction")

print (hpos*vpos)