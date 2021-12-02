
inp = open('input', 'r').read().strip().split('\n')

hpos = 0
vpos = 0

for order in inp:
    direction, value = order.split(' ')
    
    if direction == "forward":
        hpos += int(value)
    elif direction == "down":
        vpos += int(value)
    elif direction == "up":
        vpos -= int(value)
    else:
        raise ValueError("Undefined direction")

print (hpos*vpos)